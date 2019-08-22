vx = 0
kmx = 0
vy = 0.5
kmy = 0
time = 0
distance = int(input())
while kmy < kmx + distance:
    kmy = kmy + vy
    time = time + 1
print(time, "minutos")
