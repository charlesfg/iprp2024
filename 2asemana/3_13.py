

frase = "A vida é uma constante oscilação entre a ânsia de ter e o tédio de possuir."


# Versao 1
for i in range(len(frase)):
    c = frase[i]
    
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print(frase[i], end="")
    else:
        print(" ", end="")
    
print("\n-----")
    
    
fr

# Versao 1
for i in range(len(frase)):
    if frase[i] not in 'aeiou':
      print(frase[i], end="")
    else:
        print(" ", end="")
    
