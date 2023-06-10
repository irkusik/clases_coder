# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/
# Slides

# Definiendo e instanciar una clase
'''
class Auto:
    ... # pass
    
auto1 = Auto()
auto2 = Auto()
'''

#def funcion():
 #   return 'valor'

#valor = funcion()
#print(valor)

# print(type(2))

#class ClaseAuto: # PascalCase
#   ... # pass
#auto1 = ClaseAuto()
#print(type(auto1))



#class ClaseAuto: # PascalCase
#   ... # pass
#auto1 = ClaseAuto()
#print(type(auto1))
#print(type(2))

#class ClaseAuto: # PascalCase
#  ... # pass
#auto1 = ClaseAuto()
#auto2 = ClaseAuto()
#print(type(2))
#print(type(auto1))
#print(type(auto2))

#print(auto1)
#print(auto2)

# Base sobre metodos

        
#class ClaseAuto: # PascalCase
            
#    def tocar_bocina(self):
#        print('Pi pi!!')  
#    def describir_auto(self):
#        return f'Este es un auto. {self}'



#class NombreClase:
#    def nobre_funcion(): # self siempre va como primer parametro 
#       ... #codigo
            
#class ClaseAuto: # PascalCase
            
#    def tocar_bocina(self):
#        print(f'Pi pi!!')  

#    def describir_auto(self):
#       #return f'Este es un auto.'
#        return f'Este es un auto. {self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()      
#print(auto1)
#print(auto2)
#auto1.tocar_bocina()
#auto2.tocar_bocina()
#print(auto2.describir_auto()) #describir_auto(auto2)


# self va a valer el objeto estoy valorando (aca auto1)

#class ClaseAuto: # PascalCase
            
#    def tocar_bocina(self):
#        print(f'Pi pi!!{self}')  

#    def describir_auto(self):
#       #return f'Este es un auto.'
#        return f'Este es un auto. {self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()      
#print(auto1)
#print(auto2)
#auto1.tocar_bocina()
#auto2.tocar_bocina()
##self va a valer auto1
#print(auto1.describir_auto()) #describir_auto(auto1)
##self va a valer auto2
#print(auto2.describir_auto()) #describir_auto(auto2)


# self va a valer el objeto estoy valorando (aca auto1)



# Atributos

# De clase
#class ClaseAuto: # PascalCase
      
#    tiene_velocimetro = True  # es atributo que tiene todo clase auto
            
#    def tocar_bocina(self):
#        print(f'Pi pi!!')  

#    def describir_auto(self):
#       #return f'Este es un auto.'
#        return f'Este es un auto. {self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()      
#auto1.tocar_bocina()
#auto2.tocar_bocina()
#print(auto1.describir_auto()) 
#print(auto2.describir_auto()) 
#print(auto1.tiene_velocimetro)
#print(auto2.tiene_velocimetro)



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#class ClaseAuto: # PascalCase
      
#    tiene_velocimetro = True 
    #def generar_color(self):
    ###def generar_color(self, color):
       # self.color = 'blanco'
       ## self.color = input('ingrese un color de auto:')
    ###   self.color = color
#    def tocar_bocina(self):
#        print(f'Pi pi!!')  

#    def describir_auto(self):
#        return f'Este es un auto. {self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()   
#auto1.generar_color()
###auto1.generar_color('negro')
#auto2.generar_color() 
###auto2.generar_color('blanco')   
#print(auto1.color)
#print(auto2.color)


#lass ClaseAuto: # PascalCase
      
#    tiene_velocimetro = True 
    
#    def generar_color(self, color):
#       self.color = color
       
#    def tocar_bocina(self):
#        print(f'Pi pi!!')  

#    def describir_auto(self):
#        return f'Este es un auto de color {self.color}.{self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()   
#auto1.generar_color('negro')
#print(auto1.describir_auto())
#print(auto2.describir_auto())

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# De instancia
#'''
#class Auto:
    
#    def __init__(self, modelo, marca):
#        self.modelo = modelo
#        self.marca = marca
#'''

#class FordK:
    
#    def __init__(self, color = 'blanco', puertas=2):
#        self.color = color
#        self.puertas = puertas

