from cargarInventario import getCargarInicial
from cargarInstrucciones import getCargarInstrucciones
from crearInventario import setInventario

def getOpciones():
    print("Ingrese una opcion:")
    opcion=int(input())
    if((opcion<1)or(opcion>5)):
        print("El numero de opcion no esta disponible")
    elif(opcion==1):
       getCargarInicial()
    elif(opcion==2):
       getCargarInstrucciones()
    elif(opcion==3):
       setInventario()
    elif(opcion==4):
       quit()
