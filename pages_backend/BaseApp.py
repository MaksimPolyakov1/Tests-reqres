from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://reqres.in/"

    def find_element(self, locator: tuple, time=10):
        """
        :param locator: tuple with type of searching (xpath f.e.) and locator
        :param time: wait time until element found
        :return: found element
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        """
        :return: get request to base url
        """
        return self.driver.get(self.base_url)

    def get_current_url(self):
        """
        :return: current url of page
        """
        return self.driver.current_url

    def click_on_button(self, locator: tuple):
        """
        :param locator: tuple with type of searching (xpath f.e.) and locator
        :return: click on clickable element
        """
        return self.find_element(locator).click()

    def copy_text(self, locator: tuple):
        """
        :param locator: tuple with type of searching (xpath f.e.) and locator
        :return: copy text from element
        """
        return self.find_element(locator).text
