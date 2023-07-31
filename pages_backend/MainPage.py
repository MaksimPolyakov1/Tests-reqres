from BaseApp import Base
from selenium.webdriver.common.by import By


class MainPageLocators(Base):
    def get_endpoint_locator(self, data_id: str):
        """

        :param data_id: string with data_id
        :return: found element
        """
        locator_endpoint = (By.XPATH, f'//li[@data-id="{data_id}"]')
        return self.find_element(locator_endpoint)

    LOCATOR_BUTTON_REQUEST = (By.XPATH, '//span[@data-key="url"]')
    LOCATOR_REQUEST_TEXT = (By.XPATH, '//pre[@style="word-wrap: break-word; white-space: pre-wrap;"]')
    LOCATOR_RESPONSE_CODE = (By.XPATH, '//span[@data-key="response-code"]')
    LOCATOR_OUTPUT_RESPONSE = (By.XPATH, '//pre[@data-key="output-response"]')
