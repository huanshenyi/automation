from selenium import webdriver
import time
import os
import random
# pip install Pillow
from PIL import Image
from ShowapiRequest import ShowapiRequest
import pytesseract
import platform


if platform.platform().startswith("Windows"):
    driver_path = os.path.abspath(os.getcwd()) + "\chromedriver.exe"
else:
    driver_path = os.path.abspath(os.getcwd()) + "/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)


# ブラウザを初期化
def driver_init():
    driver.get('http://www.5itest.cn/register')
    # windowを最大に
    driver.maximize_window()
    time.sleep(5)


# elementデータ取得
def get_element(id):
    element = driver.find_element_by_id(id)
    return element


# ランダム数を取得
def get_range_user():
    user_info = ''.join(random.sample("1234567890abcdefghijklmn", 8))
    return user_info

# 画像を取得
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
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
def code_online(file_name):
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
def code_local(file_name):
    image = Image.open(file_name)
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    text = pytesseract.image_to_string(image, config=tessdata_dir_config)
    print(text)
    return text

def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@gmail.com"
    file_name = os.path.abspath(os.getcwd())+"\\img\\test02.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_local(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()

run_main()