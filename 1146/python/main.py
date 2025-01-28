x = int(input())

while x != 0:

    count = 1

    while count <= x:
        if count == x:
            print(count)
        else:
            print(count, end = ' ')
        count += 1
    x = int(input())