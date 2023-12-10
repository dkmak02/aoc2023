from shapely.geometry import Point, Polygon

def get_data():
    with open('input.txt') as f:
        return f.read().splitlines()


def s_locataion(data):
    for i in data:
        for j in i:
            if j == 'S':
                return data.index(i), i.index(j)


def part1(data):
    loop_index = []
    goto = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direction = {'|': [goto[0], goto[2]]
        , '-': [goto[1], goto[3]]
        , 'L': [goto[2], goto[3]]
        , 'J': [goto[1], goto[2]]
        , '7': [goto[0], goto[1]]
        , 'F': [goto[0], goto[3]]
                 }
    out_direction = {'|': [goto[0], goto[2]]
        , '-': [goto[1], goto[3]]
        , 'L': [goto[0], goto[1]]
        , 'J': [goto[0], goto[3]]
        , '7': [goto[2], goto[3]]
        , 'F': [goto[1], goto[2]]}
    loc_s = s_locataion(data)
    found = False
    next = None
    while True:
        if found is False:
            for i in goto:
                new_cords = [sum(x) for x in zip(loc_s, i)]
                if data[new_cords[0]][new_cords[1]] in direction and all(x >= 0 for x in new_cords):
                    next = data[new_cords[0]][new_cords[1]]
                    loop_index.append(new_cords)
                    found = True
                    break
        else:
            now = loop_index[-1]

            for j in out_direction[next]:
                new_cords = [sum(x) for x in zip(now, j)]
                if new_cords in loop_index:
                    continue
                if len(loop_index) == 2 and new_cords == list(loc_s):
                    continue
                loop_index.append(new_cords)
                next = data[new_cords[0]][new_cords[1]]
        if next == 'S':
            break
    best = len(loop_index)/2
    print(best)
    return loop_index


def part2(grid, indexes):
    result = 0
    for i in range(len(grid)):
        left = 0
        for j in range(len(grid[0])):
            if [i, j] not in indexes and left % 2 == 1:
                result += 1
            if grid[i][j] in ['|', 'L', 'J', 'S'] and [i, j] in indexes:
                left += 1
    print(result)


if __name__ == '__main__':
    data = get_data()
    indesxes = part1(data)
    part2(data, indesxes)

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''
