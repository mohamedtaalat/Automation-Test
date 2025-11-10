import time
from base import base_init
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class ProductPage(base_init.Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def search_item(self,item):
        home_page = HomePage(self.driver)
        home_page.click_product()
        self.write_in_search(item)
        self.click_search()

    def write_in_search(self,item):
        self.wait_until_visible(By.ID,"search_product").send_keys(item)

    def click_search(self):
        self.wait_until_click(By.ID,"submit_search").click()


    def check_every_item_in_category(self):
        home_page = HomePage(self.driver)
        home_page.click_product()
        self.driver.execute_script("window.scrollBy(0, 300);")
        self.click_on_women_in_category()
        self.click_on_men_in_category()
        self.click_on_kids_in_category()

    def click_on_women_in_category(self):
        self.wait_until_click(By.XPATH,"//a[normalize-space()='Women']").click()

    def click_on_men_in_category(self):
        self.wait_until_click(By.XPATH,"//a[normalize-space()='Men']").click()

    def click_on_kids_in_category(self):
        self.wait_until_click(By.XPATH,"//a[normalize-space()='Kids']").click()

    def check_price_of_items(self):
        home_page = HomePage(self.driver)
        self.driver.execute_script("window.scrollBy(0, 800);")
        home_page.click_product()
        print(self.get_price_of_items())
        return self.get_price_of_items()

    def get_price_of_items(self):
        elements=self.wait_until_elements_visible(By.TAG_NAME,"h2")
        return [el.text for el in elements]

    def check_specific_product(self):
        home_page = HomePage(self.driver)
        self.driver.execute_script("window.scrollBy(0, 800);")
        home_page.click_product()
        self.wait_until_click(By.LINK_TEXT,"View Product").click()
