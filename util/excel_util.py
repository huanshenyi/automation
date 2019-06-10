# pip install xlrd
import xlrd
# pip install xlutils
from xlutils.copy import copy
import os
import time

ex_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\config\casedata.xls"

class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            self.excel_path = ex_path
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    # 一行一つのリストとして.一つのリストに納入
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # excelの行数を取得
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # excel,sellのデータを取得
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None


    # データ入力
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)

if __name__ == '__main__':
    ex = ExcelUtil(os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\config\casedata.xls")
    print(ex.get_data())