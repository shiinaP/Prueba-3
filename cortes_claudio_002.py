lista=[]
def confirmar():
    op=input("Esta seguro de que quiere actualizar el nombre?").lower()
    if op=="si":
        return True
    if op=="no":
        return False
    else:
        print("Ingrese una opcion valida")
def listar():
    for x in lista:
        p=x[2]
        if p<0:
            print("Su equipo puede ser listado...")
        else:
            print("Su equipo no puede ser listado.")
            

def estadisticas():
    cont=0
    acum=0
    puntos=0
    for x in lista:
        cont=cont+1
        acum=int(acum+x[2])
    prom=acum/cont
    print("El promedio de puntos es de = ",prom)
    for x in lista:
        p=x[2]
        if puntos<p:
            puntos=x[2]
    print ("La mayor cantidad de puntos son = ",puntos)
    
def datos_equipo(a):
    encontrado=false
    for x in lista:
        if a==x[1]:
            print("Numero de equipo: ", x[1],"\nNombre: ",x[0],"\nPuntos: ",x[2],"\nCategoria: ",x[3])
            encontrado=True
            break
        if encontrado==False:
            print("El equipo no existe.")
while(True):
    print("1.- Agregar equipo")
    print("2.- Listar equipo")
    print("3.- Actualizar nombre de equipo por id")
    print("4.- Generar BBDD")
    print("5.- Cargar BBDD")
    print("6.- Estadisticas")
    print("0.- Salir")
    print("")
    print("")
    print("")
    op=int(input("Ingrese una opcion: "))
    if op==1:
        nombre=input("Ingrese el nombre del equipo que desea agregar: ")
        numero=int(input("Ingrese el numero del equipo: "))
        puntos=int(input("Ingrese el numero de puntos del equipo: "))
        if puntos <= 0 and puntos >=40:
                   categoria=amateur
        elif puntos <= 41 and puntos >=80:
            categoria=principiante
        elif puntos <= 81 and puntos >=120:
            categoria=avanzada
        elif puntos <= 120:
            categoria=idolos
        listad=[nombre,numero,puntos,categoria]
        lista.append(listad)               
        print("")
    elif op==2:
        print("")
        listar()
        for x in lista:
            print ("Nombre : ", x[0],"Numero : ", x[1], "Puntos : ", x[2], "Categoria : ", x[3])
    elif op==3:
        print("")
        num_buscar=int(input("Ingrese el numero del equipo"))
        datos_equipo(num_buscar)
        nombre_act=print("Ingrese el nuevo nombre de su equipo")
        confirmar()
        if nombre_act=nombre:
            nombre_act=nombre
    elif op==4:
        print("Generando BBDD...")
        with open('bbdd_equipos.csv','w'nweline='') as bbdd_equipos:
            escritor_csv=csv.writer(bbdd_equipos)
            escritor_csv.writerow(['Numero','Nombre','Puntos','Categoria'])
            escritor_csv.writerow(lista)
            print("Archivo generado con exito")
    elif op==5:
        print("Cargando BBDD...")
        with open('bbdd_equipos.csv','r',newline='')as bbdd_equipos:
            lector_csv=csv.reader(bbdd_equipos)
            for x in lector.csv:
                list.append(x)
                print("Csv cargado exitosamente")
    elif op==6:
        print("Estadisticas del equipo : ")
        estadisticas()
    elif op==0:
        print("Adios...")
        break
    else:
        print("Ingrese una opcion valida")
        
