import os
import logging
from sqlalchemy import create_engine, MetaData, exc
from dotenv import load_dotenv
from .database_management import DatabaseManagement
from .llm_integration import LLMIntegration
from .query_handling import QueryHandling

load_dotenv(override=True)
logging.basicConfig(level=logging.INFO, format='%(message)s')

class PostgresDB(DatabaseManagement, LLMIntegration, QueryHandling):
    def __init__(self, name: str = 'db', postgres_username: str = None, postgres_password: str = None, postgres_host: str = None) -> None:
        """
        Initialize the PostgresDB instance.

        Args:
            name (str): The name of the database.
            postgres_username (str): The PostgreSQL username.
            postgres_password (str): The PostgreSQL password.
            postgres_host (str): The PostgreSQL host.
        """
        try:
            self.name = name
            self.postgres_username = postgres_username or os.getenv("POSTGRES_DB_USERNAME")
            self.postgres_password = postgres_password or os.getenv("POSTGRES_DB_PASSWORD")
            self.postgres_host = postgres_host or os.getenv("POSTGRES_DB_HOST")

            if not self.postgres_password or not self.postgres_host:
                raise ValueError("Please provide a password and host for the database either by passing them in or providing them in a .env file.")

            self.default_engine = create_engine(f'postgresql://{self.postgres_username}:{self.postgres_password}@{self.postgres_host}/postgres')
            self._ensure_database_exists()
            self.engine = create_engine(f'postgresql://{self.postgres_username}:{self.postgres_password}@{self.postgres_host}/{self.name}')
            self.metadata = MetaData()
            logging.info(f"Connecting to database '{self.name}'...")
            self.connection = self._connect_to_database()
        except Exception as e:
            logging.error(f"Error initializing PostgresDB: {e}")
            raise

    def _ensure_database_exists(self):
        """
        Ensure the specified database exists, creating it if necessary.
        """
        try:
            self.default_engine.connect()
            self._create_database(db_name=self.name)
        except exc.OperationalError as e:
            logging.error(f"Failed to connect to the default 'postgres' database: {e}")
            raise
        except Exception as e:
            logging.error(f"Error ensuring database exists: {e}")
            raise

    def _connect_to_database(self):
        """
        Connect to the specified database.

        Returns:
            connection: The database connection object.
        """
        try:
            connection = self.engine.connect()
            logging.info(f"Successfully connected to database '{self.name}'.")
            return connection
        except exc.OperationalError as e:
            logging.error(f"Failed to connect to the database '{self.name}': {e}")
            raise
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
            raise