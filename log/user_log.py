import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# バイナリオブジェクト
# consle = logging.StreamHandler()
# logger.addHandler(consle)

#logをファイルに出力
file_handle = logging.FileHandler(r"D:\program\automation_test\automation\log\logs\test.log")
# log出力のフォーマット
formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s --->%(message)s')
# フォーマット使用
file_handle.setFormatter(formatter)
logger.addHandler(file_handle)

# terminalで出力
logger.debug("teste1234")
# 終了後閉じる
file_handle.close()
logger.removeHandler(file_handle)