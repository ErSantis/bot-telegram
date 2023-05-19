import numpy as np
from IPython.display import display, Math
from fractions import Fraction
from sympy import Poly
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

#Obtener el número que está antes del f(n-k)
def get_number(recurrence,index):
  
  #Arguments -> recurrence,index : funcion de recurrencia, indice donde se encuentra f(n-k)
  #Returns -> add : Number
  
  if recurrence[index] == "+":
        add = -1
  elif recurrence[index] == '-':
        add = 1
  elif recurrence[index-1] == ')':
      add =  -1*int(recurrence[index])
  else:
    add = int(recurrence[index]) * get_number(recurrence,index-1)
  return add
  
#Hallar los coeficientes del polinomio caracteristico
def find_coeff(recurrence,k):
  
  #Argument -> recurrence,k : funcion de recurrencia, grado.
  #Returm -> coeff : lisa de los coeficientes del polinio caracteristo.
  
  recurrence = recurrence.replace(' ','') #Quitar los espacios en blanco.
  coeff=[1] # Agregar el coeficinte de la f(n).
  for x in range(k):
      if f'f(n-{x+1})' in recurrence:
        coeff.append(get_number(recurrence,recurrence.index(f'f(n-{x+1})')-1))
      else:
        #Si no esxite un f(n-x) su coeficiente es 0.
        coeff.append(0)
  return coeff

#Encontrar las raices del polinomio caracteristico.
def find_roots(coeff):

  #Argument -> coeff : lista de coeficientes del polinomio caracteristico.
  #Returns -> d: diccionarios donde cada llave es una raiz del polinomio y su valor es su multiplicidad.

  roots =  np.around(np.roots(coeff))
  d = {}
  for i in roots:
    if i not in d:
      d[i] = np.count_nonzero(roots == i)
  return d

#Resolver la RRLHCCC
def solve_homogenea(k,funtion,cond,fp):
  #Resolver la RR
  mat = []
  roots = find_roots(find_coeff(funtion,k))
  # Iterar sobre el numero de condiciones inicales, estas seran el numero de ecuaciones.
  for c in range(len(cond)): 
    if fp != 0:
      n = sp.symbols('n')
      cond[c] = cond[c] - fp.subs(n, c)
    g = [] #Lista que almacena los coeficientes de las b_i
    for r in roots:
      for m in range(roots[r]):
        t = (r**c)*(c**m) #Coeficientes de las b_i segun la formula de RRLHCCC
        g.append(t)
    mat.append(g) #Lista que contendra las ecuaciones
  mat = np.array(mat)
  X = np.vectorize(lambda x: Fraction(x).limit_denominator())(np.linalg.inv(mat).dot(cond)) #Hallar los valores de b_i
  s = ''
  count = 0
  #Armar la funcion con los valores hallados
  for r in roots:
      for m in range(roots[r]):
        s = s + f'+{X[count]}*({int(r)})**n*(n**{m})'
        count += 1
  expr = sp.simplify(parse_expr(s)+fp) #Simplificar la expresion
  display(Math(sp.latex(expr)))
  return expr #Mostrar en formato LaTeX

def rrlhccc():
  #Pedir al usuario, la f(n), el grado y las condiciones iniciales.
  k = int(input('Ingrese el grado de la funcion de recurrencia '))
  funtion = input("Escribe la relación de recurrencia \nNO USES * PARA LA MULTIPLICACIÓN \nEjemplo: 2f(n-2) + f(n-1) \nf(n) = ")
  cond = np.array(list(map(float,input("Escribe las condiciones iniciales <f(0),f(1),...,> ").split(","))))
  solve_homogenea(k,funtion,cond,0)