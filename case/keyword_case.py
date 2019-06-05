# coding=utf-8
from util.excel_util import ExcelUtil
from keyword.actionMethod import ActionMethod
import os


ex_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\config\keyworld.xls"
class KeywordCase:
    def run_main(self):
        handle_excel = ExcelUtil(ex_path)
        # 行数を取得
        case_lines = handle_excel.get_lines()
        if case_lines:
            # 行数をループ、毎行のcaseを実行
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                # 実行するかどうか
                if is_run == 'yes':
                    # 実行方法を取得
                    method = handle_excel.get_col_value(i, 4)
                    # 実行方法を取得
                    send_value = handle_excel.get_col_value(i, 5)
                    # 操作値を取得
                    handle_value = handle_excel.get_col_value(i, 6)
                    #if send_value:
                    self.run_method(method, send_value, handle_value)





           # 入力データを取得
           # 入力データ存在するかどうか
             # 実行方法(入力データ,要素を操作)
           # 入力データない
             # 実行方法(要素を操作)
    def run_method(self,method, send_value, hand_value):
        action_method = ActionMethod()
        # ActionMethod中のmethodを取得
        method_value = getattr(action_method, method)
        if send_value:
            method_value(send_value, hand_value)
        else:
            method_value(hand_value)