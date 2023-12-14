def get_data():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def check_if_can_go_up(i, j, data):
    if data[i - 1][j] == ".":
        data[i][j] = "."
        if i - 1 < 0:
            data[i][j] = "O"
            return
        check_if_can_go_up(i - 1, j, data)
    else:
        data[i][j] = "O"

def spin(data):
    for o in range(4):
        for i, line in enumerate(data):
            if i == 0:
                continue
            for j, char in enumerate(line):
                if char == "O":
                    check_if_can_go_up(i, j, data)
        data = list(zip(*data[::-1]))
        for chuj, l in enumerate(data):
            l = list(l)
            data[chuj] = l
    return data
def part1(data):
    data = [list(x) for x in data]
    map_of_tuples = {}
    new_for_value = 0
    to_find = None
    for y in range(1000000000):
        data = spin(data)
        list_tuples = tuple(tuple(x) for x in data)
        if list_tuples in map_of_tuples.keys():
            if list_tuples == to_find:
                beggining_of_loop = 1000000000 - new_for_value
                new_for_value = y - new_for_value
                new_for_value = beggining_of_loop % new_for_value - 1
                break
            if to_find is None:
                to_find = list_tuples
                new_for_value = y
        map_of_tuples[list_tuples] = y
    for u in range(new_for_value):
        data = spin(data)
    sum_of_o_times = 0
    to_multiply = len(data)
    for l in data:
        sum_of_o_times += l.count("O") * to_multiply
        to_multiply -= 1
    print(sum_of_o_times)


if __name__ == '__main__':
    data = get_data()
    part1(data)
