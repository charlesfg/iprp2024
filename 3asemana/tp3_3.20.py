a = 'abc'
c = a[0]
o = ord(a[0])
print(c)
print(chr(o+10))

tabela = ""
for i in range(65, 123):
    if i < 97 and i > 90:
        continue
    tabela += chr(i)
    #print(chr(i), end="")

print(tabela)

print(tabela[10])

def codifica(c, d):
    for i in range(len(tabela)):
        if tabela[i] == c:
            return tabela[i+d % len(tabela)]

p = "casa"
# a -> a + 3
print(codifica(p[0],3))



