Ejercicio 5 — Historial de reproducción (10 pts)
Implementar Pila sobre ListaEnlazada (apilar y desapilar en el extremo del primer nodo):
•	apilar(dato)
•	desapilar() devuelve el tope. Si está vacía, lanza PilaVaciaError.
•	ver_tope() devuelve el tope y lo deja en la pila. Si está vacía, lanza PilaVaciaError.
•	esta_vacia()
Definir HistorialReproduccion, que usa una Pila de canciones:
•	registrar(cancion) apila lo que acaba de sonar.
•	anterior() desapila y devuelve la canción a la que se vuelve.
•	ultima() devuelve la última canción reproducida, sin sacarla.
Teoría. Se registran, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer anterior()? ¿Por qué?




________________________________________
Ejercicio 6 — Cola de reproducción (10 pts)
Implementar Cola sobre ListaEnlazada:
•	encolar(dato) agrega al final.
•	desencolar() saca y devuelve el primero. Si está vacía, lanza ColaVaciaError.
•	ver_frente() devuelve el primero y lo deja en la cola. Si está vacía, lanza ColaVaciaError.
•	esta_vacia()
Definir ColaReproduccion (la cola “up next”), que usa una Cola de canciones:
•	encolar_cancion(cancion)
•	siguiente() devuelve la canción que toca ahora.
•	que_sigue() devuelve la canción del frente, sin sacarla.
Teoría. Se encolan, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer siguiente()? ¿En qué se diferencia este orden del de la pila del ejercicio 5?
