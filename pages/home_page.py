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
        self.wait_until_click(By.XPATH,"//a[@href='/cart']").click()

    def click_contact_us(self):
        self.wait_until_click(By.XPATH,"//a[normalize-space()='Contact us']").click()

    def click_add_to_cart(self):
        ActionChains(self.driver).move_to_element(self.wait_until_elements_visible(By.XPATH,"//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]")).perform()
        self.wait_until_click(By.XPATH,"//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]").click()