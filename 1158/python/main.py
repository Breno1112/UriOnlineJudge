c = int(input())

while c > 0:
    x, y = [int(i) for i in input().split(' ')]
    inner_sum = 0
    while y > 0:
        while x % 2 == 0:
            x += 1
        inner_sum += x
        x += 1
        y -= 1
    print(inner_sum)
    c -= 1