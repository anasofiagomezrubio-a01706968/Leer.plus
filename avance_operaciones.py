def rapidez_lector(palabras,segundos):
    return (palabras/segundos)*60

def tiempo_pagina(pbpagina,rapidez_lector):
    return (pbpagina / rapidez_lector)

pbminuto = rapidez_lector(200,40)

print(tiempo_pagina(800,pbminuto))

