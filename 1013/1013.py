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


l = popular(input())
maior = l[0]
for x in l:
    if x > maior:
        maior = x
print("{} eh o maior".format(int(maior)))
