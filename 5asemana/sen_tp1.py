import math

def sen(x, precision):
    s = 0
    last_s = 0
    cur_precision = 1
    i = 0

    while cur_precision > precision:   
        termo = (pow(-1, i) * pow(x,(2*i+1)) / math.factorial(2*i+1))
        last_s = s
        s = s + termo
        cur_precision = abs(s - last_s)
        #print(last_s)
        print(f"{cur_precision:0.6f}")
        i+=1
        
    return s


print(sen(15,0.000001))
print(math.sin(15))

