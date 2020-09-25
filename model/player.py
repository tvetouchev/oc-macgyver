from model.image import Image
from model.position import Position


class Player(Position, Image):
    CASE_SIZE = 50

    def __init__(self, pos, img):
        Position.__init__(self, pos)
        Image.__init__(self, img)

    def move_left(self):
        return [self.get_x - self.CASE_SIZE, self.get_y]

    def move_right(self):
        return [self.get_x + self.CASE_SIZE, self.get_y]

    def move_up(self):
        return [self.get_x, self.get_y - self.CASE_SIZE]

    def move_down(self):
        return [self.get_x, self.get_y + self.CASE_SIZE]
