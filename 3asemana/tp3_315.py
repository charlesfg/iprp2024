from aula_utils import print_string_frame

# cadeia = input("Insira a cadeia:\n")
# n = int(input("insira o tamanho da subcadeia\n"))
cadeia = "Monty Python"
n = 3

print_string_frame(cadeia)

for i in range(len(cadeia)):
    a = 0
    b = i+1
    print(a, b, cadeia[a:b])


