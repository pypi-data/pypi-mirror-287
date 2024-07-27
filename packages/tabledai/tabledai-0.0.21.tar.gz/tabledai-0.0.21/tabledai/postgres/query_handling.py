import logging
from decimal import Decimal
from typing import Dict, Optional, Any

class QueryHandling:
    def _query_cleaning(self, query: str) -> str:
        """
        Clean and normalize the input query by replacing specific words.

        Args:
            query (str): The input query string.

        Returns:
            str: The cleaned and normalized query string.
        """
        break_words = {
            'maximum': 'max',
            'minimum': 'min',
        }
        query = query.lower()
        for word, replacement in break_words.items():
            query = query.replace(word, replacement)
        return query

    def query(self, query: str, generative: bool = False, n_retries: int = 2) -> Dict[str, Optional[Any]]:
        """
        Process the input query and generate an SQL query, execute it on the database, 
        and optionally generate a generative response.

        Args:
            query (str): The input query string.
            generative (bool): Flag to indicate if a generative response is required.
            n_retries (int): The number of retry attempts for generating and executing the SQL query.

        Returns:
            dict: A dictionary containing the results of the query execution.
        """
        result = {'success': False, 'message': None, 'sql': None, 'data': None, 'generation': None}
        query = self._query_cleaning(query)
        if n_retries < 0 or not isinstance(n_retries, int):
            logging.info("The number of retries must be a positive integer. Defaulting to 2 retries.")
            n_retries = 2
        
        retry_sql = None
        error_message = None
        for i in range(n_retries + 1):
            if i > 0:
                retry_prompt = (
                    f"The user query was: '{query}'\n\n"
                    f"The SQL query generated from OpenAI in the first attempt is: '{retry_sql}'.\n\n"
                    f"This SQL failed to execute due to the following error:\n\n'{error_message}'.\n\n"
                    f"Please try to generate the appropriate SQL again, taking into account the error message. Make adjustments based on the above error message.\n\n"
                )
                prompt = self._build_sql_prompt(query, starter_prompt=retry_prompt)
            else:
                prompt = self._build_sql_prompt(query)
                logging.info(f"Generating SQL for query: '{query}'...")
            
            sql_dict = self._sql_openai_call(prompt)
            if not sql_dict:
                logging.error("Failed to generate SQL query, trying again.")
                error_message = "Failed to generate SQL query."
                continue
            
            sql = sql_dict.get('sql')
            in_domain = sql_dict.get('in_domain')
            if not in_domain:
                logging.error("SQL query generated is not in domain, trying again.")
                result['message'] = "Query is not in domain. Please ask a different question."
                return result

            db_result_dict = self._query_db(sql)
            if not db_result_dict.get('success'):
                logging.error(f"Error message: {db_result_dict.get('message')}")
                logging.error(f"SQL: '{sql}'")
                retry_sql = sql
                error_message = db_result_dict.get('message')
                logging.error("Couldn't execute SQL on the database. Tweaking the query and trying again...")
                logging.info('-' * 50)
                continue
            
            result_df = db_result_dict.get('data')
            if result_df.empty:
                logging.info("Query returned no results.")
                error_message = "Query returned no results."
                continue
            
            logging.info("Query executed successfully.")
            for col in result_df.columns:
                if result_df[col].dtype == object and isinstance(result_df[col].iloc[0], Decimal):
                    result_df[col] = result_df[col].astype(float)
            
            result['success'] = True
            result['sql'] = sql
            result['message'] = "Query executed successfully."
            result['data'] = result_df.to_dict(orient='records')

            if generative:
                generative_prompt = self._build_generative_prompt(query, result_df)
                result['generation'] = self._generative_openai_call(generative_prompt)
            
            return result

        result['message'] = "Failed to execute query after retries."
        return result