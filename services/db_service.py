import sqlite3
import logging

from datetime import datetime
from config.settings import DB_PATH
from helpers.decorators import db_error_handler


class DBService:

    @staticmethod
    @db_error_handler
    def connect():
        conn = sqlite3.connect(DB_PATH)
        logging.info(f'Connected to {DB_PATH}')
        return conn

    @staticmethod
    @db_error_handler
    def create_user(login, email, name, password, version = 0, org_id = 1, is_admin = 0, created = 0, updated = 0):
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with DBService.connect() as connection:
            connection.execute(
                "INSERT INTO user (login, email, name, password, version, org_id, is_admin, created, updated) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (login, email, name, password, version, org_id, is_admin, created, updated)
            )
            logging.info(f'Created user {login} with parameters {email, name, password, version, org_id, is_admin, created, updated}')


    @staticmethod
    @db_error_handler
    def find_user_by_email(email):
        with DBService.connect() as connection:
            cursor = connection.execute(
                "SELECT login, email, name FROM user WHERE email = ?",
                (email,)
            )
            logging.info(f'Found user {email} with parameters {email}')
            return cursor.fetchone()

    @staticmethod
    @db_error_handler
    def delete_user_by_login(login):
        with DBService.connect() as connection:
            connection.execute("DELETE FROM user WHERE login = ?", (login,))
            logging.info(f'Deleted user {login}')