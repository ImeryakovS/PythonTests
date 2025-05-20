import requests
from requests import Response
import logging

import config.settings as settings

from data.users_credentials import change_password
from helpers.decorators import api_error_handler, retry
from services.utils import write_value_in_json, read_value_in_json, total_log_in_method


class ApiUsersService:

    @staticmethod
    @api_error_handler
    @retry(3)
    def create_api_user(credentials: dict) -> Response:
        url = f'{settings.BASE_URL}/api/admin/users'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url,
                                 auth=settings.BASIC_AUTH,
                                 json=credentials,
                                 headers=headers,
                                 timeout=10)
        total_log_in_method(response)

        user_id = response.json().get('id')
        if response.status_code == 200:
            write_value_in_json(settings.USERS_TEMPLATE_PATH,settings.USERS_PATH, user_id,'userId')
            return response
        else:
            logging.info(f'User {user_id} is existing.')
            return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def find_user_by_login(login: str) -> int:
        url = f'{settings.BASE_URL}/api/users/lookup?loginOrEmail={login}'
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url,
                                auth=settings.BASIC_AUTH,
                                headers=headers,
                                timeout = 10)
        total_log_in_method(response)

        user_id = response.json().get('id')
        return user_id

    @staticmethod
    @api_error_handler
    @retry(3)
    def delete_api_user(userid=None):
        if userid is None:
            userid = read_value_in_json(settings.USERS_PATH, 'userId')

        url = f'{settings.BASE_URL}/api/admin/users/{userid}'
        response = requests.delete(url,
                                   auth=settings.BASIC_AUTH,
                                   timeout = 10)
        total_log_in_method(response)

        if response.status_code == 404:
            print(f'User {userid} already deleted. Skipping deletion')
            return

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def create_bad_request():
        url = f'{settings.BASE_URL}/api/admin/users'
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url,
                                 auth=settings.BASIC_AUTH,
                                 headers=headers,
                                 timeout = 10)
        total_log_in_method(response)

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def change_user_password():
        userid = read_value_in_json(settings.USERS_PATH, 'userId')

        url = f'{settings.BASE_URL}/api/admin/users/{userid}/password'
        headers = {'Content-Type': 'application/json'}

        response = requests.put(url,
                                 auth=settings.BASIC_AUTH,
                                 json = change_password,
                                 headers=headers,
                                 timeout = 10)
        total_log_in_method(response)

        return response



