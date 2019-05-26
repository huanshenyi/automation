from business.register_business import RegisterBusiness
from selenium import webdriver
import os
import unittest
import HTMLTestRunner

driver_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\driver\chromedriver.exe"


class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', '111', '111', 'tets')
        self.assertFalse(email_error, 'case実行')
        # if email_error is True:
        # print("ログイン成功,case失敗")
        # assertでエラーかどうかの判断をする

    def test_login_username_error(self):
        username_error = self.login.login_name_error('111@qq.com', 'ss', '111111', 'test')
        self.assertFalse(username_error)
        # if username_error is True:
        #     print("新規成功,case失敗")

    def test_login_code_error(self):
        code_error = self.login.login_name_error('111@qq.com', 'ss22', '111111', 'tst')
        self.assertFalse(code_error)
        # if code_error is True:
        #     print("新規成功,case失敗")

    def test_login_password_error(self):
        password_error = self.login.login_name_error('111@qq.com', 'ss22', '111111', 'tst')
        self.assertFalse(password_error)
        # if password_error is True:
        #     print("新規成功,case失敗")

    def test_login_success(self):
        success = self.login.user_base('111@qq.com', 'sss22', '111111', 'tst')
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
    unittest.main()