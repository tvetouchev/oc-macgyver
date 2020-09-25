class Position:

    def __init__(self, start_pos):
        self.position = start_pos

    def change_x(self, num):
        x_axis = self.__clamp_axis(self.get_x + num)

        self.position[0] = x_axis

    def change_y(self, num):
        y_axis = self.__clamp_axis(self.get_y + num)

        self.position[1] = y_axis

    def change_pos(self, position):
        x_axis = self.__clamp_axis(position[0])
        y_axis = self.__clamp_axis(position[1])

        self.position = [x_axis, y_axis]

    @staticmethod
    def __clamp_axis(axis):
        if axis > 750:
            return 750
        elif axis < 0:
            return 0

        return axis

    @property
    def get_position(self):
        return self.position

    @property
    def get_x(self):
        return self.position[0]

    @property
    def get_y(self):
        return self.position[1]

    @classmethod
    def difference_between_position(cls, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
