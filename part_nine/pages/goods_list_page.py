from part_nine.pages.base_page import BasePage
from part_nine.config.logging_setting import get_logger
from part_nine.config import basic_config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GoodsListPage(BasePage):
    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super(GoodsListPage, self).__init__(driver, basic_config.START_URL)

    def get_goods_list_driver(self, first_list_name, second_list_name):
        driver = self.open()
        first_element = (By.LINK_TEXT, first_list_name)
        second_element = (By.LINK_TEXT, second_list_name)
        first = self.find_element(*first_element)
