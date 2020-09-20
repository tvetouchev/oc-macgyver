class Position:

    def __init__(self, start_pos):
        self.position = start_pos

    def change_x(self, num):
        x_axis = self.__clamp_axis(self.get_x, num)

        self.position[0] = x_axis

    def change_y(self, num):
        y_axis = self.__clamp_axis(self.get_y, num)

        self.position[1] = y_axis

    @staticmethod
    def __clamp_axis(axis, num):
        if axis + num > 750:
            return 750
        elif axis + num < 0:
            return 0

        return axis + num

    @property
    def get_position(self):
        return self.position

    @property
    def get_x(self):
        return self.position[0]

    @property
    def get_y(self):
        return self.position[1]
