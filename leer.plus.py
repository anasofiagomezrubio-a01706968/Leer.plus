"""
Código de programa leer.plus
Esta primera parte del programa sirve para calcular la cantidad
de días que le tomaría a un usuario leer un libro considerando su
rapidez como lector y la cantidad de tiempo que le gustarúa leer por día.
"""

"""
==========funciones de rapidez de lector y tiempo para leer un libro==============
"""

def rapidez_lector(palabras,segundos):
    """
    Función para determinar que tan rápido lee una persona.
    """
    if (palabras > 0 and segundos > 0):
        return (palabras/segundos)*60

def tiempo_pagina(pbpagina,rapidez_lector):
    """
    Función para determinar cuanto tiempo taradía esa persona en una página de su libro
    """
    return (pbpagina / rapidez_lector)

def tiempo_libro(numpaginas,tiempo_pagina):
    """
    Función para determinar el tiempo total en minutos para leer el libro.
    """
    return (tiempo_pagina * numpaginas)

def tiempo(tiempo_libro):
    """
    Función para convertir el tiempo total a horas y minutos.
    """
    horas=0
    minutos=0
    if (tiempo_libro >= 60):
        horas = tiempo_libro//60
        minutos = tiempo_libro%60
        return("El tiempo para leer el libro es de" ,horas, "hrs,con" ,minutos, "minutos")
    else:
        return("El tiempo para leer el libro es de" ,tiempo_libro, "minutos")

def dias_terminar(tiempo_libro,tdia):
    """
    Función para determinar cuantos días se necesitan para acabar el libro.
    """
    return (tiempo_libro/tdia)

def libro_terminado(tiempo):
    """
    Función para mantener registro de lo que se lleva leído del libro.
    """
    acum=0.0
    diastotal=0
    terminado=""
    leiste=""  
    while (acum < tiempo):
        leiste=str(input("¿leíste?"))
        if (leiste == "si"):
            print("¿Cuánto tiempo leíste?")
            minutos_leidos=(int(input()))
            acum=acum+minutos_leidos
            diastotal=diastotal+1
            
        if(leiste == "no"):
            print("Acuérdate de leer")
            acum=acum
            diastotal=diastotal+1
        
        if (leiste == "no" and acum == 0.0):
            print("No has empezado el libro")
            acum=acum
            diastotal=diastotal
        
    diastotal=diastotal
    terminado = "Ya terminaste el libro"
    return (terminado, "y tardaste " ,diastotal, "dias")


        
"""
Aquí empieza la parte del programa para que los usuarios mantengan
un registro de los libros que han leido y los que desean leer
"""

"""
=======Funciones para registro de libros leídos y por leer==========
"""

def lista_libros_por_leer(año,leer):
    """
    Función para crear lista de libros por leer.
    """
    libros_por_leer=[]
    libro=""
    while (0<=leer < año):
        libro = str(input("¿Qué libro quieres agregar a tu lista de libros por leer?"))
        libros_por_leer.append(libro)
        leer=leer+1
    return "Tu lista de libros por leer es" , libros_por_leer


def lista_libros_leidos(leidos):
    """
    Función para crear lista de libros leídos.
    """
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
    """
    Función para crear lista con los géneros de los libros leídos.
    """
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
    """
    Función para concatenar lista de leídos y su respectivo género.
    """
    libros_y_generos=[[lista],[lista_generos]]
    return libros_y_generos



def genero_favorito(generos):
    """
    Función para determinar el género favorito en base a su repetición.
    """
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



            
"""
Aplicación del programa, es decir, lo que el usuario ve, se aplican las funciones
declaradas anteriormente dependiendo de la elección del usuario
"""

print("Si quieres ver cuanto tardarías en leer un libro y tu rapidez de lector ingresa 1")
print("Si quieres calcular cuántos libros te faltan por leer para alcanzaar tu meta anual y crear tu lista de libros que deseas leer, ingresa 2")
print("Si quieres ingresar los libros que ya leíste con su respectivo género y saber cuál es tu género favorito, ingresa 3")
opcion = int(input())
if (opcion == 1):
    """
    opción para calcular rapidez de lector
    calcula tiempo para leer un libro
    mantiene registro de lo que se lleva leído
    """
    print("¿Cúantas palabras tiene el texto?")
    palabras=int(input())
    print("¿Cuántos segundos tardaste en leer el texto?")
    segundos=int(input())
    
    if (palabras > 0 and segundos > 0):
        rapidez=rapidez_lector(palabras,segundos)
        print("La rapidez de lector es,",rapidez,"palabras por minuto")
    
        print("Aproximadamente, ¿Cuántas palabras tiene una página de tu libro?")
        ppagina=int(input())
        if (pbpagina > 0 ):
            tenpagina=tiempo_pagina(ppagina,rapidez)
            print("Te tardarás",tenpagina,"minutos, en cada página")

            print("¿Cuántas páginas tiene tu libro?")
            numpag=int(input())
            if (numpag > 0 ):
                tenlibro=tiempo_libro(numpag,tenpagina)
                print(tiempo(tenlibro))

                print("Aproximadamente, ¿Cuánto quieres leer por día (en minutos)?")
                tdia = int(input())
                if (tdia > 0):
                    dias_para_terminar = dias_terminar(tenlibro,tdia)
                    print("Si lees diario, tardarás",dias_para_terminar, "dias, para acabar tu libro")
                    print(libro_terminado(tenlibro))
                else:
                    print ("Valores no validos")
            else:
                print ("Valores no validos")
        else:
            print ("Valores no validos")

if (opcion == 2):
    """
    opcion para determinar cuantos lbros faltan por leer
    crea una lista de los libros que el usuario desea leer
    """
    libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
    libros_leidos=int(input("¿Cuántos libros has leido?"))
    while (libros_del_año <= 0 or libros_leidos < 0 ):
        print ("tus valores no se pueden utilizar en este programa, intenta otra vez, acuerda de no usar números negativos!")
        libros_del_año=int(input("¿Cuántos libros quieres leer este año?"))
        libros_leidos=int(input("¿Cuántos libros has leido?"))
    libros_leer=libros_del_año - libros_leidos
    print("Para alcanzar tu meta del año, te faltan leer " ,libros_leer)
    print(lista_libros_por_leer(libros_del_año,libros_leidos))

if (opcion == 3):
    """
    opcion para crear listas sobre los libros leidos
    crear lista generos de libros leídos
    concatenar listas anteriores
    determinar el género favorito.
    """
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

if (opcion != 1 and opcion != 2 and opcion != 3):
    print("Opción no válida")
    
