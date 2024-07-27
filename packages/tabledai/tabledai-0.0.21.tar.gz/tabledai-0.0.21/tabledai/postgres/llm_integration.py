import logging
import re
import pandas as pd
from sqlalchemy import text
from .utils import disable_logging
from openai import OpenAI

client = OpenAI()

class LLMIntegration:
    def _build_sql_prompt(self, query: str, starter_prompt: str = '') -> str:
        """
        Build a SQL prompt for generating SQL queries from a given query string.

        Args:
            query (str): The input query string.
            starter_prompt (str): An optional starter prompt to include additional context.

        Returns:
            str: The constructed prompt string.
        """
        try:
            prompt = starter_prompt
            prompt += f"""You are a Postgres SQL expert who has been tasked with writing a SQL query to extract data from the database based on this query: '{query}'."""
            with self.engine.connect() as con:
                columns_result = con.execute(text("""
                    SELECT table_name, column_name, data_type
                    FROM information_schema.columns
                    WHERE table_schema = 'public'
                    ORDER BY table_name, column_name;
                """))
                table_columns = columns_result.fetchall()

                primary_keys_result = con.execute(text("""
                    SELECT kcu.table_name, tco.constraint_name, kcu.column_name 
                    FROM information_schema.table_constraints tco
                    JOIN information_schema.key_column_usage kcu 
                        ON kcu.constraint_name = tco.constraint_name
                        AND kcu.constraint_schema = tco.constraint_schema
                        AND kcu.constraint_name = tco.constraint_name
                    WHERE tco.constraint_type = 'PRIMARY KEY' AND kcu.table_schema = 'public'
                    ORDER BY kcu.table_name, kcu.column_name;
                """))
                primary_keys = primary_keys_result.fetchall()

                foreign_keys_result = con.execute(text("""
                    SELECT 
                        kcu.table_name AS foreign_table,
                        rel_kcu.table_name AS primary_table,
                        kcu.column_name AS foreign_column,
                        rel_kcu.column_name AS primary_column
                    FROM 
                        information_schema.table_constraints tco
                        JOIN information_schema.key_column_usage kcu
                        ON tco.constraint_schema = kcu.constraint_schema
                        AND tco.constraint_name = kcu.constraint_name
                        JOIN information_schema.referential_constraints rco
                        ON tco.constraint_schema = rco.constraint_schema
                        AND tco.constraint_name = rco.constraint_name
                        JOIN information_schema.key_column_usage rel_kcu
                        ON rco.unique_constraint_schema = rel_kcu.constraint_schema
                        AND rco.unique_constraint_name = rel_kcu.constraint_name
                        AND kcu.ordinal_position = rel_kcu.ordinal_position
                    WHERE tco.constraint_type = 'FOREIGN KEY' AND kcu.table_schema = 'public'
                    ORDER BY kcu.table_name, kcu.column_name;
                """))
                foreign_keys = foreign_keys_result.fetchall()

                prompt += f"\n\nHere is the information about the database tables:\n\n"
                for table in table_columns:
                    prompt += f"Table: {table[0]}, Column: {table[1]}, Data Type: {table[2]}\n"

                prompt += f"\nPrimary Keys:\n"
                for pk in primary_keys:
                    prompt += f"Table: {pk[0]}, Column: {pk[2]}, Constraint: {pk[1]}\n"

                prompt += f"\nForeign Keys:\n"
                for fk in foreign_keys:
                    prompt += f"Foreign Table: {fk[0]}, Foreign Column: {fk[2]}, Primary Table: {fk[1]}, Primary Column: {fk[3]}\n"

            prompt += f"""
                The query will be run against a Postgres database.

                CONTEXTUAL INSTRUCTIONS:
                - Understand the context of the request to ensure the SQL query correctly identifies and filters for the relevant entities.
                - Maintain context from previous questions and ensure the current query builds on previous results when needed.
                - Be mindful of pronouns and ambiguous terms, ensuring they are mapped to the correct entities and columns.

                SQL INSTRUCTIONS:
                - The query must be written specifically for PostgreSQL.
                - Do not use parameterized queries.
                - Only use the columns from the provided table information.
                - Try to make the query as efficient as possible.
                - Round computation results to two decimal places.
                - Avoid symbols such as '?', '(', ')', '%', '$', ':' in comparisons.
                - Use 'LIKE' for string comparisons instead of '='.
                - Use wildcard characters with 'LIKE' for partial matches (e.g., '%value%').
                - Write a SQL query adhering to general SQL standards.
                - Ensure the query does not exceed the LLM's context length.
                - Ensure the query is syntactically correct for PostgreSQL.
                - Format date comparisons as 'YYYY-MM-DD HH:MM:SS' and consider PostgreSQL's date functions.
                - Use case-insensitive comparisons (e.g., 'WHERE LOWER(column_name) LIKE ...').
                - Optimize the query to return only the necessary data using clauses like 'DISTINCT', 'WHERE', 'GROUP BY', 'ORDER BY', 'LIMIT', 'JOIN', 'UNION'.
                - Explicitly cast fields to the appropriate data types when performing operations like ROUND, AVG, SUM, CORR, etc., to avoid type mismatch errors.
                - Eliminate null values in all columns to ensure accurate results. Use 'WHERE column_name IS NOT NULL' for all relevant columns.
                - Do not use aggregate functions in the WHERE clause. Use HAVING for conditions involving aggregate functions or FILTER.
                - Example of the explicit casting issue: 
                    -- This SQL would fail: 'SELECT product_category, ROUND(CORR(price::double precision, sales::double precision), 2) AS price_sales_correlation FROM sales_data GROUP BY product_category ORDER BY product_category;'
                    -- This SQL would succeed: 'SELECT product_category, ROUND(CAST(CORR(price::double precision, sales::double precision) AS numeric), 2) AS price_sales_correlation FROM sales_data GROUP BY product_category ORDER BY product_category;'

                HERE ARE 8 EXAMPLES OF USER QUESTIONS AND THE GENERATED SQL THAT ANSWERED THAT USER QUESTION:
                1: User Question: How does the correlation between Frequency and Signal Strength change under different Weather Conditions?
                1: SQL: SELECT weather_condition, ROUND(CAST(CORR(frequency::double precision, signal_strength::double precision) AS numeric), 2) AS freq_signal_correlation FROM logged_data WHERE frequency IS NOT NULL AND signal_strength IS NOT NULL AND weather_condition IS NOT NULL GROUP BY weather_condition ORDER BY weather_condition;

                2: User Question: What are the average Temperature and Humidity levels for each unique combination of Device Type and Antenna Type?
                2: SQL: SELECT device_type, antenna_type, ROUND(AVG(temperature)::numeric, 2) AS avg_temperature, ROUND(AVG(humidity)::numeric, 2) AS avg_humidity FROM logged_data WHERE temperature IS NOT NULL AND humidity IS NOT NULL AND device_type IS NOT NULL AND antenna_type IS NOT NULL GROUP BY device_type, antenna_type;

                3: User Question: Which Location experiences the highest average Wind Speed during Rainy weather conditions, and what is the average Signal Strength in that location?
                3: SQL: SELECT location, ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed, ROUND(AVG(signal_strength)::numeric, 2) AS avg_signal_strength FROM logged_data WHERE LOWER(weather_condition) LIKE '%rain%' AND wind_speed IS NOT NULL AND signal_strength IS NOT NULL AND location IS NOT NULL GROUP BY location ORDER BY avg_wind_speed DESC LIMIT 1;

                4: User Question: How does the Battery Level impact the CPU Usage and Memory Usage across different Power Sources?
                4: SQL: SELECT ROUND(battery_level::numeric, 2) AS battery_level, ROUND(AVG(cpu_usage)::numeric, 2) AS avg_cpu_usage, ROUND(AVG(memory_usage)::numeric, 2) AS avg_memory_usage, power_source FROM logged_data WHERE battery_level IS NOT NULL AND cpu_usage IS NOT NULL AND memory_usage IS NOT NULL AND power_source IS NOT NULL GROUP BY battery_level, power_source ORDER BY battery_level, power_source;

                5: User Question: What is the correlation between Disk Usage and System Load across different Device Types?
                5: SQL: SELECT device_type, ROUND(CAST(CORR(disk_usage, system_load) AS numeric), 2) AS disk_usage_system_load_correlation FROM logged_data WHERE disk_usage IS NOT NULL AND system_load IS NOT NULL AND device_type IS NOT NULL GROUP BY device_type ORDER BY device_type;

                6: User Question: How do Temperature and Precipitation jointly impact the occurrence of different Interference Types?
                6: SQL: SELECT interference_type, ROUND(CAST(AVG(temperature) AS numeric), 2) AS avg_temperature, ROUND(CAST(AVG(precipitation) AS numeric), 2) AS avg_precipitation FROM logged_data WHERE temperature IS NOT NULL AND precipitation IS NOT NULL AND interference_type IS NOT NULL GROUP BY interference_type ORDER BY interference_type;

                7: User Question: Which Antenna Type is most effective in maintaining high Signal Strength across varying Bandwidth values and Weather Conditions?
                7: SQL: SELECT antenna_type, ROUND(AVG(signal_strength), 2) AS avg_signal_strength FROM logged_data WHERE signal_strength IS NOT NULL AND bandwidth IS NOT NULL AND weather_condition IS NOT NULL GROUP BY antenna_type ORDER BY avg_signal_strength DESC LIMIT 1;

                8: User Question: How does the usage of different Modulation methods affect the correlation between Temperature and Humidity, and what are the average values for each combination?
                8: SQL: SELECT modulation, ROUND(CAST(CORR(temperature::double precision, humidity::double precision) AS numeric), 2) AS temp_humidity_correlation, ROUND(AVG(temperature::double precision)::numeric, 2) AS avg_temperature, ROUND(AVG(humidity::double precision)::numeric, 2) AS avg_humidity FROM logged_data WHERE temperature IS NOT NULL AND humidity IS NOT NULL AND modulation IS NOT NULL GROUP BY modulation ORDER BY modulation;
                    
                RESPONSE INSTRUCTIONS:
                - Return ONLY the following key-value pairs: 'sql': "your sql query here" and 'in_domain': "boolean True or False if you think the query relates data in the database and will be answered with the SQL".
                - Only include the dictionary in the response. Don't include '```python' or '```' in the response.
                - The response should be a python dictionary that returns 'dict' when evaluated: type(eval(response)) == dict
            """
            return prompt
        except Exception as e:
            logging.error(f"Error building SQL prompt: {e}")
            raise

    @disable_logging
    def _sql_openai_call(self, prompt: str) -> dict:
        """
        Make a call to the OpenAI API to generate SQL based on the prompt.

        Args:
            prompt (str): The constructed prompt string.

        Returns:
            dict: The generated SQL query and in_domain status.
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant and a SQL expert for Postgres databases."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            result = response.choices[0].message.content
            result = re.sub(r'```.*?```', '', result, flags=re.DOTALL)
            if isinstance(eval(result), dict) and 'sql' in eval(result) and 'in_domain' in eval(result):
                return eval(result)
            return None
        except Exception as e:
            logging.error(f"Error in _sql_openai_call: {e}")
            return None

    def _build_generative_prompt(self, query: str, df: pd.DataFrame) -> str:
        """
        Build a prompt for generating a response based on the query and DataFrame.

        Args:
            query (str): The input query string.
            df (pd.DataFrame): The DataFrame containing the query results.

        Returns:
            str: The constructed prompt string for generative response.
        """
        try:
            prompt = f"""
            Based on the question:\n\n**{query}**\n\n the following data was found:\n\n
            SQL Data in JSON format: {df.to_json()}\n

            Do not make reference to the data sources themselves, only reference the data. For example, don't mention 'the data', 'JSON', 'SQL data', 'databases', etc.\n

            Unless specified in the query, don't show your work for mathematical calculations. Only provide the final answer.\n

            **This is a retrieval-augmented generation task, so it is critical that you only generate the answer based on the data provided in this prompt.**
            **If you need to make any assumptions, please state them clearly.**
            **If you think the data provided is insufficient to generate the answer, please state that as well.**
            """
            return prompt
        except Exception as e:
            logging.error(f"Error building generative prompt: {e}")
            raise

    @disable_logging
    def _generative_openai_call(self, prompt: str) -> str:
        """
        Make a call to the OpenAI API to generate a response based on the prompt.

        Args:
            prompt (str): The constructed prompt string.

        Returns:
            str: The generated response.
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant and a SQL expert for Postgres databases."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return None