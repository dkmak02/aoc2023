import heapq


def get_data():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def part1(data):
    directions = {'right': [0, 1], 'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'none': [0, 0]}
    end = [len(data) - 1, len(data[0]) - 1]
    queue = []
    visited = set()
    can_not_go = {'right': 'left', 'up': 'down', 'down': 'up', 'left': 'right', 'none': 'none'}
    heapq.heappush(queue, (0, 'none', [0, 0], 0))

    while queue:
        cost, going_to, now, steps = heapq.heappop(queue)

        if now == end:
            print(cost)
            break

        if tuple(now) in visited:
            continue

        visited.add(tuple(now))

        for direction in directions:
            if steps > 9 and direction == going_to:
                continue

            new_row = now[0] + directions[direction][0]
            new_col = now[1] + directions[direction][1]

            if steps >= 4 or direction == going_to:
                if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
                    if can_not_go[direction] == going_to:
                        continue

                    new_cost = cost + int(data[new_row][new_col])
                    new_steps = steps + 1 if direction == going_to else 0
                    heapq.heappush(queue, (new_cost, direction, [new_row, new_col], new_steps))


if __name__ == '__main__':
    data = get_data()
    part1(data)
