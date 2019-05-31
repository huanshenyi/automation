import ddt
import unittest
import os
import platform
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import time
from util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()

if platform.platform().startswith("Windows"):
    driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\driver\chromedriver.exe"
    code_img_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\img\test001.png"
else:
    driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/driver/chromedriver"


# メール、ユーザーネーム、パスワード、キャップちゃ,エラーメッセージのエレメント要素,エラーメッセージ
@ddt.ddt
class FirstDbtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        # self.driver.save_screenshot()
        time.sleep(2)
        # sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                # caseの名前を取得
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\report\%s.png" % case_name
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # 'email', 'username', 'password', 'code', 'assertCode', 'assertText'
    # @ddt.data(
    #     ['123', 'huasdasd01', '1111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['123@qq.com', 'huasdasd01', '1111111', 'code', 'user_email_error-error', '请输入有效的电子邮件地址']
    # )
    @ddt.data(*data)

    @ddt.unpack
    # def test_register_case(self, email, username, password, code, assertCode, assertText):
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error, 'テスト失敗')


if __name__ == '__main__':
    file_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\report\first_case1.html"
    file = open(file_path, 'wb')
    # 沢山のcaseの挿入TestLoader
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDbtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="This is Ddt_first report",
                                           description="ddt最初レポート", verbosity=2)
    runner.run(suite)