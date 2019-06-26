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
        """
        商品リストのdriver
        :param first_list_name:     一級メニュー名
        :param second_list_name:    二級メニュー名
        :return:
        """
        driver = self.open()
        first_element = (By.LINK_TEXT, first_list_name)
        second_element = (By.LINK_TEXT, second_list_name)
        first = self.find_element(*first_element)
        ActionChains(driver).move_to_element(first).perform()
        second = self.find_element(*second_element)
        second.click()

        # ハンドルの切り替え
        handles = driver.window_handles
        index_handle = driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                driver.close()
                driver.switch_to.window(handle)

        self.logger.info("ページ取得" + second_list_name)
        self.logger.info("現在urlは" + driver.current_url)

        self._driver = driver
        return driver

    def get_select_page(self, selector_condition_list):
        """
        複数の選択条件を選択
        :param selector_condition_list: 選択条件のリスト 例:[(By.ID,"id_value"),(By.name,"name_value")]
        リスト使用するのは順位変化しないためである
        :return:
        """

        # リストであるかどうかの判断しても良い

        for condition in selector_condition_list:
            element = self.find_element(*condition)
            element.click()

    def get_goods_info_page(self, selector_condition):
        """
        商品の詳細を取得
        :param selector_condition: 具体的な商品の選択条件
        例:(By.ID,"id_value")
        :return:driver
        """
        self.find_element(*selector_condition).click()
        # ハンドルの切り替え
        handles = self._driver.window_handles
        index_handle = self._driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                self._driver.close()
                self._driver.switch_to.window(handle)
        self.logger.info("詳細ページを取得")
        self.logger.info("現在urlを取得"+self._driver.current_url)
        return self._driver


