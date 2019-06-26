from part_seven.field import Field,StringField
from part_seven.orm import Model

class Goods(Model):
    computer_part = Field("computer_part")
    computer_info = Field("computer_info", "text")

goods = Goods()
goods.insert("")