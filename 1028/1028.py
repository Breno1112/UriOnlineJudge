def popular(a):

    n = []
    loc = ""
    for x in a:
        if x != " ":
            loc = loc + str(x)
        else:
            n.append(int(loc))
            loc = ""
    if loc !="":
        n.append(int(loc))
    return n

def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    print(num1)

a = int(input())
for x in range(a):
    testes = popular(input())
    mdc(testes[0], testes[1])
