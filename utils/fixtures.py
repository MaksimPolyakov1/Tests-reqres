import yaml
import pytest
from selenium import webdriver


@pytest.fixture
def test_data(request):
    """
    :param request: requests by pytest
    :return: dict with data from yaml file of test config
    """
    path = request.fspath.strpath.replace('tests', 'config').replace('.py', '.yaml')
    with open(path) as file:
        test_data = yaml.load(file, Loader=yaml.FullLoader)
        return test_data


@pytest.fixture
def get_api(test_data: dict):
    """
    :param test_data: data from yaml file of test config
    :return: string with target url
    """
    url = 'https://reqres.in/api/' + test_data['req']
    return url


@pytest.fixture(scope="session")
def browser():
    """
    :return: selenium chrome driver
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

