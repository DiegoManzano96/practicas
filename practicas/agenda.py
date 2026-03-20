# Creamos un diccionario vacío
agenda = {}

# Pedimos al usuario que agregue un contacto
nombre = input("Ingresa el nombre del contacto: ")
telefono = input("Ingresa el número de teléfono: ")

# Guardamos en el diccionario
agenda[nombre] = telefono

# Mostramos la agenda completa
print("Tu agenda de contactos:")
print(agenda)

# agenda = {} → creamos un diccionario vacío.

# nombre = input(...) → el usuario escribe el nombre del contacto.

# telefono = input(...) → el usuario escribe el número.

# agenda[nombre] = telefono → guardamos el par clave: valor en el diccionario.

# La clave es el nombre.

# El valor es el teléfono.

# Al final imprimimos el diccionario completo para ver lo que hay guardado.