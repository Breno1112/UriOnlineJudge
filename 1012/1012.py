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


a, b, c = popular(input())
print("TRIANGULO: {:.3f}".format((a*c)/2))
print("CIRCULO: {:.3f}".format(3.14159*(c**2)))
print("TRAPEZIO: {:.3f}".format((a + b)*c/2))
print("QUADRADO: {:.3f}".format(b**2))
print("RETANGULO: {:.3f}".format(a*b))
