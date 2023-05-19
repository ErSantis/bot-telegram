import numpy as np
from IPython.display import display, Math
from fractions import Fraction
from sympy import Poly
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from .rr import solve_homogenea

def get_gn(recurrence,k):

  #Arguments -> recurrence,k : funcion de recurrencia,grado
  #Returns -> g(n)

  recurrence = recurrence.replace(' ','')
  for x in range(1,k+1):
      if f'f(n-{x})' in recurrence:
        a = recurrence.index(f'{x})')
        recurrence = recurrence[a+2:]
  n = sp.Symbol('n')
  exp = parse_expr(recurrence)
  return exp

#Evaluar en caso se encuentra g(n)
def open_cases(gn,recurrence,k,cond):

  #Arguments -> gn,recurrence,k : g(n), funcion de recurrencia, grado
  
  f_fp = recurrence
  try: #Intenta convertir g(n) a un polinomio
    pol = sp.Poly(gn)
    
    #Evalua el grado g_n
    if pol.degree() == 1:
      
      #Comprueba si g_n tiene la forma a^n
      if '**' in f'{gn}':
        print('Caso g(n) = a^n')
      
        ind = f'{gn}'.index('n')
        new = f'{gn}'[:ind]+'('+ f'{gn}'[ind:] +')'
  
        #Remplazar C*g(n) donde aparazeca f(n-i)
        for i in range(1,k+1):  
          if f'f(n-{i})' in recurrence:
            f_fp = f_fp.replace(f'f(n-{i})','*C*'+new.replace('n',f'n-{i}'))
        f_fp = sp.simplify(parse_expr(f_fp)) #Lo convierte en expresion matematica.
        
        #Reduce la ecucion y halla los valores de C
        n,C = sp.symbols('n C')
        aux = str(gn)
        number =int(aux[:aux.index("**")-1].replace('(', '').replace(')', ''))
        eq = sp.Eq(C*number**n, f_fp)
        sol = sp.solve(eq, C)
        
        #Crea la fp con los valores de C
        fp = C*number**n
        fp = fp.subs(C, sol[0])
        
        #Arma la fh quitando de la RR la fp
        terms = pol.terms()
        #Revisa si el primer termino de g(n) es '-', si lo es quita de la funcion, si es '+' entoces quita el gn y el signo '+' que le antecede
        fh = recurrence.replace(' ','').replace(f'{gn}','') if int(terms[0][1]) <0 else recurrence.replace(' ','').replace(f'+{gn}','') 
  
        #Resolver la no homogenea
        return solve_homogenea(k,fh,cond,fp)
      
      #g(n) = n
      else:
        print('Caso g(n) = n')

        #Remplazar An + B donde aparazeca f(n-i)
        for i in range(1,k+1):
          if f'f(n-{i})' in recurrence:
            f_fp = f_fp.replace(f'f(n-{i})',f'*(A*(n-{i})+B)')
        print(f_fp)
        f_fp = sp.simplify(parse_expr(f_fp)) #Lo convierte en expresion matematica.
        print(f_fp)
        #Reduce la ecucion y halla los valores de A y B
        A,B,n = sp.symbols('A B n')
        eq = sp.Eq(A*n + B, f_fp)
        sol = sp.solve(eq, (A, B))
        print(sol)
        #Crea la fp con los valores de A y B
        fp = A*n + B
        fp = fp.subs(A, sol[A])
        fp = fp.subs(B, sol[B])
      
        #Arma la fh quitando de la RR la fp
        terms = pol.terms()
        #Revisa si el primer termino de g(n) es '-', si lo es quita de la funcion, si es '+' entoces quita el gn y el signo '+' que le antecede
        fh = recurrence.replace(' ','').replace(f'{gn}','') if int(terms[0][1]) <0 else recurrence.replace(' ','').replace(f'+{gn}','') 
        print(fh,fp)
        #Resolver la no homogenea
        return solve_homogenea(k,fh,cond,fp)
        

    ## Caso g(n) = n^2
    if pol.degree() == 2:
      #Remplazar An^2 + Bn + C donde aparazeca f(n-i)
      for i in range(1,k+1):
        if f'f(n-{i})' in recurrence:
          f_fp = f_fp.replace(f'f(n-{i})',f'*(A*(n-{i})**2+B*(n-{i})+C)')
      print(f_fp)
      f_fp = sp.simplify(parse_expr(f_fp)) #Lo convierte en expresion matematica.
      print(f_fp)
      #Reduce la ecucion y halla los valores de A y B
      n, A, B, C = sp.symbols('n A B C')
      eq = sp.Eq(A*n**2 + B*n + C, f_fp)
      sol = sp.solve(eq, (A, B, C))
      print(sol)
      #Crea la fp con los valores de A y B y C
      fp = A*n**2 + B*n + C
      fp = fp.subs(A, sol[A])
      fp = fp.subs(B, sol[B])
      fp = fp.subs(C, sol[C])
      
      #Arma la fh quitando de la RR la fp
      terms = pol.terms()
      #Revisa si el primer termino de g(n) es '-', si lo es quita de la funcion, si es '+' entoces quita el gn y el signo '+' que le antecede
      fh = recurrence.replace(' ','').replace(f'{gn}','') if int(terms[0][1]) <0 else recurrence.replace(' ','').replace(f'+{gn}','') 
      #Resolver la no homogenea
      return solve_homogenea(k,fh,cond,fp)
      
  
  #Caso g(n):C
  except:
      #Remplazar C donde aparazeca f(n-i)
      for i in range(1,k+1):
        if f'f(n-{i})' in recurrence:
          f_fp = f_fp.replace(f'f(n-{i})',f'*C')
      f_fp = sp.simplify(parse_expr(f_fp)) #Lo convierte en expresion matematica.
      
      #Reduce la ecucion y halla los valores de A y B
      C = sp.symbols('C')
      eq = sp.Eq(C, f_fp)
      sol = sp.solve(eq, C)
      
      #Crea la fp con los valores de C
      fp = C
      fp = fp.subs(C, sol[0])
     
      #Revisa si el primer termino de g(n) es '-', si lo es quita de la funcion, si es '+' entoces quita el gn y el signo '+' que le antecede
      fh = recurrence.replace(' ','').replace(f'{gn}','') if gn < 0 else recurrence.replace(' ','').replace(f'+{gn}','') 
      #Resolver la no homogenea
      return solve_homogenea(k,fh,cond,fp)
