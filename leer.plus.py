def rapidez_lector(palabras,segundos):
    return (palabras/segundos)*60

def tiempo_pagina(pbpagina,rapidez_lector):
    return (pbpagina / rapidez_lector)

def tiempo_libro(numpaginas,tiempo_pagina):
    return (tiempo_pagina * numpaginas)

def tiempo(tiempo_libro):
    horas=0
    minutos=0
    if (tiempo_libro >= 60):
        horas = tiempo_libro//60
        minutos = tiempo_libro%60
        return("El tiempo para leer el libro es de" ,horas, "hrs,con" ,minutos, "minutos")
    else:
        return("El tiempo para leer el libro es de" ,tiempo_libro, "minutos")
    


#prueba
palabras=int(input())
segundos=int(input())
rapidez=rapidez_lector(palabras,segundos)
print("La rapidez del lector es,",rapidez,"palabras por minuto")

ppagina=int(input())
tenpagina=tiempo_pagina(ppagina,rapidez)
print(tenpagina)

numpag=int(input())
tenlibro=tiempo_libro(numpag,tenpagina)
print(tenlibro)

print(tiempo(tenlibro))

