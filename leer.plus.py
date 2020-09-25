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

            
#prueba
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




