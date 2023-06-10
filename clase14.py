#V1
#class Perro:
#    def tipo_animal(self):
#     print(f'Yo soy un', type(self).__name__)
#    def hablar(self):
#         print('Guau guau!!')
         
         
#class Gato:
#    def tipo_animal(self):
#     print(f'Yo soy un', type(self).__name__)    
#    def hablar(self):
#        print('Miau miau!!') 
         
#gato = Gato()
#perro = Perro()   

#perro.tipo_animal()
#perro.hablar()

#gato.tipo_animal()
#gato.hablar()

#-------------
# V2 
#class Animal:
#    def tipo_animal(self):
#     print(f'Yo soy un', type(self).__name__)

#class Perro(Animal): # aca Animal es clase padre
#    def hablar(self):
#         print('Guau guau!!')
         
         
#class Gato (Animal):
#    def hablar(self):
#        print('Miau miau!!') 
    
#perro = Perro()      
#gato = Gato()

#perro.tipo_animal()
#perro.hablar()

#gato.tipo_animal()
#gato.hablar()
   
# V3
   
   
#class Animal:
#    def tipo_animal(self):
#     print(f'Yo soy un', type(self).__name__)

#class Perro(Animal): # aca Animal es clase padre
#    def hablar(self):
#         print('Guau guau!!')
         
         
#class Gato (Animal):
#    def hablar(self):
#        print('Miau miau!!') 

#class Abeja(Animal):
#    ... #me permita crear un clase vacia pero hereida del padre
    
#perro = Perro()      
#gato = Gato()
#abeja = Abeja() 

#perro.tipo_animal()
#perro.hablar()

#gato.tipo_animal()
#gato.hablar()

#abeja.tipo_animal()


#------------------------------------------------------------------
#  Ej 2
#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#  ...    
    
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('Bermuda')
#print(lancha.descripcion())

#moto = Moto('Yamaha')
#print(moto.descripcion())    
 
 
 ##V1   
#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#   def __init__(self, tipo_ancla, marca): ##
#        self.tipo_ancla = tipo_ancla   ##
#        self.marca = marca
        
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('sin sepo', 'Bermuda')
#print(lancha.descripcion()) 
#print(lancha.tipo_ancla) ##

#moto = Moto('Yamaha')
#print(moto.descripcion())     
    
## Ej 2.1
  
#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#   def __init__(self, tipo_ancla, marca): ##
#        self.tipo_ancla = tipo_ancla   ##
#        self.marca = marca
        
#   def descripcion(self):
#       print (f'{type(self).__name__} marca: {self.marca}. Ancla {self.tipo_ancla}')       
        
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('sin sepo', 'Bermuda')
#lancha.descripcion()
#print(lancha.tipo_ancla) ##

#moto = Moto('Yamaha')
#print(moto.descripcion())    
  
  ##V2 

#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#   def __init__(self, tipo_ancla, marca): 
#        super().__init__ (marca)   ## me permite llamar el padre
#        self.tipo_ancla = tipo_ancla
        
#   def descripcion(self):
#       print (f'{type(self).__name__} marca: {self.marca}. Ancla {self.tipo_ancla}')       
        
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('sin sepo', 'Bermuda')
#lancha.descripcion()
#print(lancha.tipo_ancla)

#moto = Moto('Yamaha')
#print(moto.descripcion())      

   ## V3 
#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#   def __init__(self, tipo_ancla, marca):##
#        super().__init__ (marca)   ## me permite llamar el padre
#        self.tipo_ancla = tipo_ancla
        
#   def descripcion(self):
#       return super().descripcion() + f'. Ancla {self.tipo_ancla}' ##      
        
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('sin sepo', 'Bermuda')
#print(lancha.descripcion())

#moto = Moto('Yamaha')
#print(moto.descripcion())    

    
 ##V3   

#class Vehiculo:
#    def __init__(self, marca):
#        self.marca = marca
        
#    def descripcion(self):
#       return f'{type(self).__name__} marca: {self.marca}'

#class Auto(Vehiculo):
#    ...
        
#class Lancha(Vehiculo):
#   def __init__(self, tipo_ancla, *args, **kwargs):##
#        super().__init__ (*args, **kwargs)  ##
#        self.tipo_ancla = tipo_ancla
        
#   def descripcion(self):
#       return super().descripcion() + f'. Ancla {self.tipo_ancla}' ##      
        
