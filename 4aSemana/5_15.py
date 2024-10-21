

def fact_iter(n):
    if n == 0:
        return 1
    
    r = n
    for i in range(1,n):
        r *=i
    return r

def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)
    
def exp_l(prec):

    e = 0
    for i in range(prec):
        e += 1 / (fact_rec(i))

    return e


p = 100

print(exp_l(p))