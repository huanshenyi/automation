# pageのelementの最も長い待ち時間
UI_WAIT_TIME = 2
# ローカルdriverのpath
# driverによってpathを増やす
EXECUTABLE_PATH = r"D:\program\automation_test\automation\driver\chromedriver.exe"

# リモートdriverのpath
REMOTE_DRIVER_DICT = {
    'dicker_1': "http://192.168.1.35:4444/wd/hub",
    'docker_2': "http://192.168.1.38:4444/wd/hub"
}

# スタートurl
START_URL = "url"