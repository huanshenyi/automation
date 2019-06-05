from page.register_page import RegisterPage
from util.get_code import GetCode

class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # メールアドレス入力
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    # ユーザーname入力
    def send_user_name(self, username):
        self.register_p.get_username_element().send_keys(username)

    # パスワード入力
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # キャップチャー入れ
    def send_user_code(self, file_name):
        # キャップチァーcode取得用
        # get_code_text = GetCode(self.driver)

        # code = get_code_text.code_online(file_name)
        # code = get_code_text.code_local(file_name)
        self.register_p.get_code_element().send_keys(file_name)

    # 文字データを取得
    def get_user_text(self, info, user_info):
        try:
            if info == "user_email_error":
                text = self.register_p.get_email_error_element().text
            elif info == "user_name_error":
                text = self.register_p.get_name_error_element().text
            elif info == "password_error":
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_error_element().text
        except:
          text = None
        return text
    # 新規登録ボタン
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 新規ボタンを取得
    def get_register_text(self):
        return self.register_p.get_button_element().text