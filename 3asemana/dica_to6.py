import math

def  tp6_quadrado(n):
    return math.pow(n, 2)

a = eval(input("numero para elevar ao quadrado"))
print(type(a))

resultado = tp6_quadrado(a)

print(f"O quadrado é : {resultado}")