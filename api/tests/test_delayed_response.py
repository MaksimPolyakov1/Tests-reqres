import pytest
from utils.checks import check_get_requests
import time
import math
from fixtures import test_data, get_api


@pytest.mark.usefixtures('test_data', 'get_api')
def test_delayed_response(test_data, get_api):
    """
    :param test_data: yaml file for test with configs
    :param get_api: get url
    """
    start = time.perf_counter()
    check_get_requests(test_data, get_api)
    finish = time.perf_counter()
    assert math.floor(finish - start) == test_data['delayed_time'], f'Last for {math.floor(finish - start)},' \
                                                                    f'but expected {test_data["delayed_time"]}'
