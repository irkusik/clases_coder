
import sys




#print(sys.argv)
#print (type(sys.argv))

#print('Ahi te va de que grupo sos!')
#nombre = sys.argv[1]
#preferencia = sys.argv[2]

#if (preferencia =='marvel' and nombre < 'm') or (preferencia=='capcom' and nombre>'n'):
#    print('Sos de grupo A !')
#else:
#    print('Sos de grupo B!')


#print(sys.argv)


#################################################
 # # # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase

#import clase14 
#perro = clase14.Perro()
#perro.hablar()
#clase14.llama_hablar(perro)
##################################################
 # # # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase

#from clase14  import Perro, llama_hablar
#perro = Perro()
#perro.caminar()
#llama_hablar(perro)
##################################################
# # # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase

#from clase14 import *
#perro = Perro()
#perro.caminar()
#llama_hablar(perro)
##################################################
# # # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase

#from clase14  import Perro as PerritoLoco, llama_hablar as llama_hablar14

#def llama_hablar():
#    print('Mira lo que hago!!!')    
    
#perro = PerritoLoco()
#perro.caminar()
#llama_hablar14(perro)
##################################################
# vamos a llamar de parte pel mi_paquete

#from mi_paquete import funciones
from mi_paquete.funciones import llama_hablar as llama_hablar_funciones
from mi_paquete.clases import Perro as PerritoLoco
    
perro = PerritoLoco()
perro.caminar()

llama_hablar_funciones(perro)

def llama_hablar():
    print('Mira lo que hago!!!') 
    
llama_hablar_funciones(perro)  


##################################################################