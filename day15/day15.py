
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        return [x.strip() for x in f.readlines()]

def neighbours(visited, max_height, max_width, h, w):
    n = []
    for c in [-1, 1]:
        if 0 <= h+c < max_height and f"{h+c},{w}" not in visited:
            n.append([h+c, w])
        if 0 <= w+c < max_width and f"{h},{w+c}" not in visited:
            n.append([h, w+c])
    return n


map = input_file()

height = len(map)
width = len(map[0])
visited = set()
tracker = {"0,0":0}
res = 9999999
while tracker:
    lowest_risk_coords = min(tracker, key=tracker.get)
    coords_risk = tracker[lowest_risk_coords]
    visited.add(lowest_risk_coords)
    del tracker[lowest_risk_coords]
    local_h, local_w = lowest_risk_coords.split(",")
    to_update = neighbours(visited, height, width, int(local_h), int(local_w))
    for coords in to_update:
        h, w = coords
        peer_risk = map[h][w]
        pointer = f"{h},{w}"
        tracker[pointer] = min(tracker.get(pointer, 999999), coords_risk + int(peer_risk))
        if pointer == f"{height-1},{width-1}":
            res = min(res, tracker[pointer])

print(res)
