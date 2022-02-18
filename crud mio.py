import os
#Funcion para ingresar alumnos.
def ingresar_nombreYnotas():
    while True:
        confirmacion=(input("Desea ingresar nombre y nota de un alumno?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            try:
                nota = float(input("Ingrese la nota del estudiante (0-10):"))
                if nota<=0 or nota>10:
                    print("La nota debe estar entre 0 y 10.")
                else:
                    lista_notas.append(nota)
                    nombre=(input("Ingrese el nombre del estudiante: ")).capitalize()
                    if nombre=="":
                        print("No ha ingresado un nombre.")
                    else:
                        lista_nombres.append(nombre)
                        nombreYnota[nombre]=nota
                        edad=int(input("Ingrese la edad del alumno: "))
                        lista_edades.append(edad)
                        print("El alumno ha sido registrado exitosamente!")
                        break
            except:
                print("la nota tiene que ser un valor numerico")
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break                
        else:
            print("No ha elegido opcion.")
#ingresar_nombreYnotas()
#Funcion para buscar alumno
def buscar_alumno():
    while True:
        confirmacion=(input("Desea buscar un alumno?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            alumno=(input("Ingrese el nombre del alumno que desea buscar: ")).capitalize()
            if alumno in nombreYnota:
                print("El alumno se encuentra en la lista.",alumno,"tiene la nota: ",nombreYnota[alumno])
                break
            elif alumno=="":
                print("No ha ingresado un nombre. Intentelo nuevamente.")
            else:
                print("El alumno no se encuentra en la lista.")
                print("Regresando al menu principal.")
                break
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
#buscar_alumno()
#Funcion para modificar nota
def modificar_nota():
    while True:
        confirmacion=(input("Desea modificar la nota de un alumno?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            alumno=(input("Ingrese el nombre del alumno: ")).capitalize()
            if alumno=="":
                print("No ha ingresado un nombre. Intentelo nuevamente.")
            elif alumno in lista_nombres and nombreYnota:
                print(f"{alumno} tiene la nota: {nombreYnota[alumno]}")
                try:
                    nueva_nota=float(input("Ingrese la nota por la que desea cambiar la anterior: "))
                    if 0<nueva_nota>10:
                        print("La nota debe ser mayor a cero e igual o menor que 10.")
                    else:
                        nombreYnota[alumno]=nueva_nota
                        print(f"La nota de {alumno} ha sido cambiada por: {nombreYnota[alumno]}")
                        for i in range(len(lista_nombres)):
                            indice=lista_nombres.index(alumno)
                            lista_notas[indice]=nueva_nota
                        break
                except:
                    print("No ha ingresado una nota. Intentelo nuevamente.")
            else:
                print("El alumno no se encuentra en la lista.")
                break
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.") 
#modificar_nota()
#Funcion para listar nombres de alumnos
def listar_nombres():
    while True:
        confirmacion=(input("Desea listar los nombres de los alumnos en orden alfabetico?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            if len(lista_nombres)==0:
                print("No hay cantidad de alumnos suficiente.")
            else:
                lista_nombres.sort()
                print(f"""La lista ordenada por orden alfabetico es: 
                {lista_nombres}""")
                break
        elif confirmacion=="No" or confirmacion=="N":
                print("Regresando al menu principal.")
                break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
    return listar_nombres
#listar_nombres()
#Funcion para listar notas de mayor a menor
def listar_notas():
    while True:
        confirmacion=(input("Desea ordenar las notas de mayor a menor?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            if len(lista_notas)==0:     
                print("No hay notas suficientes")
            else:
                lista_notas.sort()
                lista_notas.reverse()
                print(f"""Las notas ordenadas de mayor a menor son: 
                {lista_notas}""")
                break
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
    return listar_notas
#listar_notas()
#Funcion para mostrar promedio de las notas.
def promedio():
    while True:
        confirmacion=(input("Desea obtener el promedio de las notas de los alumnos?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            if len(lista_notas)==0:
                print("No hay notas suficientes para calcular el promedio.")
            else:
                prom=sum(lista_notas)//len(lista_notas)
                print(f"El promedio de las notas de los alumnos es: {prom}")
                break
        elif confirmacion=="No" or confirmacion=="N": 
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
    return promedio
#promedio()
#Funcion para borrar un estudiante
def borrar_estudiante():
    while True:
        confirmacion=(input("Desea borrar a un alumno del registro?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            borrar=(input("Ingrese el nombre del alumno que desea borrar del registro: ")).capitalize()
            if borrar=="":
                print("No ha ingresado un nombre. Intentelo nuevamente.")
            elif borrar in lista_nombres:
                confirmacion2=(input("Seguro que desea borrar a este alumno? El procedimiento es irreversible: ")).capitalize()
                if confirmacion2=="Si":
                    indice=lista_nombres.index(borrar)
                    lista_nombres.pop(indice)
                    lista_notas.pop(indice)
                    (nombreYnota).pop(borrar)
                    print("El alumno ha sido eliminado del registro exitosamente.")
                    break
                elif confirmacion2=="No":
                    print("Regresando al menu principal.")
                    break
                else:
            
                    print("No ha ingresado una opcion valida. Intentelo nuevamente.")
            else:
                print("El alumno no se encuentra en la lista.")
                break
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
#borrar_estudiante()
#Funcion para calcular promedio de edades.
def promedio_edades():
    while True:
        confirmacion=(input("Desea calcular el promedio de las edades?: ")).capitalize()
        if confirmacion=="Si" or confirmacion=="S":
            if len(lista_edades)==0:
                print("No hay alumnos suficientes para calcular el promedio de edades.")
            else:
                print(f"El promedio de las edades es: {sum(lista_edades)//len(lista_edades)}")
                break
        elif confirmacion=="No" or confirmacion=="N":
            print("Regresando al menu principal.")
            break
        else:
            print("No ha ingresado una opcion valida. Intentelo nuevamente.")
#promedio_edades()
#Funcion de menu
def menu():
    print("Bienvenido/a a la aplicacion de registro estudiantil.")
    print("""-------------------------------------------------------
    Selecciona una opción...
    1 - Agregar estudiante
    2 - Buscar estudiante por nombre
    3 - Modificar nota
    4 - Listado ordenados por nombres
    5 - Listado ordenados por notas
    6 - Mostrar promedio de las notas
    7 - Borrar un estudiante
    8 - Calcular la edad promedio de los estudiantes
    0 - Salir""")
##############################################################################################################################################
#PROGRAMA PRINCIPAL
lista_nombres=[]
lista_notas=[]
lista_edades=[]
nombreYnota={}
while True:
    menu()
    try:
        opcion=int(input("Ingrese la opcion que desea usar: "))
    except:
        opcion=-1
    if opcion==1:
        ingresar_nombreYnotas()
        os.system("pause")
        os.system ("cls")
    elif opcion==2:
        buscar_alumno()
        os.system("pause")
        os.system ("cls")
    elif opcion==3:
        modificar_nota()
        os.system("pause")
        os.system ("cls")
    elif opcion==4:
        listar_nombres()
        os.system("pause")
        os.system ("cls")
    elif opcion==5:
        listar_notas()
        os.system("pause")
        os.system ("cls")
    elif opcion==6:
        promedio()
        os.system("pause")
        os.system ("cls")
    elif opcion==7:
        borrar_estudiante()
        os.system("pause")
        os.system ("cls")
    elif opcion==8:
        promedio_edades()
        os.system("pause")
        os.system ("cls")
    elif opcion==0:
        print("Gracias por utilizar!.")
        os.system ("cls")
        exit()
    else:
        print("No ha ingresado una opcion valida. Intentelo nuevamente.")
        os.system ("cls")