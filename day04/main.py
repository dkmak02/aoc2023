def get_data():
    with open('input.txt','r') as f:
        input = f.readlines()
    return input

def get_number_of_winning(line):
    winning = list(filter(lambda x: x != '', list(line[line.index(':')+1:line.index('|')].split(' '))))
    my_numbers = list(filter(lambda x: x != '', list(line[line.index('|')+1:-1].split(' '))))
    return len([x for x in my_numbers if x in winning])


def part1(data):
    sum = 0
    for line in data:
        winning_count = get_number_of_winning(line)
        sum += 2**(winning_count - 1) if winning_count > 0 else 0
    return sum


def part2(data):
    card_times = {}
    sum = 0
    for line in data:
        winning_count = get_number_of_winning(line)
        id = int(line[5:line.index(':')])
        if id in card_times:
            card_times[id] +=1
        else:
            card_times[id] = 1
        for j in range(card_times[id]):
            for i in range(id+1,id+winning_count+1):
                if i in card_times:
                    card_times[i] += 1
                else:
                    card_times[i] = 1
    for key, value in card_times.items():
        sum += value
    return sum



if __name__ == '__main__':
    data = get_data()
    print(part1(data))
    print(part2(data))


