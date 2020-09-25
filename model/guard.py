from model.image import Image
from model.position import Position


class Guard(Position, Image):

    def __init__(self, pos, img):
        Position.__init__(self, pos)
        Image.__init__(self, img)

    def kill_guard(self):
        self.change_image('Tombstone.png')
