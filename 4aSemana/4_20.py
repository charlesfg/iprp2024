

def calc_pop(n, f, e, p, d=365):
    m = d * 24 * 60
    return p + (m // n - m // f - m // e)


fn = eval(input("Frequência de nascimentos (em minutos): "))
ff = eval(input("Frequência de falecimentos (em minutos): "))
fe = eval(input("Frequência de emigração (em minutos): "))

pop_i = eval(input("Qual a populacão inicial ? ")) 

print("A população ao fim de um ano é: ", calc_pop(fn,ff, fe, pop_i))

