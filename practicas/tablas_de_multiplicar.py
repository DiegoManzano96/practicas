print("📊 Tabla de multiplicar automática")

# El usuario elige el número
numero = int(input("¿De qué número quieres la tabla? "))

# Usamos un bucle for para generar la tabla del 1 al 10
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

# numero = int(input(...)) → el usuario escribe el número de la tabla que quiere.

# for i in range(1, 11): → el bucle recorre los números del 1 al 10.

# print(numero, "x", i, "=", numero * i) → muestra la multiplicación en cada vuelta del bucle.