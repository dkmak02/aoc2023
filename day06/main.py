def get_data():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


def part(data, part=1):
    time = list(map(int, data[0].split()[1:]))
    distance = list(map(int, data[1].split()[1:]))

    if part == 2:
        time = list(map(int, ''.join(map(str, time)).split(',')))
        distance = list(map(int, ''.join(map(str, distance)).split(',')))

    possible = []
    ways_to_win = 1

    for t, d in zip(time, distance):
        winners = [i for i in range(t) if i * (t - i) > d]
        possible.append(winners)

    for i in possible:
        ways_to_win *= len(i)

    return ways_to_win



if __name__ == '__main__':
    data = get_data()
    print(part(data))
    print(part(data, part=2))

