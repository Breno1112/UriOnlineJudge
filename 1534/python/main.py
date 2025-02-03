try:
    while True:
        c = int(input())
        count = 0
        one_idx = 0
        two_idx = c - 1
        while count < c:
            s_line = list("3" * c)
            s_line[one_idx] = "1"
            s_line[two_idx] = "2"
            print(''.join(s_line))
            one_idx += 1
            two_idx -= 1
            count += 1
except EOFError:
    pass