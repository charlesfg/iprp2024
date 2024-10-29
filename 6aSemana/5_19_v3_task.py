import turtle
import random
import time



def grade(t, d, c):
    """
    Método que desenha a grade na Tela

    t : um objeto turtle,  que irá desenhar
    d : inteiro, dimensão da grade (número de células por linha x coluna)
    c : inteiro, tamanho da célula da grade
    """

    pass


def gera_local_aleatorio(d, c, lb_coord):
    """
    Método que retorna um ponto aleatório de uma dada grade de 
    dimensão d e célula de tamanho c

    d : inteiro, dimensão da grade (número de células por linha x coluna)
    c : inteiro, tamanho da célula da grade
    lb_coord: tupla (x, y) coordenadas x e y cando inferior esquerdo da grade
    return:  tupla (x, y) coordenadas aleatórias x e y
    """
    return (0,0)


def move_turtle(t, dest, c, pos):
    """
    Atualiza o desenho movendo o turtle para a direção indicada
    t : um objeto turtle,  que irá desenhar
    dest : string, direção para mover o turtle ('N','S','L' ou 'O')
    c : inteiro, tamanho da célula para movimentação
    pos: tupla (x, y) coordenadas x e y do objeto que se move na grade
    return (x,y) : tupla, a nova posição no tabuleiro
    """
    return (0,0)

def movimento_valido(dest, pos, lb_coord, rt_coord):
    """
    Método que retorna True or False após avaliar se um movimento
    para o destino `dest` é válido ou não 
    

    dest : string, direção para mover o turtle ('N','S','L' ou 'O')
    pos: tupla (x, y) coordenadas x e y do objeto que se move na grade
    lb_coord: tupla (x, y) coordenadas x e y cando inferior esquerdo da grade
    lb_coord: tupla (x, y) coordenadas x e y cando superior direito da grade
    return: boolean 
    """

    return False
    
def square(t, l, x, y):
    """
    Desenha um quadrado de lado l à partir do ponto x,y
    t : um objeto turtle,  que irá desenhar
    l : inteiro, lado do quadrado (
    x : inteiro, coordenada x
    y : inteiro, coordenada y
    """

    pass
    


def game(t, d, c, steps=None):
    """
    Método para inicializar o jogo em uma grade de dimensão d x d 
    e célula de lado c

    t : um objeto turtle,  que irá desenhar
    d : inteiro, dimensão da grade (número de células por linha x coluna)
    c : inteiro, tamanho da célula da grade
    steps: inteiro, número máximo de passos que o jogo deverá fazer (se None, sem limite de passos)
    """

    # Ajusta a posição inicial do turtle
    t.teleport(-(d*c//2), -(d*c//2))
    
    t.color("light gray")

    # Posição inicial, nosso referencial, canto inferior esquerdo
    lim_lb = t.pos()
    # canto inferior direito?
    lim_ru = (0,0)              # TODO definir <-----

    # Desenho a grade
    grade(t, d, c)

    # Escolha um inicio aleatório
    start_x, start_y = 0, 0     # TODO definir <-----

    # Escolha um final aleatório
    end_x , end_y = 0, 0        # TODO definir <-----

    
    t.teleport( end_x, end_y)
    t.color("green")
    t.shape("square")
    t.shapesize(0.3,0.3)
    t.stamp()

    t.shapesize(0.5,0.5)
    t.shape("triangle")

    
    t.teleport(start_x, start_y)
    t.color("red")
    t.dot(5)

    x = start_x
    y = start_y

    s = 0

    while not (x == end_x and y == end_y):

        # Escolhendo o movimento ...
        m = random.choice(['N','S','L','O'])
        

        if movimento_valido(m, (x,y), lim_lb, lim_ru):
            x, y = move_turtle(t, m, c, (x, y))
        else:
            print(f"Movimento Proibido ({m}): ", x,  y, end_x, end_y)
            continue
        s+=1
        if (s == steps):
            break
    
    if not steps or s < steps:
        print(f"Fim para a dimensão {d}, Número de Passos: {s}!")
    else:
        print(f"Desistindo após {s} passos... Objetivo não alcançado!")
    
    pass


if __name__ == "__main__":

    t = turtle.Turtle()
    t.speed(9)

    for i in range(1, 6):
        t.teleport(0,0)
        t.setheading(0)
        game(t, i, 20, 300)
        time.sleep(2)
        
        t.clear()

    turtle.exitonclick()