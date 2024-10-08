# Reference
# https://docs.python.org/3/library/string.html#format-specification-mini-language

m2km = 1.609

header = "{0:^15s} {1:^15s}".format("Milhas", "Quilómetros")

def print_m2km(km):
    print("{0:^15.2f} {1:^15.2f}".format(km, km*m2km))

print(header)
print("-" * len(header))
for i in range(10, 21):
    print_m2km(i)