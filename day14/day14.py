

ENV = "real"

def input_file():
    with open(f'{ENV}_file.txt') as f:
        pattern, mapping = [x.split("\n") for x in f.read().split("\n\n")]
        pattern = list(pattern[0])
        mapping = {x:y for x,y in [z.split(" -> ") for z in mapping]}
    return pattern, mapping


pattern, mapping = input_file()
res = {}
shortcut = {}

def sum_dict(d1, d2):
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}

lookup = dict()

def rebuild(couple, threshold=1):
    if threshold <= 0:
        return dict()
    couple_str = "".join(couple)
    if lookup.get(couple_str, {}).get(threshold, None):
        return lookup[couple_str][threshold]
    new = mapping[couple_str]
    res = {new:1}
    res = sum_dict(res, rebuild([couple[0], new],threshold-1))
    res = sum_dict(res, rebuild([new, couple[1]],threshold-1))
    lookup.setdefault(couple_str, {}).setdefault(threshold, {})
    lookup[couple_str][threshold] = res
    return res

final = dict()
for x in pattern:
    final[x] = final.get(x, 0) + 1
for x in range(len(pattern)-1):
    final = sum_dict(final, rebuild(pattern[x:x+2], threshold=40))

print(max(final.values())-min(final.values()))