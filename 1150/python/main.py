x = int(input())

z = None
times = 0
sum = 0


while z is None or z <= x:
    z = int(input())


while sum < z:
    sum += x + times
    times += 1
print(times)