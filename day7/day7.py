
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip().split(",") for x in f.readlines()][0]
    return [int(x) for x in lines]

def mid(n):
    return (min(n) + max(n)) // 2

def distances(array, x):
    for i in array:
        yield abs(x-i)

def split(n):
    return n//2, n+n//2

def find_shortest(array):
    low = sum(distances(array, 0))
    for x in range(1, len(array)):
        new_dist = sum(distances(array, x))
        if new_dist < low:
            low = new_dist
    return low


arr = input_file()
print(find_shortest(arr))