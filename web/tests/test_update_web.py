import pytest
from utils.checks import get_endpoint_response, check_put_requests, get_response_from_request_button
import json
from fixtures import browser, test_data, get_api


@pytest.mark.usefixtures('browser', 'test_data', 'get_api')
def test_update_web(browser, test_data, get_api):
    """
    :param browser: Selenium Chrome driver
    :param test_data: yaml file for test with configs
    :param get_api: get url
    """
    ep_response = get_endpoint_response(browser, test_data, delayed=1)
    assert test_data['status_code'] == ep_response['status_code'], f"Expected {test_data['status_code']}," \
                                                                   f"but got {ep_response['status_code']}"
    for key, value in test_data['body'].items():
        assert value == json.loads(ep_response['text'])[key]

    req_button = get_response_from_request_button(browser)
    api_response = check_put_requests(test_data, get_api)
    assert json.loads(req_button) == json.loads(api_response.text), f'Response from API: {json.loads(api_response.text)},' \
                                                                    f'but got {json.loads(req_button)}'