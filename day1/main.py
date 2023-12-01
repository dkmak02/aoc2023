sum = 0
filter_v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapa = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5','six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'sevenine': '79'}

def check(line):
    coski = []
    for i in filter_v:
        if i in line:
            coski.append((i, line.index(i)))
        if line.rfind(i) != -1:
            coski.append((i, line.rfind(i)))
    coski.sort(key=lambda tup: tup[1])
    return [mapa[coski[0][0]] if coski[0][0] in mapa else coski[0][0],
            mapa[coski[-1][0]] if coski[-1][0] in mapa else coski[-1][0]]


with open('input.txt') as f:
    for line in f:
        line = check(line)
        val0 = line[0]
        val1 = line[-1]
        sum += int(val0 + val1)
print(sum)