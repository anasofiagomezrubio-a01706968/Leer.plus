def rapidez_lector(palabras,segundos):
    return (palabras/segundos)*60


def tiempo_pagina(pbpagina,rapidez_lector):
    return (pbpagina / rapidez_lector)

pbminuto = rapidez_lector(200,40)


print("caso 1 valor %s,  es %r debe ser %r" % ((200,40), rapidez_lector(200,40), 300 ))
print("caso 2 valor %s,  es %r debe ser %r" % ((800,40), rapidez_lector(800,40), 1200 ))
print("caso 3 valor %s,  es %r debe ser %r" % ((350,45), rapidez_lector(350,45), 466.66 ))
print("caso 4 valor %s,  es %r debe ser %r" % ((562,58), rapidez_lector(562,58), 581.37 ))

print("caso 1 valor %s,  es %r debe ser %r" % ((800,pbminuto), tiempo_pagina(800,pbminuto), 2.66 ))
print("caso 2 valor %s,  es %r debe ser %r" % ((1050,pbminuto), tiempo_pagina(1050,pbminuto), 3.5 ))
print("caso 3 valor %s,  es %r debe ser %r" % ((15678,pbminuto), tiempo_pagina(15678,pbminuto), 52.26 ))
print("caso 4 valor %s,  es %r debe ser %r" % ((89355,pbminuto), tiempo_pagina(89355,pbminuto), 297.85 ))

