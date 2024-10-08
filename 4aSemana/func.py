import math

def raizes(a,b,c):
	""" 
       Calcula as raízes de um polinómio do segundo grau.

	"""
	comum = math.sqrt( b**2 - 4 * a * c)
	raiz1= (-b + comum)/ (2 * a)
	raiz2= (-b - comum)/ (2 * a)
	return raiz1, raiz2

print(raizes(2, 5, 1))