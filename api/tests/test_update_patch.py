import pytest
import json
from utils.checks import check_patch_requests
from fixtures import test_data, get_api


@pytest.mark.usefixtures('test_data', 'get_api')
def test_update_patch(test_data, get_api):
    """
    :param test_data: yaml file for test with configs
    :param get_api: get url
    """
    response = check_patch_requests(test_data, get_api)
    for key, value in test_data['body'].items():
        assert value == json.loads(response.text)[key]
