# pip install Configparser
import configparser
import os
import platform


class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            if platform.platform().startswith("Windows"):
              file_name = os.path.abspath(os.path.join(os.getcwd(), '..'))+r"\config\LocalElement.ini"
              # file_name = "config\LocalElement.ini"
            else:
               file_name = os.path.abspath(os.path.join(os.getcwd(), '..')) + r"/config/LocalElement.ini"
               # file_name = "/Users/tianxiaoyi/spider/automation/config/LocalElement.ini"

        if node == None:
           self.node = "RegisterElement"
        else:
           self.node = node
        self.cf = self.load_ini(file_name)

    # configの読み込み
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # dom要素取得
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data

# if __name__ == '__main__':
#     read_int = ReadIni()
#     print(read_int.get_value("user_name"))