

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

def map_folding(coords, threshold):
    res = set()
    for coord in coords:
        if coord[coord_index] >= threshold:
            coord[coord_index] = threshold - ((coord[coord_index] - threshold))
            res.add(tuple(coord))
        else:
            res.add(tuple(coord))
    return [list(x) for x in res]

def printer(coords):
    max_x, max_y = max([[x[0], x[1]] for x in coords])
    for y in range(max_y+1):
        for x in range(max_x+1):
            if [x, y] in coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()

coords, folds = input_file()

for fold in folds:
    coord_index = map_coords[fold[0]]
    coords = map_folding(coords, fold[1])

printer(coords)