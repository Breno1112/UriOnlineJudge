numbers = input().split(' ')

x = int(numbers[0])
y = int(numbers[1])

count = 1

inner_count = 1

while count <= y:
    while inner_count < x:
        print(count, end=' ')
        count = count + 1
        inner_count += 1
    print(count)
    count = count + 1
    inner_count = 1