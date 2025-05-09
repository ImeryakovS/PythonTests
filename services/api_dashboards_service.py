import requests
import config.settings as settings
import data.dashboards_data as data
import logging

from helpers.decorators import api_error_handler, retry
from services.utils import write_value_in_json, read_value_in_json, extract_value_in_object,total_log_in_method, log_get_id


class ApiDashboardsService:

    @staticmethod
    @api_error_handler
    @retry(3)
    def create_folder():
        url = f'{settings.BASE_URL}/api/folders'
        headers = {'Content-Type': 'application/json'}
        body = data.body_for_create_folder
        response = requests.post(url,
                                 auth=settings.BASIC_AUTH,
                                 json = body,
                                 headers=headers,
                                 timeout = 10)
        total_log_in_method(response)

        folder_uid = response.json().get('uid')
        write_value_in_json(settings.DASHBOARDS_TEMPLATE_PATH,settings.DASHBOARDS_PATH, folder_uid, 'folderUid')

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def create_dashboard():
        url = f'{settings.BASE_URL}/api/dashboards/db'
        headers = {'Content-Type': 'application/json'}

        folder_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'folderUid')

        body = data.get_body_for_create_dashboard(folder_uid)
        response = requests.post(url,
                                 auth = settings.BASIC_AUTH,
                                 json = body,
                                 headers=headers,
                                 timeout = 10)
        total_log_in_method(response)

        dashboard_uid = response.json().get('uid')
        write_value_in_json(settings.DASHBOARDS_TEMPLATE_PATH,settings.DASHBOARDS_PATH, dashboard_uid, 'dashboardUid')

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def get_dashboard():
        dashboard_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'dashboardUid')
        url = f'{settings.BASE_URL}/api/dashboards/uid/{dashboard_uid}'
        headers = {'Content-Type': 'application/json'}
        log_get_id('dashboard_uid',dashboard_uid)

        title = extract_value_in_object('title')

        response = requests.get(url,
                                auth=settings.BASIC_AUTH,
                                headers=headers,
                                timeout = 10)
        total_log_in_method(response)

        return response, title

    @staticmethod
    @api_error_handler
    @retry(3)
    def get_dashboard_with_incorrect_auth():
        dashboard_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'dashboardUid')
        url = f'{settings.BASE_URL}/api/dashboards/uid/{dashboard_uid}'
        headers = {'Content-Type': 'application/json'}
        log_get_id('dashboard_uid',dashboard_uid)

        response = requests.get(url,
                                auth=('admin2','admin2'),
                                headers=headers,
                                timeout = 10)
        total_log_in_method(response)

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def get_dashboard_with_low_level_access():
        dashboard_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'dashboardUid')

        url = f'{settings.BASE_URL}/api/dashboards/uid/{dashboard_uid}'
        headers = {'Content-Type': 'application/json'}
        log_get_id('dashboard_uid',dashboard_uid)

        response = requests.get(url,
                                auth=settings.LOW_ACCESS,
                                headers=headers,
                                timeout = 10)
        total_log_in_method(response)

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def get_404_dashboard():
        dashboard_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'dashboardUid')
        dashboard_uid += '12'
        url = f'{settings.BASE_URL}/api/dashboards/uid/{dashboard_uid}'
        headers = {'Content-Type': 'application/json'}
        log_get_id('dashboard_uid',dashboard_uid)

        response = requests.get(url,
                                auth=settings.BASIC_AUTH,
                                headers=headers,
                                timeout = 10)
        total_log_in_method(response)

        return response

    @staticmethod
    @api_error_handler
    @retry(3)
    def delete_dashboard():
        dashboard_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'dashboardUid')

        url = f'{settings.BASE_URL}/api/dashboards/uid/{dashboard_uid}'

        headers = {'Content-Type': 'application/json'}
        title = extract_value_in_object('title')
        log_get_id('title',title)

        response = requests.delete(url,
                                   auth = settings.BASIC_AUTH,
                                   headers = headers,
                                   timeout = 10)
        total_log_in_method(response)

        if response.status_code == 404:
            logging.warning(f'User {dashboard_uid} already deleted. Skipping deletion')
            return response,title
        return response,title

    @staticmethod
    @api_error_handler
    @retry(3)
    def delete_folder_for_dashboard():
        folder_uid = read_value_in_json(settings.DASHBOARDS_PATH, 'folderUid')
        url = f'{settings.BASE_URL}/api/folders/{folder_uid}'

        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url,
                                   auth = settings.BASIC_AUTH,
                                   headers = headers,
                                   timeout = 10)
        total_log_in_method(response)

        if response.status_code == 404:
            logging.warning(f'User {folder_uid} already deleted. Skipping deletion')
            return  response
        return response