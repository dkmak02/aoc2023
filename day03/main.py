def get_data():
    with open('input.txt') as f:
        input = f.read().splitlines()
    return input


def find_number_and_replace(line):
    indexes = []
    numbver = ""
    for i, char in enumerate(line):
        if char.isdigit():
            numbver += char
        else:
            if numbver != "":
                indexes.append((i, len(numbver)))
                numbver = ""
    if numbver != "":
        indexes.append((len(line), len(numbver)))
    return indexes


def get_symbols(data):
    symbols = set()
    for line in data:
        for char in line:
            if not char.isdigit() and char != '.':
                symbols.add(char)
    return list(symbols)


def check_neighbours(data, indexes, previous, next):
    possible_numbers = []
    for i in indexes:
        start = i[0] - i[1]
        end = i[0] if i[0] < len(data) else len(data) - 1
        possible_number = data[start:end]
        if i[0] == len(data):
            possible_number = data[start:end + 1]
        for line in [data,previous, next]:
            if line is None:
                continue
            j_s = start - 1 if start - 1 > 0 else 0
            j_e = end + 1 if end + 1 < len(line) else (len(line) - 1)
            for j in range(j_s, j_e):
                if line[j] in symbols:
                    possible_numbers.append(possible_number)
    return sum([int(x) for x in possible_numbers])


def part1(data):
    sum = 0
    for i, line in enumerate(data):
        previous = data[i - 1] if i > 0 else None
        next = data[i + 1] if i < len(data) - 1 else None
        indexes = find_number_and_replace(line)
        sum += check_neighbours(line, indexes, previous, next)
    return sum


def find_gears(line, previous, next):
    indexes = find_number_and_replace(line)
    indexes_previous = find_number_and_replace(previous) if previous is not None else []
    indexes_next = find_number_and_replace(next) if next is not None else []
    lines = {0: line, 1: previous, 2: next}
    sums = []
    for i, char in enumerate(line):
        if char != '*':
            continue
        numbers = []
        for u, index in enumerate([indexes, indexes_previous, indexes_next]):
            for j in index:
                for z in range(j[0] - j[1] - 1, j[0] + 1):
                    if z == i:
                        numbers.append(lines[u][j[0] - j[1]:j[0]])
        if len(numbers) == 2:
            sums.append(int(numbers[0]) * int(numbers[1]))
    return sum(sums)


def part2(data):
    sum = 0
    for i, line in enumerate(data):
        previous = data[i - 1] if i > 0 else None
        next = data[i + 1] if i < len(data) - 1 else None
        if '*' in line:
            sum += find_gears(line, previous, next)
    return sum


if __name__ == '__main__':
    data = get_data()
    symbols = get_symbols(data)
    print(part1(data))
    print(part2(data))
