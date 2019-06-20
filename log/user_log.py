import logging
import os
from datetime import datetime


class UserLog(object):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # バイナリオブジェクト
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)

        # logファイル名
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.now().strftime("%Y-%m-%d")+".log"
        # log_name = log_dir+"\\"+log_file
        log_name = r"log\logs"+log_file
        print(log_name)

        #logをファイルに出力
        self.file_handle = logging.FileHandler(log_name, "a", encoding="utf-8")
        # log出力のフォーマット
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s --->%(message)s')
        # フォーマット使用
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


    def get_log(self):
        return self.logger
        # 終了後閉じる

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
     user = UserLog()
     log = user.get_log()
     log.debug('test')
     user.close_handle()