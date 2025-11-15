from selenium.webdriver.common.by import By

from base.base_init import Base
from pages.home_page import HomePage
from pages.products_page import ProductPage


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_checkout(self):
        self.wait_until_click(By.XPATH,"//a[@class='btn btn-default check_out']")

    def get_quantity(self):
        return self.wait_until_visible(By.XPATH, "//button[@class='disabled']").text

    def get_price(self):
        return self.wait_until_visible(By.XPATH, "//p[@class='cart_total_price']").text

    def get_name_of_item(self):
        return self.wait_until_visible(By.XPATH, "//a[normalize-space()='Blue Top']").text

    def click_remove_from_cart(self):
        self.wait_until_click(By.XPATH,"//i[@class='fa fa-times']").click()

    def add_item_and_view_cart(self,item,button):
        pr = ProductPage(self.driver)
        pr.add_item_to_cart_then_view_cart(item,button)
    def add_item_then_remove(self,item,button):
        self.add_item_and_view_cart(item,button)
        self.click_remove_from_cart()

    def check_quantity(self):
        home=HomePage(self.driver)
        home.click_cart()
        return self.get_quantity()

    def check_name(self):
        home = HomePage(self.driver)
        home.click_cart()
        return self.get_name_of_item()

    def check_price(self):
        home = HomePage(self.driver)
        home.click_cart()
        return self.get_price()