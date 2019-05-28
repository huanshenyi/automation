from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from util.ShowapiRequest import ShowapiRequest
import time


driver_path = os.path.abspath(os.getcwd())+"\chromedriver.exe"
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('--headless')
# CHROME_OPTIONS.add_argument("--no-sandbox")
# CHROME_OPTIONS.add_argument("--single-process")
driver = webdriver.Chrome(executable_path=driver_path, options=CHROME_OPTIONS)
driver.get('http://www.5itest.cn/register?goto=/')


email_element = driver.find_element_by_id("register_email")
# get_attribute要素の内容を取得
# print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
# 入力内容を取得
# print(email_element.get_attribute("value"))


# randomメールアドレス
# for i in range(5):
#     user_email = ''.join(random.sample("1234567890abcdefg",5))+"@163.com"
#     print(user_email)

# キャプチャー取得
driver.save_screenshot("imooc.png")
code_element = driver.find_element_by_id("getcode_num")
# 要素の座標が取得できる{'x': 440, 'y': 523}
print(code_element.location)
left = code_element.location["x"]
top = code_element.location["y"]
# 画像の幅と高さを取得
right = code_element.size['width']+left
height = code_element.size["height"]+top

# 画像を修理
# pip install Pillow
from PIL import Image

im = Image.open("imooc.png")
img = im.crop((left, top, right, height))
img.save("imooc1.png")

# (外部api使用した)画像の文字認識
r = ShowapiRequest("http://route.showapi.com/184-5","my_appId","my_appSecret" )
r.addBodyPara("img_base64", "")
# typeid=画像内に数字の数
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", "imooc1.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']["Result"]
print(text) # 返回信息

# 認識した数字を入力
time.sleep(3)
driver.find_element_by_id("captcha_code").send_keys(text)

driver.close()
