from selenium.webdriver.common.by import By
from base import base_init
class HomePage(base_init.Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_sign_up(self):
       self.wait_until_click(By.XPATH, "//a[normalize-space()='Signup / Login']").click()

    def click_product(self):
        self.wait_until_click(By.XPATH,"//a[@href='/products']").click()

