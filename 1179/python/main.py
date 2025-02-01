par = []
impar = []

count = 0

while count < 15:
    num = int(input())
    if num % 2 == 0:
        if len(par) == 5:
            par_idx = 0
            while par_idx < 5:
                print(f"par[{par_idx}] = {par[par_idx]}")
                par_idx += 1
            par = []
        par.append(num)
    else:
        if len(impar) == 5:
            impar_idx = 0
            while impar_idx < 5:
                print(f"impar[{impar_idx}] = {impar[impar_idx]}")
                impar_idx += 1
            impar = []
        impar.append(num)
    count += 1

impar_idx = 0
while impar_idx < len(impar):
    print(f"impar[{impar_idx}] = {impar[impar_idx]}")
    impar_idx += 1

par_idx = 0
while par_idx < len(par):
    print(f"par[{par_idx}] = {par[par_idx]}")
    par_idx += 1