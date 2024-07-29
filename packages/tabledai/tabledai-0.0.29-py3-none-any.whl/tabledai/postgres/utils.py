import logging
import pandas as pd
from sqlalchemy import types
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def disable_logging(func):
    def wrapper(*args, **kwargs):
        logging.disable(logging.CRITICAL)
        try:
            return func(*args, **kwargs)
        finally:
            logging.disable(logging.NOTSET)
    return wrapper

def map_types(dtype: pd.api.types) -> types.TypeEngine:
    if pd.api.types.is_integer_dtype(dtype):
        return types.Integer()
    elif pd.api.types.is_float_dtype(dtype):
        return types.Float()
    elif pd.api.types.is_bool_dtype(dtype):
        return types.Boolean()
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return types.DateTime()
    else:
        return types.String()
    
def create_default_uri_from_env():
    if all([os.getenv("POSTGRES_DB_USERNAME"), os.getenv("POSTGRES_DB_PASSWORD"), os.getenv("POSTGRES_DB_HOST"), os.getenv("POSTGRES_DB_PORT"), os.getenv("POSTGRES_DB_DEFAULT_NAME")]):
        return (
            f"postgresql://{os.getenv('POSTGRES_DB_USERNAME')}:{os.getenv('POSTGRES_DB_PASSWORD')}@{os.getenv('POSTGRES_DB_HOST')}:"
            f"{os.getenv('POSTGRES_DB_PORT')}/{os.getenv('POSTGRES_DB_DEFAULT_NAME')}?sslmode={os.getenv('POSTGRES_DB_SSLMODE', 'require')}"
        )
    else:
        return None