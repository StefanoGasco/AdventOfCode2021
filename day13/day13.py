

ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        coords, folds = [x.split("\n") for x in f.read().split("\n\n")]
        coords = [list(map(int, x.split(","))) for x in coords]
        folds = [x.split(" ")[-1].split("=") for x in folds]
        folds = [(x[0],int(x[1])) for x in folds]
    return coords, folds


map_coords = {
    "x": 0,
    "y": 1
}
coords, folds = input_file()
res = set()

coord_index = map_coords[folds[0][0]]
for coord in coords:
    if coord[coord_index] >= folds[0][1]:
        coord[coord_index] = folds[0][1] - ((coord[coord_index] - folds[0][1]))
        res.add(tuple(coord))
    else:
        res.add(tuple(coord))
print(len(res))
print(res)