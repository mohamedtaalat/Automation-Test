from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    def __init__(self,driver):
        self.wait = WebDriverWait(driver, 10)

    def wait_until_click(self,type,locator):
        return self.wait.until(EC.element_to_be_clickable((type,locator)))

    def wait_until_visible(self,type,locator):
        return self.wait.until(EC.visibility_of_element_located((type,locator)))

    def wait_until_elements_visible(self,type,locator):
        return self.wait.until(EC.visibility_of_all_elements_located((type,locator)))

