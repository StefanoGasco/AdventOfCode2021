

ENV = "real"

def input_file():
    with open(f'{ENV}_file.txt') as f:
        pattern, mapping = [x.split("\n") for x in f.read().split("\n\n")]
        pattern = list(pattern[0])
        mapping = {x:y for x,y in [z.split(" -> ") for z in mapping]}
    return pattern, mapping


pattern, mapping = input_file()

def rebuild(couple, threshold=1):
    if threshold <= 0:
        return couple
    couple.insert(1,mapping["".join(couple)])
    return rebuild(couple[:2],threshold-1) + rebuild(couple[1:3],threshold-1)[1:]

res = {pattern[0]: 1}

for x in range(len(pattern)-1):
    for k in rebuild(pattern[x:x+2], threshold=10)[1:]:
        res[k] = res.get(k, 0) + 1

print(max(res.values())-min(res.values()))