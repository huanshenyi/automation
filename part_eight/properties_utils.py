# log 解析のファイル

class Properties():
    def __init__(self, file_name):
        self.properties_file_name = file_name
        self.properties = {}

    def get_properties(self) -> dict:
        with open(self.properties_file_name, 'r', encoding='ISO-8859-1') as pro_file:
             for line in pro_file.readlines():
                 # データを綺麗に
                 line = line.strip().replace("\n", "")
                 # もし#あれば、その後はコメント
                 if line.find("#") != -1:
                     line = line.split("#")[0]
                 if line.find("=") > 0:
                    strs = line.split("=")
                    # dictを定義取得
                    self.__get_dict(strs[0].strip(), self.properties, strs[1].strip())
        return self.properties

    def __get_dict(self, key_name, result_dict, value):
        # keyの中に.入ってるかどうか判断,あればsplit,なければ値をset
        if key_name.find(".") > 0:
            # 再帰関数
            k = key_name.split(".")[0] # 最初のwwwをkeyにする
            result_dict.setdefault(k, {}) #結果のdictを{www.{xxx:{com:value}}}
            return self.__get_dict(key_name[len(k) + 1:], result_dict[k], value)
        else:
            result_dict[key_name] = value

