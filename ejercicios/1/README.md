### EJERCICIO DE BIBLOTECA DIGITAL

Instrucciones: Crea un sistema para gestionar una biblioteca digital usando listas, tuplas, for, while y try/except.

#### REQUERIMIENTOS

##### DATOS INICIALES

· Crea una lista con 6 títulos de libros

· Crea una tupla con géneros literarios: ("Ficción", "Misterio", "Romance", "Ciencia", "Historia")

· Crea otra lista para el estado de cada libro: "Disponible" o "Prestado"

##### TAREAS A REALIZAR

A) Usando FOR:

· Recorre los libros y muestra: "Libro #1: [título] - Estado: [disponible/prestado]"

· Recorre los géneros y asigna uno aleatorio a cada libro

· Muestra cada libro con su género asignado

B) Usando WHILE:

· Simula el sistema de préstamos: usa while para cambiar el estado de 3 libros de "Disponible" a "Prestado"

· Usa otro while para contar cuántos libros están disponibles después de los préstamos

C) Modificaciones (LISTAS vs TUPLAS):

· Agrega 2 libros nuevos a la biblioteca

· Intenta modificar uno de los géneros de la tupla (debe dar error)

· Maneja el error correctamente

· Agrega los estados "Disponible" para los nuevos libros

D) Análisis final:

· Usa FOR para crear un reporte de libros por género

· Usa WHILE para encontrar el primer libro disponible de género "Ficción"

##### 🎲 BONUS (Opcional):

· Crear un sistema de búsqueda por título

· Implementar un sistema de devolución de libros

· Mostrar estadísticas de la biblioteca

#### 📝 CONCEPTOS QUE DEBES USAR:

· ✅ Lista mutable para libros y estados

· ✅ Tupla inmutable para géneros

· ✅ FOR para recorrer y asignar

· ✅ WHILE con contadores y búsquedas

· ✅ Try/except para manejar errores

· ✅ Listas paralelas (libros, estados, géneros asignados)

#### 💡 PISTAS:

· Usa random.choice(generos) para asignar géneros aleatorios

· Las listas paralelas deben tener el mismo índice para el mismo libro

· Recuerda que random.randint(0, len(lista)-1) te da un índice válido