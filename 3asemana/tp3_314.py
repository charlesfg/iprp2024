from aula_utils import print_string_frame

#cadeia = "Monty Python"
cadeia = input("Insira a cadeia:\n")
n = int(input("insira o tamanho da subcadeia\n"))

print_string_frame(cadeia)

for i in range(len(cadeia)-n+1):
    print(i, i+n, cadeia[i:i+n])


