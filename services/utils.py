import json
import logging
import inspect
import os
import shutil

from pydantic import ValidationError

from data.dashboards_data import get_body_for_create_dashboard


def write_value_in_json(template_path,file_path, saved_value, json_value):
    if not os.path.exists(file_path):
        logging.warning(f"⚠️ {file_path} not found, creating from template")
        shutil.copy(template_path, file_path)

    with open(file_path, 'r') as file:
        json_file = json.load(file)

    json_file[json_value] = saved_value

    with open(file_path, 'w') as file:
        json.dump(json_file,file,indent=2)
    logging.info(f'Function: {inspect.currentframe().f_code.co_name}, {json_value}: {saved_value}')

def read_value_in_json(file_path, json_value):
    with open(file_path, 'r') as file:
        json_file = json.load(file)

    saved_value = json_file[json_value]
    if saved_value is None:
        logging.warning(f'Key {json_value} not found in {file_path}')
        raise ValueError

    logging.info(f'Function: {inspect.currentframe().f_code.co_name}, {json_value}: {saved_value}')

    return saved_value

def assert_status_message(response, expected_status, expected_message):
    assert response.status_code == expected_status, f'Expected {expected_status}, got {response.status_code}'
    assert response.json().get('message') == expected_message

def validate_status_code_and_body(response, schema, status_code, path: list[str] = None):
    data = response.json()

    if path:
        for key in path:
            data = data[key]
    try:
        validated = schema.model_validate(data)
    except ValidationError as e:
        logging.error(f'Error in validation Schema: {e}')
        raise AssertionError (f'Response = {data}, but expected = {schema.model_dump()}')

    assert response.status_code == status_code, f'Expected status code {status_code}, got {response.status_code} - {response.json().get("message", "")}'
    for field, value in validated.model_dump().items():
        assert data.get(field) == value, f'Value in "{field}" is unexpected. Expected: {value}, got receive: {data.get(field)}'

    logging.info (f'Function: {inspect.currentframe().f_code.co_name} is successfully validated, \n Response: {data}, \n validated: {validated}')

def extract_value_in_object(key):
    body = get_body_for_create_dashboard('get')
    key = body['dashboard'][key]
    return key

def total_log_in_method(response):
    logging.info(f"Method: {inspect.currentframe().f_code.co_name}: Status - {response.status_code}, response - {response.json()}, \n url - {response.url}")

def log_get_id(var_name, name_id):
    logging.info(f'Current value "{var_name}" is "{name_id}"')