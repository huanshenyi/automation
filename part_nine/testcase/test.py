from part_nine.pages.goods_info_page import GoodsInfoPage
from part_nine.utils.browser_engine import BrowserEngine
from part_nine.config import logging_setting
from part_nine.pages.goods_list_page import GoodsListPage

from selenium.webdriver.common.by import By

class Test(object):
    # driver = BrowserEngine.init_local_driver()
    logger = logging_setting.get_logger()

    def __init__(self):
        # 複数存在するリモートdriverを起動する
        driver_dict = BrowserEngine.init_remote_driver()
        # 複数一気に起動する場合、ここでまた処理が必要
        self.driver = driver_dict["docker_1"]



    def test_save_info(self):
        self.logger.debug("パソコン詳細保存")
        goods_list_page = GoodsListPage(self.driver)
        goods_list_page.get_goods_list_driver("电脑", "笔记本电脑")
        brand_locator = (By.ID, "brand-11518")
        price_locator = (By.LINK_TEXT, "7000以上")
        comment_locator = (By.LINK_TEXT, "评论数")
        goods_list_page.get_select_page([brand_locator, price_locator, comment_locator])

        self.logger.debug("詳細データー取得開始")
        goods = (By.XPATH, "//*[@id='plist']/ul/li[1]/div/div[1]/a/img")
        driver = goods_list_page.get_goods_info_page(goods)
        self.logger.info("現在のurlは:"+driver.current_url)
        goods_info = GoodsInfoPage(driver)
        goods_info.save_product_info()
        self.logger.info("商品データ保存しました")
