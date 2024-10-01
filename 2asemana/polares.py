import math

def cartesianas_polares(x,y):
    """
    Converte coordenadas cartesianas em polares.
    Atenção ao uso de atan2 para dar o valor certo para todos
    os quadrantes.
    """
    r = math.sqrt(x**2+y**2)
    theta = math.atan(y/x)
    return (r,theta)


a = cartesianas_polares(10, 120)

print(a)
