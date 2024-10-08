
def acronimo(frase):
    # converto tudo para maiúsculo
    f = frase.upper()
    # o primeiro caracter é o primeiro do acrônimo
    acro = f[0]
    for i in range(1,len(f)-1):
        
        if f[i] == ' ':
            #Todo primeiro caracter de cada palavra integra o acrônimo
            acro += f[i+1]
    return acro

a = "table Lookaside buffer"
print(acronimo(a))