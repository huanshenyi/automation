from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from part_nine.config import basic_config

class BasePage(object):
    def __init__(self, driver, url):
        """
        BasePageの構造関数
        :param driver: どのブラウザを開く
        :param url: ターゲットurl
        """
        self._driver = driver
        self._url = url

    def open(self):
        """
        page_open関数
        :return: ブラウザのdriver
        """
        self._driver.get(url=self._url)
        return self._driver

    # 単独の要素を特定
    def find_element(self, *locator,
                     element=None,
                     timeout=None,
                     wait_type="visibility",
                     when_failed_close_browser=True):
        """
        elementをfind関数,driver,あるいはelementを上乗せしてelementを発見可能

        :param locator: elementの特定関数,データタイプはtuple,例:(By.ID,'id_value')
        :param element: default はNone,もし値があれば,値はpageのelement要素,関数はこのelementの上に
        :param timeout: default はNone,もしNoneの時,configのtimeoutのパラメータを取得
        :param wait_type: 待ちのタイプ,二種類の待ち方適応,1,visibility(見えるまでの待ち),2,presence(存在までの待ち)
        :param when_failed_close_browser:element特定失敗したら、ブラウザ閉じるか,
        :return: elementを返す
        """
        if element is not None:
            # elementを基づいて動作するvisibility_of
            return self._init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))
        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_element_located(*locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(*locator))
        except TimeoutException:
            if when_failed_close_browser:
               self._driver.quit()
            raise TimeoutException(msg="element見つからない,使用方法は:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="element見つからない,使用方法は:{}".format(locator))


    # 複数の要素を特定
    def find_elements(self,
                      *locator,
                      element=None,
                      timeout=None,
                      wait_type="visibility",
                      when_failed_close_browser=True):
        """
        複数のelementを特定 関数
        :param locator: elementの特定方式と値,tupleタイプ,例(By.ID,"id_value")
        :param element: default はNone,もし値があれば,値はpageのelement要素,関数はこのelementの上に
        :param timeout:
        :param wait_type:
        :param when_failed_close_browser:
        :return:特定された要素を返す
        """

        if element is not None:
            return element.find_elements(*locator)
        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="element見つからない,使用方法は:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="element見つからない,使用方法は:{}".format(locator))


    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=basic_config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
