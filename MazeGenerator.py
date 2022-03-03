import csv
import random

# The table from the sorce code of Entombed
TABLE = {
    "00000": 1,
    "00001": 1,
    "00010": 1,
    "00011": 2,
    "00100": 0,
    "00101": 0,
    "00110": 2,
    "00111": 2,
    "01000": 1,
    "01001": 1,
    "01010": 1,
    "01011": 1,
    "01100": 2,
    "01101": 0,
    "01110": 0,
    "01111": 0,
    "10000": 1,
    "10001": 1,
    "10010": 1,
    "10011": 2,
    "10100": 0,
    "10101": 0,
    "10110": 0,
    "10111": 0,
    "11000": 2,
    "11001": 0,
    "11010": 1,
    "11011": 2,
    "11100": 2,
    "11101": 0,
    "11110": 0,
    "11111": 0
}

# The maze gonna be a list of zeroes and ones
maze = []


def generate_random_bit():
    rnd_bit = random.randint(0, 1)
    return rnd_bit


# Generate an empty field (Zeroes) for creating maze on it
def base(maze):
    for i in range(150):
        temp = []
        for i in range(20):  # add a line of 0
            temp.append(0)
        maze.append(temp)

    return maze


# Edit the empty field with the "algorythm" and generate a maze(add one and twoes)
def generate_maze(maze):
    for i in range(len(maze)):  # generate the left and righ-hand walls
        maze[i][0] = 1
        maze[i][1] = 1
        maze[i][-1] = 1
        maze[i][-2] = 1

    for y in range(1, 150):  # 150 vertical bits
        for x in range(1, 9):  # 8 horizantal bits
            a = maze[y][x - 2]  # reversed x and y used due to list index
            b = maze[y][x - 1]
            c = maze[y - 1][x - 1]
            d = maze[y - 1][x]
            e = maze[y - 1][x + 1]

            if x == 2:
                a = 1
                b = 0
                c = generate_random_bit()

            if x == 3:
                a = 0

            if x == 9:
                e = generate_random_bit()

            # Generate the wall with the table
            condotion = str(a) + str(b) + str(c) + str(d) + str(e)
            z = TABLE[condotion]
            if z == 2:
                z = generate_random_bit()

            maze[y][x + 1] = z
            maze[y][18 - x] = z  # Mirror the wall

    return maze


# Write the maze list into a csv file
def to_csv(maze):
    with open('Assets/maze.csv', 'w+', newline='') as f:
        f.truncate()
        writer = csv.writer(f)
        writer.writerows(maze)
        f.close()


# RUNNING FUNCTIONS
# ==========
base(maze)
generate_maze(maze)
to_csv(maze)
