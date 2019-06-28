from part_seven.field import Field,StringField
from part_seven.orm import Model

class Goods(Model):
    computer_part = Field("computer_part")
    computer_info = Field("computer_info", "text")

goods = Goods()
goods.insert(["computer_part", "computer_info"], ["组件", "组件信息"])
result = goods.select(["computer_part", "computer_info"], ["computer_part='组件'"])
print(result)
goods.update(["computer_part='组件1'"], ["computer_part='组件'"])