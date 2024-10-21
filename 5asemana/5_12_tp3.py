import math

def meu_seno(x, iter):
    
    s = 0
    for i in range(iter):
        termo = (pow(-1, i) * pow(x,(2*i+1)) / math.factorial(2*i+1))
        last_s = s
        s = s + termo
        prec = abs(s - last_s)
        print(prec)

    print("\n")
    return s


def meu_seno_precision(x, precision):
    
    s = 0
    prec_atual = 1000
    i = 0
    while  prec_atual > precision:

        termo = (pow(-1, i) * pow(x,(2*i+1)) / math.factorial(2*i+1))
        last_s = s
        s = s + termo
        prec_atual = abs(s - last_s)
        print(f"{prec_atual} > {precision} ?" )
        i += 1

    print("\n")
    return s

# angulo =  15
x = 15


r = meu_seno_precision(x, 0.0000001)

print(f"O valor de sen({x}) é: {math.sin(x)}")
print(f"O valor de meu_seno({x}) é: {r}")