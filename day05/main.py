def get_data():
    with open('input.txt','r') as f:
        input = f.readlines()
    return input



def get_initial_seeds_number(line):
    return list(filter(lambda x: x != '\n', line[7:].split()))


def get_map(data, key):
    start = 0
    map = {}
    for line in data:
        if key in line:
            start = 1
        elif line == "\n" and start == 1:
            break
        elif start == 1:
            line_info = list(filter(lambda x: x != '\n', line.split()))
            for i in range(int(line_info[2])):
                map[int(line_info[1])+i] = int(line_info[0])+i
    for v in range(max(map)):
        if v in map:
            continue
        else:
            map[v] = v
    return map

def part1(data,seeds):
    soil_map = get_map(data, "seed-to-soil map:")
    fertilizer_map = get_map(data,'soil-to-fertilizer map:')
    water_map = get_map(data, 'fertilizer-to-water map:')
    light_map = get_map(data, 'water-to-light map:')
    temperature_map = get_map(data, 'light-to-temperature map:')
    humidity_map = get_map(data, 'temperature-to-humidity map:')
    location_map = get_map(data, 'humidity-to-location map:')
    min_loc = None
    for seed in seeds:
        seed = int(seed)
        soil = soil_map[seed] if seed in soil_map else seed
        fertilizer = fertilizer_map[soil] if soil in fertilizer_map else soil
        water = water_map[fertilizer] if fertilizer in water_map else fertilizer
        light = light_map[water] if water in light_map else water
        temp = temperature_map[light] if light in temperature_map else light
        humidity = humidity_map[temp] if temp in humidity_map else temp
        location = location_map[humidity] if humidity in location_map else humidity
        min_loc = location if min_loc > location or min_loc is None else min_loc
    return min_loc





if __name__ == '__main__':
    data = get_data()
    initial_seeds = get_initial_seeds_number(data[0])
    print(part1(data, initial_seeds))


