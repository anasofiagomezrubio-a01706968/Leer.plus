# Leer.plus
¿Qué es Leer.plus?
  -Es un programa diseñado para mejorar el rendimiento del lector haciendo un plan para leer un libro en un determinado tiempo, tomando en cuenta el número de páginas del libro y la rapidez del lector. Además permite al usuario plantearse una meta de libros que quiere leer por año, calcular cuántos le falta por leer y realizar un regisro de los libros que desea leer y los que ya ha leído. 

¿Cómo funcionará?
La primera parte del programa calcula el tiempo que tardaría el lector en leer un libro deseado tomanando en cuenta las características del libro y la rapidez de lector del usuario. También permite al usuario llevar un registro de lo que lleva leído y da una retroalimentación de la cantidad de días que tardó en leer el libro.

 ¿Cómo se caclula la rapidez de lector?
 -Primero se calcula la rapidez del lector dividiendo el número de palabras de un texto entre la cantidad de segundos que se tardó multiplicado por 60        (palabras/segundos*60=palabras por minuto).

 -De ahí se asigna el nivel de rapidez del lector en base a una tabla (arreglo).

 -Calcular un estimado de tiempo que le tomaría a una persona de cierto nivel leer una página del libro. (palabras en una página/palabras por minuto=tiempo en leer una página).

 -Multiplicar ese tiempo por el número de páginas de un libro para saber cuánto tardaría en leerlo (tiempo en leer una página*número de páginas=tiempo en leer el libro).

 -Determinar cuánto tiempo desearía leer esa persona al día (ej, 30 minutos diarios)

 -Dividir el tiempo en total para leer el libro sobre la cantidad de tiempo que se desea leer por día (tiempo en leer el libro/minutos diarios=días para leer el libro)

 -Esa es la cantidad de días que se necesitarían para acabar ese libro dependiendo del nivel de lectura de cada usuario.
 
 La segunda parte del programa permite al usuario plantearse una meta de libros a leer en el año y calcular cuántos le faltan de acuerdo con los que lleva leídos, además le permite crear una lista con los libros que desea leer.
 
 Por último, el programa permite al usuario llevar un registro de los libros que ha leído junto con sus respectivos géneros.
  
  
