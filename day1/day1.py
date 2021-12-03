def input_file():
    with open('input_file.txt') as f:
        lines = [int(x.strip()) for x in f.readlines()]
    return lines

def example_file():
    with open('example_file.txt') as f:
        lines = [int(x.strip()) for x in f.readlines()]
    return lines

def count_increases(arr):
    count = 0
    prev = arr[0]
    for x in arr[1:]:
        if x > prev:
            count += 1
        prev = x
    return count

def trisum(arr):
    sum = 0
    res = []
    for i,x in enumerate(arr):
        if i < 3:
            if i == 0:
                to_sub = x
            sum += x
            continue
        if i == 3:
            res.append(sum)
        sum += x-to_sub
        res.append(sum)
        to_sub = arr[i-2]
    return res

print(count_increases(trisum(input_file())))
