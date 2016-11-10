# Representation of maze (goal = piece of cheese, start = rat)
class Maze:
    def __init__(self, n, start, goal):
        self.start = start
        self.goal = goal
        self.size = n
        self.walls = {}

        # Initialize wall boundaries.
        for x in range(n):
            for y in range(n):
                if x == 0:
                    self.add_wall(x, y, 'S')
                elif x == self.size - 1:
                    self.add_wall(x, y, 'N')
                if y == 0:
                    self.add_wall(x, y, 'W')
                elif y == self.size - 1:
                    self.add_wall(x, y, 'E')

    # From a position, add a wall in a direction - "N", "E", "S", or "W"
    def add_wall(self, pos, direction):
        x, y = pos[0], pos[1]
        if not (self.valid_pos(x) and self.valid_pos(y)):
            print("Bad positions given.")
            return
        if (x, y) not in self.walls:
            self.walls[(x, y)] = [direction]
        else:
            self.walls[(x, y)].append(direction)

    # Helper method for add_wall.
    def valid_pos(self, p):
        return p >= 0 and p < self.size

    # Returns boolean value representing whether there is a wall in a
    # certain direction from a position (x, y).
    def has_wall(self, pos, direction):
        x, y = pos[0], pos[1]
        if (x, y) not in self.walls:
            return False
        else:
            return direction in self.walls[(x, y)]
