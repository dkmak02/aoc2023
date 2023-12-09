def get_data():
    with open('input.txt') as f:
        return f.read().splitlines()


def get_value(line, part2=False):
    values = line.split(' ')
    values = [int(i) for i in values]
    dif_num = []
    dif_num.append(values)
    while values != [0]*len(values):
        new_num = []
        for i in range(len(values)-1):
            new_num.append(values[i+1] - values[i])
        values = new_num
        dif_num.append(new_num)
    sum = 0
    position = 0 if part2 else -1
    for i in range(len(dif_num)-1, -1, -1):
        if part2:
            sum = dif_num[i][position] - sum
        else:
            sum += dif_num[i][position]
    return sum


def part2(data):
    suma = 0
    for i in data:
        suma += get_value(i, True)
    print(suma)
def part1(data):
    suma = 0
    for i in data:
        suma += get_value(i)
    print(suma)



if __name__ == '__main__':
    data = get_data()
    part1(data)
    part2(data)
