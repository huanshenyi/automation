import logging

# ディフォルトのlogレベルはwaring
# 詳細はソースコードを確認する
# logging.basicConfig(level="DEBUG")
#
# # 調整用log,logメッセージ最も詳しいのレベル,プログラム調整用
# logging.debug("this is debug logging")
#
# # daily record,debugより出力結果が少ない,普通release環境で使用することが多い
# logging.info("info logging")
#
# # 警告メッセージ,でもプログラム影響ない
# logging.warning("warning logging")
#
# # エラー,プログラム停止
# logging.error("error logging")

# logging.Formatter()
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
# logging.basicConfig(filename="my-first.log",
#                     level=10,
#                     format=LOG_FORMAT,
#                     datefmt=DATE_FORMAT)
#
# logging.debug("debugのlogです")

import sys

file_path = "my-second.log"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# ファイルのlogの配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh = logging.FileHandler(file_path, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# consoleのlog配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("ログインフォメーションです")