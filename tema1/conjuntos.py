
# Un conjunto de elementos, es una agrupacion de elementos de un tipo, o agrupados por alguna categoria

# ******TIPOS**********

# Conjunto verduras
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

conjuntoComplementoUniversal = [1,2,3,4,5]
conjuntoComplementoA = [1,2]
conjuntoComplementodeA = [3,4,5]

# ******COMBINATORIA**********

"""PERMUTACIONES"""
# Cuantas formas, de ordenar los elementos, tiene un conjunto
# => Va de la mano de Factorial
conjuntoBase = ["ABC"]
conjuntoPermutaciones = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"] # cantidad => 6 combinaciones
