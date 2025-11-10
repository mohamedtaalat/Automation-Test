import logging
import inspect
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

    def log(self, log_level=logging.INFO):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        if not logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler = logging.FileHandler('log.log', mode='w')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger