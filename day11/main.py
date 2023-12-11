import numpy as np

def get_data():
    with open('input.txt','r') as f:
        return f.read().splitlines()

def expand(line):
    if '#' in line:
        return False
    return True


def find_index(data):
    indexes = []
    for i,line in enumerate(data):
        for j, char in enumerate(line):
            if char == '#':
                indexes.append((i,j))
    return indexes
def part1(data):
    to_expand_rows =[]
    to_expand_col = []
    row_len = len(data[0])
    for i, line in enumerate(data):
        col = ''
        if expand(line):
            to_expand_rows.append(i)
        for j in range(len(data)):
            col+=data[j][i]
        if expand(col):
            to_expand_col.append(i)
    for i in to_expand_rows:
        data.insert(i+to_expand_rows.index(i), '.'*row_len)
    col_len = (len(data))
    for i in to_expand_col:
        for j in range(row_len+len(to_expand_rows)):
            s_l = list(data[j])
            s_l.insert(i+to_expand_col.index(i), '.')
            data[j] = ''.join(s_l)
    gal_index = find_index(data)
    suma = 0
    for i1 in gal_index:
        for i2 in gal_index:
            if i1 != i2:
                suma += abs(i1[0]-i2[0]) + abs(i1[1]-i2[1])
    print(suma/2)
if __name__ == '__main__':
    data = get_data()
    part1(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
