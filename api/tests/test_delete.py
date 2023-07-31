import pytest
from utils.checks import check_delete_requests
from fixtures import test_data, get_api


@pytest.mark.usefixtures('test_data', 'get_api')
def test_delete(test_data, get_api):
    """
    :param test_data: yaml file for test with configs
    :param get_api: get url
    """
    response = check_delete_requests(test_data, get_api)
    assert test_data['response'] == response.text, f"Response is wrong. Expected: {test_data['response']}," \
                                                   f"but got {response.text}"
