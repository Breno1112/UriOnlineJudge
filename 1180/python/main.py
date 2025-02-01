num_count = int(input())

numbers = input().split(" ")


count = 0

menor_valor = None
menor_posicao = None

while count < num_count:
    searching_num = int(numbers[count])
    if menor_valor is None or searching_num < menor_valor:
        menor_valor = searching_num
        menor_posicao = count
    count += 1
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {menor_posicao}")