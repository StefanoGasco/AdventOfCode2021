
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        return [x.strip() for x in f.readlines()]

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
queue = []
scoreboard = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def add(char):
    queue.insert(0, char)

def remove():
    return queue.pop(0)


res = []
for line in input_file():
    points = 0
    error = False
    for x in line:
        if x in openers:
            add(closers[openers.index(x)])
        else:
            control = remove()
            if control != x:
                error = True
    if not error:
        for x in queue:
            points = points*5 + scoreboard[x]
    if points > 0:
        res.append(points)
    queue = []

print(sorted(res)[len(res)//2])