# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 4
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.direction = (self.direction % 4) + 1
            if instruction == 'L':
                self.direction = (self.direction -2) % 4 + 1
            if instruction == 'A':
                    if self.direction == NORTH:
                        self.y_pos += 1
                    elif self.direction == EAST:
                        self.x_pos += 1
                    elif self.direction == SOUTH:
                        self.y_pos -= 1
                    elif self.direction == WEST:
                        self.x_pos -= 1

                    self.coordinates = (self.x_pos, self.y_pos)