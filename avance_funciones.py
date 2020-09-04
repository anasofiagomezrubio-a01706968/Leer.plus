def rapidez_lector(palabras,segundos):
    return (palabras/segundos)*60

def tiempo_pagina(pbpagina,rapidez_lector):
    return (pbpagina / rapidez_lector)

def tiempo_libro(numpaginas,tiempo_pagina):
    return (tiempo_pagina * numpaginas)

#prueba
palabras=int(input())
segundos=int(input())
rlector=rapidez_lector(palabras,segundos)
pbpagina=int(input())
tpag=tiempo_pagina(pbpagina,rlector)
numpaginas=int(input())
tlibro=tiempo_libro(numpaginas,tpag)

print("El tiempo en necesario para leer el libro es",tlibro,"minutos")

