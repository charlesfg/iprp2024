

def codificar(s, d):
    ns = ""
    for i in s:
        ns += chr(ord(i)+d)
    return ns

codigo = "charles goncalves"
print(codigo)
print(codificar(codigo,3))