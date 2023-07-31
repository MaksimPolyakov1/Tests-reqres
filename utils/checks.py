import time

import requests
from MainPage import MainPageLocators


def check_get_requests(test_data: dict, get_api: str):
    """
    :param test_data: dict with data from yaml file of test config
    :param get_api: string with target url
    :return: response with get request
    """
    request = requests.get(get_api)
    assert test_data['status_code'] == request.status_code, 'Status code is wrong'
    return request


def check_post_requests(test_data: dict, get_api: str):
    """
    :param test_data: dict with data from yaml file of test config
    :param get_api: string with target url
    :return: response with post request
    """
    request = requests.post(get_api, json=test_data['body'])
    assert test_data[
               'status_code'] == request.status_code, f'Status code is wrong, expected {test_data["status_code"]},' \
                                                      f' but got {request.status_code}'
    return request


def check_put_requests(test_data: dict, get_api: str):
    """
    :param test_data: dict with data from yaml file of test config
    :param get_api: string with target url
    :return: response with put request
    """
    request = requests.put(get_api, json=test_data['body'])
    assert test_data[
               'status_code'] == request.status_code, f'Status code is wrong, expected {test_data["status_code"]},' \
                                                      f' but got {request.status_code}'
    return request


def check_patch_requests(test_data: dict, get_api: str):
    """
    :param test_data: dict with data from yaml file of test config
    :param get_api: string with target url
    :return: response with patch request
    """
    request = requests.patch(get_api, json=test_data['body'])
    assert test_data[
               'status_code'] == request.status_code, f'Status code is wrong, expected {test_data["status_code"]},' \
                                                      f' but got {request.status_code}'
    return request


def check_delete_requests(test_data: dict, get_api: str):
    """
    :param test_data: dict with data from yaml file of test config
    :param get_api: string with target url
    :return: response with delete request
    """
    request = requests.delete(get_api)
    assert test_data[
               'status_code'] == request.status_code, f'Status code is wrong, expected {test_data["status_code"]},' \
                                                      f' but got {request.status_code}'
    return request


def get_endpoint_response(browser, test_data: dict, delayed=None):
    """
    Get text from response from main page
    :param browser: selenium chrome driver
    :param test_data: dict with data from yaml file of test config
    :param delayed: optional param if you need delayed after clicking on ep
    :return: dict with status code and output response
    """
    response = {}
    main_page = MainPageLocators(browser)
    main_page.go_to_site()
    main_page.get_endpoint_locator(test_data['data_id']).click()
    if delayed:
        time.sleep(delayed)
    response.update({'status_code': int(main_page.copy_text(main_page.LOCATOR_RESPONSE_CODE)),
                     'text': main_page.copy_text(main_page.LOCATOR_OUTPUT_RESPONSE)})
    return response


def get_response_from_request_button(browser):
    """
    Get text from response of request button, after pressing on it
    :param browser: selenium chrome driver
    :return: text from response of request button
    """
    main_page = MainPageLocators(browser)
    main_page.click_on_button(MainPageLocators.LOCATOR_BUTTON_REQUEST)
    return main_page.copy_text(MainPageLocators.LOCATOR_REQUEST_TEXT)
