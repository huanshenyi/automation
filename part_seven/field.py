# FieldClassを定義
class Field(object):
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type

# もう一種類の方法
class StringField(Field):
    def __init__(self, column_name):
        super(StringField, self).__init__(column_name, "varchar(200)")

class IntegerField(Field):
    def __init__(self, column_name):
        super(IntegerField, self).__init__(column_name, "bigint")

class TextField(Field):
    def __init__(self, column_name):
        super(TextField, self).__init__(column_name, "text")

