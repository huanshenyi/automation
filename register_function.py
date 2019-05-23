import sys
sys.path.append(r"D:\program\automation_test")
# domの要素データ
from selenium import webdriver
import os
import platform
# 画像処理用のライブラリ
from PIL import Image
# 有料きゃっぷちゃ認識
from ShowapiRequest import ShowapiRequest
# 無料で精度悪い認識ライブラリ
import pytesseract
from base.find_element import FindElement
import random
import time


if platform.platform().startswith("Windows"):
    driver_path = os.path.abspath(os.getcwd()) + r"\driver\chromedriver.exe"
    driver_path2 = os.path.abspath(os.getcwd()) + r"\driver\geckodriver.exe"
    driver_path1 = os.path.abspath(os.getcwd()) + r"\driver\IEDriverServer.exe"
else:
    driver_path = os.path.abspath(os.getcwd()) + "/driver/chromedriver"


class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    # driverを取得,ブラウザ開く
    def get_driver(self, url, i):
        if i == 1:
           driver = webdriver.Chrome(executable_path=driver_path)
        else:
           driver = webdriver.Firefox(executable_path=driver_path2)
        # else:
        #    driver = webdriver.Ie(executable_path=driver_path1)
        # driver1 = webdriver.Edge()
        # driver2 = webdriver.Firefox(executable_path=driver_path2)
        driver.get(url)
        driver.maximize_window()
        return driver

    # ユーザー情報入れる
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # dom情報を取得,element取得
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element


    # ランダム数を取得
    def get_range_user(self):
        user_info = ''.join(random.sample("1234567890abcdefghijklmn", 8))
        return user_info

    # 画像を取得
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        # 要素の座標が取得できる{'x': 440, 'y': 523}
        left = code_element.location["x"]
        top = code_element.location["y"]
        # 画像の幅と高さを取得
        right = code_element.size['width'] + left
        height = code_element.size["height"] + top
        # 画像を修理
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 画像の解析
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-5", "my_appId", "my_appSecret")
        r.addBodyPara("img_base64", "")
        # typeid=画像内に数字の数
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']["Result"]
        return text

    # 画像の解析ダメな方法
    def code_local(self, file_name):
        self.get_code_image(file_name)
        image = Image.open(file_name)
        tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
        text = pytesseract.image_to_string(image, config=tessdata_dir_config)
        print(text)
        return text



    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@gmail.com"
        if platform.platform().startswith("Windows"):
            file_name = os.path.abspath(os.getcwd()) + "\\img\\test02.png"
        else:
            file_name = os.path.abspath(os.getcwd()) + "/img/test02.png"
        # code_text = self.code_local(file_name)
        self.send_user_info("user_email", user_email)
        self.send_user_info("user_name", user_name_info)
        self.send_user_info("password", "111111")
        self.send_user_info("code_text", 111)
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("新規登録成功")
        else:
            if platform.platform().startswith("Windows"):
                self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\img\codeerror.png")
            else:
                self.driver.save_screenshot(os.path.abspath(os.getcwd())+"/img/codeerror.png")
            self.driver.save_screenshot("codeerror.png")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(2):
        tt = RegisterFunction("http://www.5itest.cn/register", i)
        tt.main()


