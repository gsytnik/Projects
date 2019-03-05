# Succ

import Classes
import random


def main():
    pass


def init_game():
    pass


def pick_cell_type():
    group = random.randint(1, 100)

    if group <= 25:
        return "swamp"
    if 25 < group <= 100:
        return "normal"


#   makes Hospital, Arsenal, and Warehouse
def assign_unique_cells():

    #   makes Hospital
    while True:
        index_x = random.randint(0, MAX_SIZE - 1)
        index_y = random.randint(0, MAX_SIZE - 1)

        if CELLS[index_x][index_y].type == "normal":
            CELLS[index_x][index_y].type = "Hospital"
        break

    #   makes Arsenal
    while True:
        index_x = random.randint(0, MAX_SIZE - 1)
        index_y = random.randint(0, MAX_SIZE - 1)

        if CELLS[index_x][index_y].type == "normal":
            CELLS[index_x][index_y].type = "Arsenal"
        break

    #   makes Warehouse
    while True:
        index_x = random.randint(0, MAX_SIZE - 1)
        index_y = random.randint(0, MAX_SIZE - 1)

        if CELLS[index_x][index_y].type == "normal":
            CELLS[index_x][index_y].type = "Warehouse"
        break


if __name__ == "__main__":

    #   init global variables
    PLAYERS = []
    CELLS = []

    #   init labyrinth size
    while True:
        try:
            MAX_SIZE = int(input("Enter board size 5-8: "))
            if 5 <= MAX_SIZE <= 8:
                break
            else:
                print("enter a number between 5 and 8.")
        except ValueError:
            print("enter a number value.")

    #   init cells
    for x in range(MAX_SIZE):
        CELLS.append([])
        for y in range(MAX_SIZE):
            CELLS[x].append(Classes.Cell(x, y, pick_cell_type()))

    assign_unique_cells()

    #   init player count
    while True:
        try:
            PLAYER_COUNT = int(input("Enter player count >= 2: "))
            if PLAYER_COUNT >= 2:
                break
            else:
                print("enter a number >= 2.")
        except ValueError:
            print("enter a number value.")


