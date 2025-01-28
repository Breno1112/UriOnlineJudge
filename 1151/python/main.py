a = 0
b = 1
c = None
count = 2

n = int(input())

sequence = '0 1 '

if n == 1:
    print('0', end='')
elif n == 2:
    print(sequence, end='')
else:
    print(sequence, end='')
    while count < n:
        c = a + b
        a = b
        b = c
        if(count + 1 == n):
            print(c)
        else:
            print(c, end=' ')
        count += 1