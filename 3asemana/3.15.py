from aula_utils import print_string_frame

cadeia = "Monty Python"
n = 3

print_string_frame(cadeia)

for i in range(len(cadeia)):
    print(cadeia[0:i+1])
    