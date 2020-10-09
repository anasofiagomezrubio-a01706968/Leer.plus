#código del proyecto leer.plus
def rapidez_lector(palabras,segundos): #función para determinar que tan rápido lee una persona 
    return (palabras/segundos)*60

def tiempo_pagina(pbpagina,rapidez_lector): #función para determinar cuanto tiempo taradía esa persona en una página de su libro
    return (pbpagina / rapidez_lector)

def tiempo_libro(numpaginas,tiempo_pagina): #función para determinar el tiempo total en minutos para leer el libro
    return (tiempo_pagina * numpaginas)

def tiempo(tiempo_libro): #función para convertir el tiempo total a horas y minutos
    horas=0
    minutos=0
    if (tiempo_libro >= 60):
        horas = tiempo_libro//60
        minutos = tiempo_libro%60
        return("El tiempo para leer el libro es de" ,horas, "hrs,con" ,minutos, "minutos")
    else:
        return("El tiempo para leer el libro es de" ,tiempo_libro, "minutos")

def dias_terminar(tiempo_libro,tdia): #función para determinar cuantos días se necesitan para acabar el libro dependiendo de cuanto tiempo quiera leer esa persona por dia
    return (tiempo_libro/tdia)

def libro_terminado(dias_terminar): #función para retroalimentar al lector sobre su progreso con el libro y determinar cuantos días se tardó contando los días en los que no leyó
    acum = 0.0
    diastotal = 0.0
    terminado = ""
    print("¿leiste?")
    leiste = str(input())
    if (leiste == "si"):
        acum = 1.0
        diastotal = 1.0
        while (acum < dias_terminar):
            if (leiste == "si"):
                acum = acum + 1.0
                terminado = "no has terminado el libro"
                print(terminado)
                diastotal = diastotal + 1.0
            if (leiste == "no"):
                acum = acum
                terminado = "no has terminado el libro"
                print(terminado)
                diastotal = diastotal + 1.0
            print("¿leiste?")
            leiste = str(input())
        terminado = "terminaste el libro"
        diastotal = diastotal
        print(terminado, " y tardaste ", diastotal, "dias")
    else:
        terminado = ("no has empezado el libro")
        print (terminado)

# Aquí empieza la parte del programa para que los usuarios mantengan un registro de los libros que han leido y los que desean leer.
def lista_libros_por_leer(año,leer):
    libros_por_leer=[]
    libro=""
    while (0<=leer < año ):
        libro = str(input("¿Qué libro quieres agregar a tu lista de libros por leer?"))
        libros_por_leer.append(libro)
        leer=leer+1
    return "Tu lista de libros por leer es" , libros_por_leer


def lista_libros_leidos(leidos):
    while (leidos > 0):
        libros_terminados=[]
        libro=""
        acum=0
        while (acum < leidos):
            libro=str(input("¿Qué libro deseas agregar a tu lista de leidos?"))
            libros_terminados.append(libro)
            acum=acum+1
        return libros_terminados

def genero_libros(lista):
    generos=[]
    acum=0
    while (acum < len(lista)):
        for libro in lista:
            print (libro)
            genero = str(input("¿Qué género es este libro?"))
            generos.append(genero)
            acum=acum+1
    return generos

def generos_de_libros(lista,lista_generos):
    libros_y_generos=[[lista],[lista_generos]]
    return libros_y_generos

def genero_favorito(generos):
    vg={}
    fav=[0]
    rep=0
    for genero in generos:
        vg[genero]=0
    for genero in generos:
        vg[genero]=vg[genero]+1
        if(vg[genero] > rep):
            rep= vg[genero]
            fav= genero
    return("La cantidad de libros por cada genero es",vg,"tu genero favorito es",fav)

           
#Aplicación del programa, es decir, lo que el usuario ve.
print("Si quieres ver cuanto tardarías en leer un libro y tu rapidez de lector ingresa 1")
print("Si quieres calcular cuántos libros te faltan por leer para alcanzaar tu meta anual y crear tu lista de libros que deseas leer, ingresa 2")
print("Si quieres ingresar los libros que ya leíste con su respectivo género y saber cuál es tu género favorito, ingresa 3")
opcion = int(input())
if (opcion == 1):
    print("¿Cúantas palabras tiene el texto?")
    palabras=int(input())
    print("¿Cuántos segundos tardaste en leer el texto?")
    segundos=int(input())
    rapidez=rapidez_lector(palabras,segundos)
    print("La rapidez de lector es,",rapidez,"palabras por minuto")

    print("Aproximadamente, ¿Cuántas palabras tiene una página de tu libro?")
    ppagina=int(input())
    tenpagina=tiempo_pagina(ppagina,rapidez)
    print("Te tardarás",tenpagina,"minutos, en cada página")

    print("¿Cuántas páginas tiene tu libro?")
    numpag=int(input())
    tenlibro=tiempo_libro(numpag,tenpagina)
    print(tiempo(tenlibro))

    print("Aproximadamente, ¿Cuánto quieres leer por día (en minutos)?")
    tdia = int(input())
    dias_para_terminar = dias_terminar(tenlibro,tdia)
    print("Si lees diario, tardarás",dias_para_terminar, "dias, para acabar tu libro")


    print(libro_terminado(dias_para_terminar))

if (opcion == 2):#opcion para determinar cuantos lbros faltan por leer y crear una lista de los libros que el usuario desea leer
    libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
    libros_leidos=int(input("¿Cuántos libros has leido?"))
    while (libros_del_año <= 0 or libros_leidos < 0 ):
        print ("tus valores no se pueden utilizar en este programa, intenta otra vez, acuerda de no usar números negativos!")
        libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
        libros_leidos=int(input("¿Cuántos libros has leido?"))
    libros_leer=libros_del_año - libros_leidos
    print("Para alcanzar tu meta del año, te faltan leer " ,libros_leer)
    print(lista_libros_por_leer(libros_del_año,libros_leidos))

if (opcion == 3):#opcion para crear listas sobre los libros leidos y generos correspondientes, además de determinar el género favorito.
    libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
    libros_leidos=int(input("¿Cuántos libros has leido?"))
    while (libros_del_año <= 0 or libros_leidos < 0 ):
        print ("tus valores no se pueden utilizar en este programa, intenta otra vez, acuerda de no usar números negativos!")
        libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
        libros_leidos=int(input("¿Cuántos libros has leido?"))
    libros_leer=libros_del_año - libros_leidos
    
    mis_libros=lista_libros_leidos(libros_leidos)
    generos=genero_libros(mis_libros)
    libros_y_generos= generos_de_libros(mis_libros,generos)
    
    print("Los libros que has leído con su género correspondiente es " , libros_y_generos)
    print(genero_favorito(generos))

if (opcion != 1 or opcion != 2 or opcion != 3):
    print("Opción no válida")
    
