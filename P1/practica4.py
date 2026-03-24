#-------------------------------------------------------------------------#
# Crear una tupla con 3 elementos: 10, "Hola" y 3.14
tupla = (10, "Hola", 3.14)
print(tupla)

#-------------------------------------------------------------------------#
# La tupla(1,2,3,4,5), accede y escribe el tercer elemento
tupla = (1, 2, 3, 4, 5)
# Los índices empiezan en 0, así que el tercer elemento es el índice 2
print(tupla[2])
#-------------------------------------------------------------------------#
# Concatena las tuplas y almacena el resultado en una tupla Nueva
t1 = (1, 2)
t2 = (3, 4)
tupla_final = t1 + t2
print(tupla_final)
#-------------------------------------------------------------------------#
# Desempaqueta la tupla en tres variables y escribe sus valores
tupla = ('mamut', 'hamster', 'jabali')
var1, var2, var3 = tupla
print(var1, var2, var3)

#-------------------------------------------------------------------------#
# Verifica si el elemento 7 existe en la tupla (1,3,5,7,9)
tupla = (1, 3, 5, 7, 9)
existe = 7 in tupla
print(existe)

#-------------------------------------------------------------------------#
# Crea una tupla (0,1,2,3,4,5) y escribe los elementos del índice 2 a 4 con slice
tupla = (0, 1, 2, 3, 4, 5)
# El slice [2:5] toma desde el índice 2 hasta el anterior al 5 (es decir, el 4)
resultado = tupla[2:5]
print(resultado)

#-------------------------------------------------- -----------------------#
# Encuentra la longitud de una tupla (10,20,30,40,50)
tupla = (10, 20, 30, 40, 50)
length = len(tupla)
print(length)

#-------------------------------------------------------------------------#
# Crea una tupla y repítela 3 veces
tupla_original = (1, 2, 3)
resultado = tupla_original * 3
print(resultado)

#-------------------------------------------------------------------------#
# Convierte la lista [1,2,3] a tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)

#-------------------------------------------------------------------------#
# Encuentra los valores mínimo y máximo de la tupla (5,12,3,8,15)
tupla = (5, 12, 3, 8, 15)
valor_minimo = min(tupla)
valor_maximo = max(tupla)
print('Minimo: ', valor_minimo, ' Maximo: ', valor_maximo)