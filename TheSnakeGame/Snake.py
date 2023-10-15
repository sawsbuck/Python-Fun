from Constants import*

class Snake:
    def __init__(self):
        self.body = [(4, 3), (4, 2), (4, 1)]
        self.direction = (1, 0)

    def move(self, grow):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def check_collision(self):
        if (
            self.body[0][0] < 0
            or self.body[0][0] >= GRID_WIDTH
            or self.body[0][1] < 0
            or self.body[0][1] >= GRID_HEIGHT
            or self.body[0] in self.body[1:]
        ):
            return True
        return False

    def check_food_collision(self, food):
        if self.body[0] == food:
            return True
        return False