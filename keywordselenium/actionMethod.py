from selenium import webdriver
import os
from base.find_element import FindElement
import time

class ActionMethod:
    def __init__(self):
        pass
    # ブラウザを開く
    def open_browser(self, browser):
        if browser == 'chrome':
            driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\driver\chromedriver.exe"
            self.driver = webdriver.Chrome(executable_path=driver_path)
        elif browser == 'firefox':
            driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\driver\geckodriver.exe"
            self.driver = webdriver.Firefox(executable_path=driver_path)

    # urlの入力
    def get_url(self, url):
        self.driver.get(url)

    # 要素を特定
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 要素の入力
    def element_send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 要素のクリック
    def click_element(self, key):
        self.get_element(key).click()

    # 待つ
    def sleep_time(self):
        time.sleep(3)

    # ブラウザを閉じる
    def close_browser(self, driver):
        self.driver.close()

    # Url_titleを取得
    def get_title(self):
        return self.driver.title





