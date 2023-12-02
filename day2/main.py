max_red = 12
max_green = 13
max_blue = 14


def read_data():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        return lines


def is_possible(game):
    game_number = int(game[5:game.index(":")])
    turns = game[7:].split(";")
    for turn in turns:
        blue = 0
        green = 0
        red = 0
        turn = turn.split(",")
        for color in turn:
            if 'red' in color:
                red += int(''.join(list(filter(str.isdigit, color))))
                if red > max_red:
                    return 0
            elif 'green' in color:
                green += int(''.join(list(filter(str.isdigit, color))))
                if green > max_green:
                    return 0
            elif 'blue' in color:
                blue += int(''.join(list(filter(str.isdigit, color))))
                if blue > max_blue:
                    return 0
    return game_number


def min_number_of_cubes(game):
    turns = game[7:].split(";")
    blue = 0
    green = 0
    red = 0
    for turn in turns:
        turn = turn.split(",")
        for color in turn:
            if 'red' in color:
                red = max(red, int(''.join(list(filter(str.isdigit, color)))))
            elif 'green' in color:
                green = max(green, int(''.join(list(filter(str.isdigit, color)))))
            elif 'blue' in color:
                blue = max(blue, int(''.join(list(filter(str.isdigit, color)))))
    return red*green*blue


if __name__ == '__main__':
    games_sum = 0
    cubes_power = 0
    data = read_data()
    for game in data:
        cubes_power += min_number_of_cubes(game)
        games_sum += is_possible(game)
    print(cubes_power)
    print(games_sum)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
