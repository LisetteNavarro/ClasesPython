import random
import csv
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez' , 'Isabel Gómez','Francisco Díaz”,”Elena Fernández']
sueldos=[]
lista=[]

def sueldo_aleatorio():
    
    lista2=[]
    for lista2 in trabajadores:
        sueldos=random.randint(300000,2500000)
        lista.append((trabajadores,sueldos))
        return lista
    
def clasificar_sueldos():
    sorted(trabajadores)
    return
        
def ver_estadisticas():
    return
        
def reporte_sueldos():       
    return
    
def salida_programa():
    print(" Finalizando programa...") 
    print(" Desarrollador: Lisette Navarro")
    print(" Rut: 21.836.684-8")
    return

print("=======================================")
print("INGRESE LA OPCION QUE DESEA EJECUTAR:\n=======================================")   
while True:
    print("1) Asignar sueldo aleatorio")
    print("2) Clasificar sueldos")
    print("3) Ver estadisticas")
    print("4) Reporte de sueldos")
    print("5) Salir del programa")
    try:
        op=int(input("\n=>"))

    except ValueError:
        print("Solo se pueden ingresar valores numericos del 1 al 5")
        break
    
    match op:
        case 1:
            print("Funcion no disponible, intentelo mas tarde..")
        case 2:
            print("En mantenimiento, intentelo mas tarde.")
        case 3:
            print("Estamos arreglando errores, intentelo mas tarde..")
        case 4:
            print("Arreglando errores, intentelo mas tarde..")
        case 5:
            print("")
            salida_programa()
            break
        