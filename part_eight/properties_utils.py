

class Properties():
    def __init__(self, file_name):
        self.properties_file_name = file_name
        self.properties = {}

    def get_properties(self)->dict:
        with open(self.properties_file_name, 'r',encoding='utf-8') as pro_file:
             for line in pro_file.readlines():
                 pass
