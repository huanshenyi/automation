# coding=utf-8
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import os


ex_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\config\keyworld.xls"
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
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
                    # 入力データを取得
                    send_value = handle_excel.get_col_value(i, 5)
                    # 操作elementを取得
                    handle_value = handle_excel.get_col_value(i, 6)
                    # 予想結果を取得
                    except_result_method = handle_excel.get_col_value(i, 7)
                    # 予想結果の値
                    except_result = handle_excel.get_col_value(i, 8)
                    # except_result_method と except_resultは '' である可能性はある

                    #if send_value:
                    self.run_method(method, send_value, handle_value)
                    # もし予想結果の値が存在すれば
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        # もし予想結果のタイプはtext
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        # もし予想結果はelementであれば
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                           print("no-else")
                    else:
                        print('予想結果ありません')

    # 予想結果を取得
    def get_except_result_value(self, data):
        return data.split('=')

    # method処理
    def run_method(self, method, send_value='', hand_value=''):
        # ActionMethod中のmethodを取得
        method_value = getattr(self.action_method, method)
        if send_value == '' and hand_value != '':
            result = method_value(hand_value)
        elif send_value is '' and hand_value is '':
            result = method_value()
        elif send_value != '' and hand_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, hand_value)
        return result

if __name__ == "__main__":
    keyworldcase = KeywordCase()
    keyworldcase.run_main()