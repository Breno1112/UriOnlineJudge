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

    if n[0] == 0 and n[1] == 0 and n[2] == 0 and n[3] == 0:
        return "end"
    return n

def tempo(lista):
    horas = lista[2] - lista[0]
    minutos = lista[3] - lista[1]
    tempoint = horas*60 + minutos
    if tempoint < 0:
        tempoint = tempoint * -1
        tempo = 1440 - tempoint
    else:
        tempo = horas*60 + minutos
    return tempo


a = popular(input())
while a != 'end':
    print(tempo(a))
    a = popular(input())
