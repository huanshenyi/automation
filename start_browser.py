from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import os
import random
from selenium.webdriver.chrome.options import Options



driver_path = os.path.abspath(os.getcwd())+"/chromedriver"
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--single-process")
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

#キャプチャー取得
driver.save_screenshot("imooc.png")
code_element = driver.find_element_by_id("getcode_num")
#要素の座標が取得できる{'x': 440, 'y': 523}
print(code_element.location)
left = code_element.location["x"]
top = code_element.location["y"]
#画像の幅と高さを取得
right = code_element.size['wigth']+left
height = code_element.zize["height"]+top

#画像を修理
from PIL import Image

im = Image.open("imooc.png")
img = im.crop((left, top, right, height))
img.save("imooc1.png")


driver.close()
