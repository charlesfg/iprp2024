# Reference
# https://docs.python.org/3/library/string.html#format-specification-mini-language


def print_fmt(a,b):
    print("{0:15d}{1:15d}".format(a,b))
    
print("{0:>15s}{1:>15s}".format("Numero","Quadrado"))

for i in range(1,6):
    a = i
    print_fmt(a, a**2)

