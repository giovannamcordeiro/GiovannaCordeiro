from dino_runner.utils.constants import MUSHROOM, MUSHROOM_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Mushroom(PowerUp):
    def __init__(self):
        self.image = MUSHROOM
        self.type = MUSHROOM_TYPE
        super().__init__(self.image, self.type)