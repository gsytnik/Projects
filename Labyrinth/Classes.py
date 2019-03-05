class Player:

    def __init__(self, x_pos, y_pos, name):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name

        self.stuck = False
        self.stuck_counter = 0
        self.has_key = False
        self.alive = True

        self.ammo = 3
        self.grenades = 3
        self.cement = 1

    def die(self):
        self.alive = False
        self.ammo = 0
        self.grenades = 0
        self.cement = 0

    def resurrect(self):
        self.alive = True
        self.grenades = 1

    def move(self, dx, dy):
        self.x_pos += dx
        self.y_pos += dy

    def use_grenade(self):
        if self.grenades > 0:
            self.grenades -= 1
        else:
            print("The player has no grenades.")

    def use_cement(self):
        if self.cement > 0:
            self.cement -= 1
        else:
            print("The player has no cement.")

    def fire_gun(self):
        if self.ammo > 0:
            self.ammo -= 1
        else:
            print("The player has no ammo")

    def obtain_key(self):
        self.has_key = True

    def drop_key(self):
        self.has_key = False

    def lose_turn(self, stuck_counter):
        self.stuck_counter += stuck_counter


class Cell:

    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.type = group
        self.contains_key = False
        self.north_wall = False
        self.south_wall = False
        self.east_wall = False
        self.west_wall = False
        self.capital_walls = []

    def create_wall(self, direction):
        if direction == "N":
            self.north_wall = True
        elif direction == "S":
            self.south_wall = True
        elif direction == "E":
            self.east_wall = True
        elif direction == "W":
            self.west_wall = True

    def make_capital_wall(self, max_size):
        if self.y == 0:
            self.capital_walls.append("N")
        if self.y == max_size:
            self.capital_walls.append("S")

        if self.x == 0:
            self.capital_walls.append("W")
        if self.x == max_size:
            self.capital_walls.append("E")

    def contain_key(self, value):
        self.contains_key = value
