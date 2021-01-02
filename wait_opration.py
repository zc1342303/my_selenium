import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WaitOperation:
    def __init__(self, driver):
        self.driver = driver

    def by_class(self, name, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, name))
            )
            return elem
        except Exception as e:
            print(e)
            self.by_class(name, timeout)

    def by_xpath(self, name, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, name))
            )
            return elem
        except Exception as e:
            print(e)
            self.by_xpath(name, timeout)

