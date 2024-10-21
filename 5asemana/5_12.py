from math import factorial, sin

def sen(x, prec):

    s = 0
    for i in range(20):
        s += (pow(-1,i) * pow(x, 2*i+1)) / factorial(2*i+1)
        print(s)
    print("\n")
    return s


print(sen(15,0.01))

print(sin(15))

