
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip().split(" | ") for x in f.readlines()]
    return [[x[0].split(" "), x[1].split(" ")] for x in lines]

valid_outputs = [2,4,3,7]
count = 0
for x in input_file():
    for d in x[1]:
        if len(d) in valid_outputs:
            count += 1
print(count)