#class Moto(Vehiculo):
#    ...
       
#auto = Auto('Ford')
#print(auto.descripcion())

#lancha = Lancha('sin sepo', 'Bermuda')
#print(lancha.descripcion())

#moto = Moto('Yamaha')
#print(moto.descripcion()) 

#--------------------------------------------------------------------------
# Ej 3


#class Animal:
#    def tipo_animal(self):
#         print(f'Yo soy un', type(self).__name__)
         
#class Terrestre(Animal):   
#    def caminar(self):
#        print(f'{type(self).__name__} esta caminando')
    
#class Acuatico (Animal):   
#    def nadar (self):
#        print(f'{type(self).__name__} esta nadando')        

#class Perro(Terrestre): 
#   def hablar(self):
#        print('Guau guau!!')        
 
#class Delfin (Acuatico):
#    ...

#class Pato(Acuatico, Terrestre):
#    def hablar(self):
#        print('Cuak cuak!!')


#perro = Perro()
#perro.caminar()
#perro.hablar()
#perro.tipo_animal()
#print('#################################')
#delfin = Delfin()
#delfin.nadar()
#delfin.tipo_animal()
#print('#################################')
#pato = Pato()
#pato.caminar()
#pato.nadar()
#pato.hablar()
#pato.tipo_animal()


#class Animal:
#    def tipo_animal(self):
#         print(f'Yo soy un', type(self).__name__)
         
#class AnimalTerrestre(Animal):   
#    def caminar(self):
#        print(f'{type(self).__name__} esta caminando')
    
#    def tiene_cola(self):
#        print('Soy terrestre y no tengo cola')  
    
#class AnimalAcuatico (Animal):   
#    def nadar (self):
#        print(f'{type(self).__name__} esta nadando')  
         
#    def tiene_cola(self):
#        print('Soy acuatico y no tengo cola')          

#class Perro(AnimalTerrestre): 
#   def hablar(self):
#        print('Guau guau!!')
          
 
#class Delfin (AnimalAcuatico):
    ##def nadar (self):
    ##    print('Hola soy un defin nadando')
#    ...

#class Pato(AnimalAcuatico, AnimalTerrestre):
#    def hablar(self):
#        print('Cuak cuak!!')


#perro = Perro()
#perro.caminar()
#perro.hablar()
#perro.tipo_animal()
#print('#################################')
#delfin = Delfin()
#delfin.nadar()
#delfin.tipo_animal()
#print('#################################')
#pato = Pato()
#pato.caminar()
#pato.nadar()
#pato.hablar()
#pato.tiene_cola()
##print(Pato.__mro__)



class Animal:
    def tipo_animal(self):
         print(f'Yo soy un {type(self).__name__}') 
         
    def hablar(self):
        print('Animal hablando')
         
class AnimalTerrestre(Animal):   
    def caminar(self):
        print(f'{type(self).__name__} esta caminando')
    
    def tiene_cola(self):
        print('Soy terrestre y no tengo cola')  
    
class AnimalAcuatico (Animal):   
    def nadar (self):
        print(f'{type(self).__name__} esta nadando')  
         
    def tiene_cola(self):
        print('Soy acuatico y no tengo cola')          

class Perro(AnimalTerrestre): 
   def hablar(self):
        print('Guau guau!!')
          
 
class Delfin (AnimalAcuatico):
    #def nadar (self):
    #    print('Hola soy un defin nadando')
    ...

class Pato(AnimalAcuatico, AnimalTerrestre):
    def hablar(self):
        print('Cuak cuak!!')

#perro = Perro()
#perro.caminar()
#perro.hablar()
#perro.tipo_animal()
#print('#################################')
#delfin = Delfin()
#delfin.nadar()
#delfin.tipo_animal()
#print('#################################')
#pato = Pato()
#pato.caminar()
#pato.nadar()
#pato.hablar()
#pato.tiene_cola()

#lista_de_animales1 = [Pato(), Perro(), Delfin(), Pato(), Perro(), Perro(), Delfin()]

#for animal in lista_de_animales1:
#    animal.tipo_animal()


#lista_de_animales2 = [Pato(), Perro(), Pato(), Perro(), Perro()]
#for animal in lista_de_animales2:
#    animal.hablar()


#def llama_hablar(x):
#    x.hablar()




