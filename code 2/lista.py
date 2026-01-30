numeros = [1, 2, 3, 4, 5]

print("Números en la lista:", numeros)

# Primer elemento
print(numeros[0])  

 # Agregar un elemento
numeros.append(6)  

print("Lista después de agregar un elemento:", numeros)

# Insertar un elemento en la posición 2
numeros.insert(2, 2.5)
print("Lista después de insertar un elemento en la posición 2:", numeros)

# Eliminar
x = numeros.pop()
print("Lista después de eliminar el último elemento:", numeros, "Elemento eliminado:", x)

# Numero de elementos
x = len(numeros)
print("Número de elementos en la lista:", x)

## Acceder a un elemento
x = numeros[3]
print("Numero de elemento en la posiscion 5:", x)


