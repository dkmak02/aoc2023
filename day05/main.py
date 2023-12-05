def get_data():
    with open('input.txt','r') as f:
        input = f.readlines()
    return input



def get_initial_seeds_number(line):
    return list(filter(lambda x: x != '\n', line[7:].split()))


def get_map(data, key, looking_for):
    start = 0
    to_re = looking_for
    for line in data:
        if key in line:
            start = 1
        elif line == "\n" and start == 1:
            break
        elif start == 1:
            line_info = list(filter(lambda x: x != '\n', line.split()))
            k1 = int(line_info[0])
            k2 = int(line_info[1])
            k3 = int(line_info[2])
            dif = looking_for - k2
            if 0 < dif < k3:
                return k1+dif

    return to_re

def part1(data,seeds):
    min_loc = []
    for i in range(0,len(seeds),2):
        for seed in range(int(seeds[i+1])):
            seed = int(seeds[i])+seed
            soil = get_map(data, "seed-to-soil map:", seed)
            fertilizer = get_map(data, 'soil-to-fertilizer map:', soil)
            water = get_map(data, 'fertilizer-to-water map:', fertilizer)
            light = get_map(data, 'water-to-light map:', water)
            temperature = get_map(data, 'light-to-temperature map:', light)
            humidity = get_map(data, 'temperature-to-humidity map:', temperature)
            location = get_map(data, 'humidity-to-location map:', humidity)
            min_loc.append(location)
    return min(min_loc)





if __name__ == '__main__':
    data = get_data()
    initial_seeds = get_initial_seeds_number(data[0])
    print(part1(data, initial_seeds))


