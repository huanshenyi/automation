# pip install Pillow
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import pytesseract
import time


class GetCode:
    def __init__(self, driver):
        self.driver = driver


    # 画像を取得
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
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
        time.sleep(2)

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
        time.sleep(2)
        return text

    # 画像の解析ダメな方法
    def code_local(self, file_name):
        image = Image.open(self, file_name)
        tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
        text = pytesseract.image_to_string(image, config=tessdata_dir_config)
        time.sleep(2)
        return text
