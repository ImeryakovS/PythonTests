import inspect

import requests
import config.settings as settings
import logging

from data.organizations_data import test_organizations_body, add_in_organizations_body
from data.users_credentials import organizations_user
from helpers.decorators import api_error_handler, retry
from services.api_users_service import ApiUsersService
from services.utils import write_value_in_json, read_value_in_json, extract_value_in_object


class ApiOrganizationsService:

    @staticmethod
    @api_error_handler
    @retry(3)
    def create_new_organization():
        url = f'{settings.BASE_URL}/api/orgs'
        headers = {'Content-Type': 'application/json'}
        body = test_organizations_body
        response = requests.post(url,
                                 auth=settings.BASIC_AUTH,
                                 json = body,
                                 headers=headers,
                                 timeout = 10)

        org_id = response.json().get('orgId')
        write_value_in_json(settings.ORGANIZATIONS_TEMPLATE_PATH,settings.ORGANIZATIONS_PATH,org_id,'orgId')

        return response,org_id

    @staticmethod
    @api_error_handler
    @retry(3)
    def add_user_in_organization():
        org_id = read_value_in_json(settings.ORGANIZATIONS_PATH,'orgId')
        url = f'{settings.BASE_URL}/api/orgs/{org_id}/users'
        headers = {'Content-Type': 'application/json'}
        body = add_in_organizations_body
        response = requests.post(url,
                                 auth=settings.BASIC_AUTH,
                                 json = body,
                                 headers=headers,
                                 timeout = 10)
        user_id = response.json().get('userId')
        return response, user_id

    @staticmethod
    @api_error_handler
    @retry(3)
    def delete_user_from_org(orgid=1, userid=None):
        if userid is None:
            userid = read_value_in_json(settings.USERS_PATH, 'userId')

        url = f'{settings.BASE_URL}/api/orgs/{orgid}/users/{userid}'

        response = requests.delete(url,
                                   auth=settings.BASIC_AUTH,
                                   timeout = 10)
        logging.info(f"Method: {inspect.currentframe().f_code.co_name}: Status - {response.status_code}, Body - {response.text}")

        if response.status_code == 404:
            print(f'User {userid} already deleted from org. Skipping deletion')
            return

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def get_organizations_by_id():
        org_id = read_value_in_json(settings.ORGANIZATIONS_PATH, 'orgId')
        name_org = test_organizations_body['name']
        url = f'{settings.BASE_URL}/api/orgs/{org_id}'

        response = requests.get(url,
                                   auth=settings.BASIC_AUTH,
                                   timeout = 10)
        logging.info(f"Method: {inspect.currentframe().f_code.co_name}: Status - {response.status_code}, Body - {response.text}")

        return response, org_id, name_org

    @staticmethod
    @api_error_handler
    @retry(3)
    def update_user_in_org():
        org_id = read_value_in_json(settings.ORGANIZATIONS_PATH, 'orgId')
        user_login = organizations_user['login']
        user_id = ApiUsersService.find_user_by_login(user_login)
        body = {"role": "Admin"}

        url = f'{settings.BASE_URL}/api/orgs/{org_id}/users/{user_id}'

        response = requests.patch(url,
                                auth=settings.BASIC_AUTH,
                                json=body,
                                timeout = 10)
        logging.info(f"Method: {inspect.currentframe().f_code.co_name}: Status - {response.status_code}, Body - {response.text}")

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def delete_organization():
        org_id = read_value_in_json(settings.ORGANIZATIONS_PATH, 'orgId')

        url = f'{settings.BASE_URL}/api/orgs/{org_id}'

        response = requests.delete(url,
                                   auth=settings.BASIC_AUTH,
                                   timeout = 10)
        logging.info(f"Method: {inspect.currentframe().f_code.co_name}: Status - {response.status_code}, Body - {response.text}")

        if response.status_code == 404:
            print(f'User {org_id} already deleted from org. Skipping deletion')
            return

        return response
