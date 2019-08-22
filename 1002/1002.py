import decimal
pi = 3.14159
A = float(input())
A = "{0:.2f}".format(A)
A = float(A)
area = pi*(A**2)
area = format(area, '.4f')
result = decimal.Decimal(area)
print("A={}".format(result),end="\n")
