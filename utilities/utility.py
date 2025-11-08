

class Utilities:

    def check_url(self,root,current):
        if current == root:
            return True
        else:
            return False

    def check_price_of_items(self,list_of_price):
       pass

    def take_screenshot(self,driver,path):
        driver.save_screenshot(path)