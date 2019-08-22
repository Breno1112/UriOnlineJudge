def popular(a):
    n = []
    loc = ""
    for x in a:
        if x != " ":
            loc = loc + str(x)
        else:
            n.append(float(loc))
            loc = ""
    if loc != "":
        n.append(float(loc))
    return n


a, b, c = popular(input())
d, e, f = popular(input())

print("VALOR A PAGAR: R$ {:.2f}".format(b*c + e*f))

