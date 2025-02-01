count = 0

fib_arr = [0, 1]

test_cases = int(input())

while test_cases > 0:
    pos = int(input())
    while pos >= len(fib_arr):
        fib_arr.append(fib_arr[len(fib_arr) - 1] + fib_arr[len(fib_arr) - 2])
    print(f"Fib({pos}) = {fib_arr[pos]}")
    test_cases -= 1