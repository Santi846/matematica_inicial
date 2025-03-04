
# Un conjunto de elementos, es una agrupacion de elementos de un tipo, o agrupados por alguna categoria => Comprensión

# ******TIPOS**********

# Conjunto verduras
# cada elemento, es la => Extensión
conjuntoVerduras = ["apple", "banana", "cherry"]

# Conjunto numerico
conjuntoNumerico = [1, 2, 3]

# Conjuntos vacios => van con {} en papel
conjuntoVacio = []

# Conjuntos unitarios => de un unico elemento
conjuntoCuantosComoYoHay = ["SantiagoArochaPerez"]

# Conjuntos universales => todos los elementos de un contexto, componen el conjunto
conjuntoTodos = ["atomos"]

# ******RELACIONES**********

# Subconjuntos
conjuntoOriginal = [1, 2, 3, 4, 5]

conjuntoSubConjunto = [1,2]
# => conjuntoSubConjunto es subconjunto => C (nomeclatura) de conjuntoOriginal

# Igualdad => cuando todos los elementos del primer conjunto, coinciden con los elementos del segundo conjunto
conjuntoA = [5, 4, 0]   
conjuntoB = [5, 4, 0]

# Conjunto Potencia
conjuntoOriginal2 = [1,2,3,4,5,6]

conjuntoPotencia = [
    {"vacio"},
    {1},
    {2},
    {3},
    {4},
    {5},
    {6},
    # + la combinacion de cada uno posible
    ]

# ******OPERACIONES**********

#Union
conjuntoUnionA = [1,2,3]
conjuntoUnionB = [4,5]
conjuntoUnionAyB = [1,2,3,4,5]

# Interseccion

conjuntoInterseccionA = [1,2,3]
conjuntoInterseccionB = [3,4,5]
conjuntoInterseccionAyB = [3]

# Diferencia Simetrica

conjuntoDiferenciaSimetricaA = [1,2,3]
conjuntoDiferenciaSimetricaB = [3,4,5]
conjuntoDiferenciaSimetricaAyB = [1,2,4,5]

# Complemento

conjuntoComplementoOriginalUniversal = [1,2,3,4,5]
conjuntoComplementoA = [1,2]
#Los que no estan en A, que llenan el conjunto universal del contexto
conjuntoComplementodeA = [3,4,5]

# ******COMBINATORIA**********

"""PERMUTACIONES"""
# Cuantas formas, de ordenar los elementos, tiene un conjunto
# => Va de la mano de Factorial
conjuntoBase = ["ABC"]
conjuntoPermutaciones = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"] # cantidad => 6 combinaciones

# Ejemplo Matemático
formulaPermutaciones = "P(n)=n!"

def P(n):
  result_P = n*2*1
  print(result_P)
# EXEC
P(3)


"""PERMUTACIONES (Con repeticion)"""
# Cuantas formas, de ordenar los elementos, tiene un conjunto, con elementos repetidos
# => Va de la mano de Factorial
conjuntoBaseRepeticion = ["AAB"]
conjuntoPermutacionesRepeticion = ["AAB", "ABA", "BAA"] # cantidad => 3 combinaciones

# Ejemplo Matemático
formulaPermutacionesRepeticion = "P(n;a,b,c,...) = n! / (a!×b!×c!...)"

def P_cr(n ,a, b ):
  dividendo = n*2*1
  divisor = a*b
  print(dividendo/divisor)
# EXEC
P_cr(3, 2, 1)

"""COMBINACIONES"""
# Formas de seleccionar elementos de un conjunto
conjuntoCombinacionesOriginal = [5,2]
conjuntoCombinacionesTotal = 10

# Ejemplo Matemático
formulaCombinaciones = "C(n,k)= n! / (k!(n-k)!)"

def C(n ,k ):
  result_n = n*4*3*2*1
  result_k = k*1*(n-k)*2*1
  print(result_n/result_k)
# EXEC
C(5, 2)

"""VARIACIONES"""
# Formas de seleccionar elementos de un conjunto, considerando el ORDEN
formulaVariaciones = "V(n,k)= n! / (n-k)!"

def V(n ,k ):
  result_n = n*4*3*2*1
  result_k = (n-k)*2*1
  print(result_n/result_k)
# EXEC
V(5, 2)