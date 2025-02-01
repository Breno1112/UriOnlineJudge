number = float(input())

count = 0

while count < 100:
    print("N[{}] = {:.4f}".format(count, number))
    number = number / 2
    count +=1