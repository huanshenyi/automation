from part_seven.field import Field
from part_seven.my_database import create_pool

# tuple_classの操作
class ModelMetaClass(type):
    """
    パラメタに関しては
    table_name : ClassNameでもあれば,DBNameでもあります
    bases      : ParentClassのtuple
    attrs      : Classの函数と値でできたkey:value
    """
    def __new__(cls, table_name, bases, attrs):
        if table_name == "Model":
            return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)
        # 属性とclassのマッピング
        mappings = dict()
        for k, v in attrs.items():
            # classの属性と列の対照関連をmappings_dictに保存
            if isinstance(v, Field):
                mappings[k] = v # mappingsに属性名, カラム名, 列名
        for k in mappings.keys():
            # classの属性を排除する,定義されたclassカラム,USer_classカラム汚さないため
            # インスタンスの中でしかアクセスできないようにする (class_name.属性)使用不可にする
            attrs.pop(k)

        # table名を小文字化する,つまりclass_nameを小文字化する
        # __table__属性を足して,保存されたテーブル名を代わりにする
        attrs['__table__'] = table_name.lower()

        # 属性と列関係の対処関係を保存
        attrs['__mappings__'] = mappings
        return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)


# modelの子class(base_class), modelのインスタンスに継承させる
# 具体的なCRUDを実現
# オブジェクト指向の三大継承規則,今後のmodelは全てそれらの方法可能になる

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
# insert into table_name(カラム名) values (値)
    def insert(self, column_list, param_list):
        print("insert方法実行しました")
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)
        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        # 内容安全性チェック
        args = self.__check_params(param_list)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(column_list), ','.join(args))
        res = self.__do_execute(sql)

    def __check_params(self, param_list):
         args = []
         for param in param_list:
             # もしパラメータに"が存在すれば、全てstr"に変化する,sqlインジェクションを防止
             if "\"" in param:
                 param = param.replace("\"", "\\\"")

             # パラメータの両側に"をつける
             param = "\"" + param + "\""
             args.append(param)

         return args

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.cursor()
        print(sql)
        rs = cur.execute(sql)
        conn.commit()
        cur.close()
        return rs
