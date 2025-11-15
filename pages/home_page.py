from selenium.webdriver import ActionChains
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

    def click_cart(self):
        self.wait_until_click(By.XPATH,"/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()

    def click_contact_us(self):
        self.wait_until_click(By.XPATH,"//a[normalize-space()='Contact us']").click()
