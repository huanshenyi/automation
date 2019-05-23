# 要素取得用
from base.find_element import FindElement

class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # メールアドレス要素取得
    def get_email_element(self):
        return self.fd.get_element("user_email")

    # ユーザーネームの要素取得
    def get_username_element(self):
        return self.fd.get_element("user_name")

    # パスワード要素取得
    def get_password_element(self):
        return self.fd.get_element("password")

    # キャップチャーcode要素取得
    def get_code_element(self):
        return self.fd.get_element("code_text")

    # ボタン
    def get_button_element(self):
        return self.fd.get_element("register_button")

    # emailエラー要素取得
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

    # nameエラー要素取得
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

    # passwordエラー要素取得
    def get_password_error_element(self):
        return self.fd.get_element("password_error")

    # キャップチャーエラー
    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")