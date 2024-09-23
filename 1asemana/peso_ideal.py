def peso_ideal(alt, s):
    if s == 0:
        p = (72.7 * alt) - 58
    else:
        p = (62.1 * alt) - 44.7
    
    return p


# Calcula o peso ideal

altura =  eval(input("Qual a sua altura (em metros) ?\n"))

sexo =  eval(input("Qual o seu sexo (0 - Homem, 1 - Mulher) ?\n"))

print('O seu peso ideal é {}'.format(peso_ideal(altura,sexo)))
#print('O seu peso ideal é {}'.format(peso_ideal))
