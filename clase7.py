
# Strings


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#METODO UPPER

#cadena1 = 'soY la pRimer cadena'
#print(cadena1)
#cadena1_en_mayusculas = cadena1.upper()
# cadena1 = cadena1.upper()
# print(cadena1)
#print(cadena1_en_mayusculas)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#METODO LOWER

#cadena1 = 'soY la pRimer cadena'
#cadena1_en_minusculas = cadena1.lower()
#print(cadena1)
#print(cadena1_en_minusculas)

#------------------------------------------------------------------------
#--------------------------------------------------------------------------
# METODO CAPITALIZE

#cadena1 = 'soY la pRimer cadena'
#cadena1_capitaliciada = cadena1.capitalize()
#print(cadena1)
#print(cadena1_capitaliciada)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#METODO TITLE

#cadena1 = 'soY la pRimer cadena'
#cadena1_titleada = cadena1.title()
#print(cadena1)
#print(cadena1_titleada)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#METODO COUNT

#cadena1 = 'soY la pRimer cadena'
#cadena1 = 'soY la pRimeroY cadenaoY  oY'
#print(cadena1.count('oy'))
#print(cadena1.count('oY'))
# print(cadena1.count('a'))
# print(cadena1.count('a', 2))
# print(cadena1.count('a', 7))
# print(cadena1.count('a', 2, 16))

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#METODO FIND
#permite buscar 1 aparecion de pedazo de str en el string y indica su indice

#cadena1 = 'soY la pRimer oY cadena'
#print(cadena1.find('oy')) # aca resultado sea -1 , significa que no se encontro
#print(cadena1.find('oY'))
#print(cadena1.find('oY', 2)) # aranca de pocision 2
#print(cadena1.find('oY', 2, 14)) # aranca de pocision 2 y ternina en posicion 14
#print(cadena1.find('oY', 2, 15))


#r.find me permite buscar de izquierda a la derecha

#cadena1 = 'soY la pRimer oY cadena'
#print(cadena1.rfind('oy'))
#print(cadena1.rfind('oY'))
#print(cadena1.rfind('oY', 1, 4))

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#Método SPLIT abd JOINT

#cadena2 = 'segunda cadena al rescate'
#print(list(cadena2))


#cadena2 = 'segunda cadena al rescate'
#cadena2_spliteada = cadena2.split()
#cadena2_spliteada = cadena2.split('cadena')
#cadena2_spliteada = cadena2.split('cadena1')
#cadena2_spliteada = cadena2.split('a ')
#cadena2_spliteada = cadena2.split('a')
#print(cadena2)
#print(cadena2_spliteada)


#cadena2 = 'segunda cadena al rescate'
#cadena2_spliteada = cadena2.split()
#print(cadena2)
#print(cadena2_spliteada)
#print(''.join(cadena2_spliteada))

#print('a'.join(cadena2_spliteada))
#print(' '.join(cadena2_spliteada))
# print(''.join(cadena2_spliteada))
# print('-------'.join(cadena2_spliteada))

#----------------------------------------------------------------------------
#---------------------------------------------------------------------------

# Método STRIP
#nos permite sacar parte adelante y parte atras

#password = input('Ingrese un password: ')
#print(password.strip())
#print(password)


#print(password.strip('tor'))
# password.strip()
#print(password)
#print('..dsapepea.sd'.strip('asd'))

#----------------------------------------------------------------------------
#--------------------------------------------------------------------------

#METODO REPLACE

#palabra_repetida = 'cadena cadena cadena cadena cadena'
#palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
#print(palabra_repetida)
#print(palabra_repetida_modificada)
#print(palabra_repetida.replace('cadena', 'otra', 3)) # 3 candidad de palabras para remplazar

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#LISTAS

#Método CLEAR nos permite vaciar la lista que quieremos

#lista1 = ['primera', 'lista', 1]
#lista2 = ['segunda', 'lista', 2]
#lista1 = []
#lista2.clear()
#print(lista1)
#print(lista2)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#Método EXTEND

#lista1 = ['primera', 'lista', 1]
#lista2 = ['segunda', 'lista', 2]
#lista1 += lista2
#print(lista1)

#lista1 = ['primera', 'lista', 1]
#lista2 = ['segunda', 'lista', 2]
#lista1.extend(lista2)
#print(lista1)

#lista1 = ['primera', 'lista', 1]
#lista2 = ['segunda', 'lista', 2]
#lista1 += lista2
#print(lista1)
#lista1.extend(lista2)
# # lista1.extend('otro')
#print(lista1)


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Método INSERT agaramos una lista y metemos informacion en lugar especifico

#lista2 = ['segunda', 'lista', 2]
#dicc = {
#    'llave': 'valor'
# }
#print(lista2)
#lista2.insert(1, dicc)
#print(lista2)

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#Método REVERSE

#lista2 = ['segunda', 'lista', 2]
#print(lista2)
#lista2 = lista2[::-1]
#print(lista2)

#=


#lista2 = ['segunda', 'lista', 2]
#print(lista2)
#lista2.reverse()
#print(lista2)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#Método SORT nos permite ordenar la lista

#lista_numeros = [5,1,2,3,4,10]
#lista_numeros.sort()
#print(lista_numeros)

#lista_numeros = [5,1,2,3,4,10]
#lista_numeros.sort(reverse=True) # para modificar lista al reverse
#print(lista_numeros)



# [].sort()
#lista_numeros1 = ['5','1','2','3','4','10'] #aca numeros en strings
#lista_numeros1.sort()
#lista_numeros1.sort(reverse=True)
#print(lista_numeros1)

#Ejercicio - colecciones 1

#Utilizando todo lo que sabes sobre cadenas, listas y
#sus métodos internos, transforma este texto:

#texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

#En este:

#Gordon lanzó su curva...
#- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
#- Dos pies -le corrigió Troop.
#- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

#texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'
#lista= texto.split('&')
#print(lista)
#lista[0] += '..' 
#lista2=[]

#print(lista)
#for oracion in lista:
#    lista2.append(oracion[0].upper() + oracion[1:])
#texto2 = '.\n- '.join(lista2)
#texto2 += '.'
#print(texto2)

# =


texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'
texto=texto.replace('&','\n')
#print(texto)


  