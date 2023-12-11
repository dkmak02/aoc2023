def get_data():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


def expand(line):
    if '#' in line:
        return False
    return True


def find_index(data):
    indexes = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '#':
                indexes.append((i, j))
    return indexes


def is_between(x1, x2, to_expand, to_add):
    suma = 0
    for t in to_expand:
        if x1 <= t <= x2:
            suma += to_add
        elif x2 <= t <= x1:
            suma += to_add
    return suma


def part1(data, to_add=0):
    to_expand_rows = []
    to_expand_col = []
    for i, line in enumerate(data):
        col = ''
        if expand(line):
            to_expand_rows.append(i)
        for j in range(len(data)):
            col += data[j][i]
        if expand(col):
            to_expand_col.append(i)
    gal_index = find_index(data)
    suma = 0
    gal_index_2 = gal_index.copy()
    for i1 in gal_index:
        for i2 in gal_index_2:
            if i1 != i2:
                suma += abs(i1[0] - i2[0]) + abs(i1[1] - i2[1])
                suma += is_between(i1[0], i2[0], to_expand_rows, to_add-1)
                suma += is_between(i1[1], i2[1], to_expand_col, to_add-1)
        gal_index_2.remove(i1)
    print(suma)


if __name__ == '__main__':
    data = get_data()
    # part1(data)
    part1(data, 1000000)

