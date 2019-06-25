from part_nine.pages.goods_info_page import GoodsInfoPage
from part_nine.utils.browser_engine import BrowserEngine
from part_nine.config import logging_setting
from part_nine.pages.goods_list_page import GoodsListPage

from selenium.webdriver.common.by import By

class Test(object):
    driver = BrowserEngine.init_local_driver()
    logger = logging_setting.get_logger()
