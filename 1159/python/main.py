x = int(input())

while x != 0:
    inner_sum = 0
    c = 0
    while c < 5:
        if x % 2 != 0:
            x += 1
        inner_sum += x
        c += 1
        x += 1
    print(inner_sum)
    x = int(input())
        