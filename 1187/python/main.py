operation = input()

result = None
count = 0

matrix = []

i = 0

while i < 12:
    j = 0
    while j < 12:
        num = float(input())
        if j > i and j < 11 - i:
            if result is None:
                result = num
            else:
                result += num
            count += 1
        j += 1
    i += 1

if operation == 'M':
    result = result / count


print('{:.1f}'.format(result))