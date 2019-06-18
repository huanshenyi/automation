import logging
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# バイナリオブジェクト
# consle = logging.StreamHandler()
# logger.addHandler(consle)

# logファイル名
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, "logs")
log_file = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".log"
log_name = log_dir+"\\"+log_file

#logをファイルに出力
file_handle = logging.FileHandler(log_name, "a", encoding="utf-8")
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