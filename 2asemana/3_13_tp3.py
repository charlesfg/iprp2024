frase = "A vida é uma constante oscilação entre a ânsia de ter e o tédio de possuir"

for v in "aeiouAEIOUéáãâ":
    frase = frase.replace(v, " ")
    
print(frase)