#auto1 = FordK('rojo', 5) # <<=== es como si tambien se ejecutase una linea asi auto1.__init__('rojo',5)
#auto1 = FordK(color = 'rojo', puertas = 5)
#print(auto1.color)
#print(auto1.puertas)

#auto2 = FordK()
#print(auto2.color)
#print(auto2.puertas)

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK('Rojo', 3)

# print(auto1)
# print(f'Color de auto1 {auto1.color}')
# print(f'Cant puertas {auto1.puertas}')
# print(auto2)
# print(f'Color de auto2 {auto2.color}')
# print(f'Cant puertas {auto2.puertas}')


#class FordK:
    
#    ruedas = 4
    
#    def __init__(self, color, puertas):
#        self.color = color
#        self.puertas = puertas
#        self.blindado = True
        # if self.color == 'Negro':
#         #     self.ruedas = 1
#        self.aviso_de_fabricacion()
        
#    def aviso_de_fabricacion(self):
#        print('Se fabrico un auto Ford K')
    
#    def tocar_bocina(self):
#        print('Pi pi!!')
    
#    def describir_auto(self):
#        self.tocar_bocina()
#        return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

#auto1 = FordK('Negro', 4)
#auto2 = FordK('Rojo', 2)

#print(auto1)
#print(auto2)
#print(f'Color {auto1.color}')
#print(f'Color {auto2.color}')
#print(auto1.describir_auto())
#print(auto2.describir_auto())



#'''
#============================================================================================
#============================================================================================
#'''

# Magic/Dunder Methods

#class FordK:
  
#    cant_ruedas = 4
    
#    def __init__(self, color='Verde', puertas=5):
#       self.color = color
#       self.puertas = puertas
#       self.radio = True
        
#    def tocar_bocina(self):
#      print('Pi pi!!')
    
#    def __str__(self):
#       return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'


#auto1 = FordK('Negro', 4)
#auto2 = FordK('Rojo', 2)
#auto3 = FordK(puertas=2)
#auto4 = FordK('Rojo')
#auto5 = FordK()


#class Concesionaria:
    
#    def __init__(self, nombre, autos_en_venta=[]):
#        self.nombre = nombre
#        self.autos_en_venta = autos_en_venta
        
#    def __str__(self):
#        return f'Esta es una concesionaria {self.nombre}.'
    
#    def __len__(self):
#        return len(self.autos_en_venta)
#    def __getitem__(self, ubicacion):
#        return self.autos_en_venta[ubicacion - 1]
    
#    def __setitem__(self, ubicacion,nuevo_dato):
#        self.autos_en_venta[ ubicacion -1 ] = nuevo_dato
#    def __iter__(self):
#        for auto in self.autos_en_venta:
#            yield auto
        
#concesionaria1 = Concesionaria('Grillo', [auto1, auto2])
#print(concesionaria1)
#print(len(concesionaria1))
#print(concesionaria1[1])
#concesionaria1[1] = auto5 
#print(concesionaria1[1])
#for elemento in concesionaria1:
#    print(elemento)
    
    


#'''
#============================================================================================
#============================================================================================
#'''
# Encapsulamiento

class Persona:
    
    def __init__(self, dni, color_de_pelo, cant_cirugias):
        self.__dni = dni #__ hacen que yo no puedo acceder a info desde afuera
        self.color_de_pelo = color_de_pelo
        self.__cant_cirugias = cant_cirugias
        
    def mostrar_dni(self):
       print(self.__dni)
        
    # getters
    def get_dni(self):
       return self.__dni
    
    # setters
    def set_dni(self, valor_nuevo):
      self.__dni = valor_nuevo
        

persona1 = Persona(123123, 'castanio', 5)
print(persona1.color_de_pelo)
persona1.color_de_pelo = 'canoso'
print(persona1.color_de_pelo)
#print(persona1.__dni) = 222 va a salir error , tenemos que usar set
persona1.set_dni(222)
persona1.mostrar_dni()




#print(persona1.color_de_pelo)

# persona1.__dni = 222
#persona1.set_dni(222)

# # print(persona1.__cant_cirugias)
# print(persona1.get_dni())
# # persona1.dni = 43434343
# # persona1.__dni = 43434343
# print(persona1.get_dni())
# # # print(persona1.__dni)
    
# print('================================================================================================================')
# print('================================================================================================================')
# print('================================================================================================================')
# print('================================================================================================================')
