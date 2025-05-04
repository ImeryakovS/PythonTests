import logging
import sqlite3
import traceback
from functools import wraps
import requests

def api_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except requests.exceptions.HTTPError as e:
            logging.error(f'[{func.__name__}]: HTTPError: {e}')
            raise
        except requests.exceptions.RequestException as e:
            logging.error(f'[{func.__name__}]: RequestException: {e}')
            raise
        except Exception as e:
            logging.error(f'[{func.__name__}]: Unexpected error: {e}\n{traceback.format_exc()}')
            raise
    return wrapper

def db_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except sqlite3.OperationalError as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): OperationalError: {e}')
            raise
        except sqlite3.IntegrityError as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): IntegrityError: {e}')
            raise
        except sqlite3.ProgrammingError as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): ProgrammingError: {e}')
            raise
        except sqlite3.DatabaseError as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): DatabaseError: {e}')
            raise
        except sqlite3.Error as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): Error: {e}')
            raise
        except Exception as e:
            logging.error(f'[{func.__name__}]({args},{kwargs}): Unexpected error: {e}\n{traceback.format_exc()}')
            raise
    return wrapper

def retry(attempts):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retries += 1
                    logging.error(f'[{func.__name__}] is not working. Try attempt = {retries}. {e}')
                    if retries == attempts:
                        logging.error(f'[{func.__name__}]: Unexpected error: {e}\n{traceback.format_exc()}')
                        raise e
        return wrapper
    return decorator

## Можно добавить в декоратор retry обработку обработку только сетевых и 5xx ошибок.


