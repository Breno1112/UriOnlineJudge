def popular(a):

    n = []
    loc = ""
    for x in a:
        if x != " ":
            loc = loc + str(x)
        else:
            n.append(float(loc))
            loc = ""
    if loc !="":
        n.append(float(loc))
    return n


a, b = popular(input())
c, d = popular(input())
resultado = ((c-a)**2 + (d-b)**2)**(1/2)
print("{:.4f}".format(resultado))
