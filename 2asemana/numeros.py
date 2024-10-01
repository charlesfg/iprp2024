print(4.3 + 2.4)


Chama-se ano bissexto o ano ao qual é acrescentado um dia extra. Esse ano ocorre a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

def e_ano_bissexto(ano):
    return (ano % 4 == 0 and ano % (100 * 4) == 0 ) or ano % 400 == 0