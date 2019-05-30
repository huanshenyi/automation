from business.register_business import RegisterBusiness
from selenium import webdriver
import os
import unittest
import HTMLTestRunner
import time
import sys
import platform


if platform.platform().startswith("Windows"):
    driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\driver\chromedriver.exe"
    code_img_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\img\test001.png"
else:
    driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/driver/chromedriver"


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.log = UserLog()
        # cls.logger = cls.log.get_log()
        cls.file_name = code_img_path


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
        self.driver.quit()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34hbu@aa.com', '111', '111', 'tets')
        self.assertFalse(email_error, 'case実行')
        # if email_error is True:
        # print("ログイン成功,case失敗")
        # assertでエラーかどうかの判断をする

    def test_login_username_error(self):
        username_error = self.login.login_name_error('111@qq.com', 'ss', '111111', self.file_name)
        self.assertFalse(username_error)
        # if username_error is True:
        #     print("新規成功,case失敗")

    def test_login_code_error(self):
        code_error = self.login.login_name_error('111@qq.com', 'ss22', '111111', 'xxxx')
        self.assertFalse(code_error)
        # if code_error is True:
        #     print("新規成功,case失敗")

    def test_login_password_error(self):
        password_error = self.login.login_name_error('111@qq.com', 'ss22', '111111', self.file_name)
        self.assertFalse(password_error)
        # if password_error is True:
        #     print("新規成功,case失敗")

    def test_login_success(self):
        success = self.login.user_base('111@qq.com', 'sss22', '111111', self.file_name)
        self.assertFalse(success)
        # if self.login.register_success() is True:
        #     print("新規成功")

# def main():
#     first = FirstCase()
#     first.test_login_code_error()
#     first.test_login_email_error()
#     first.test_login_password_error()
#     first.test_login_username_error()
#     first.test_login_success()

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    # unittest.TextTestRunner().run(suite)
    # unittest.main()
    file_path = os.path.abspath(os.path.join(os.getcwd(), ".."))+r"\report\first_case.html"
    file = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="This is first report",
                                  description="最初レポート", verbosity=2)
    runner.run(suite)
