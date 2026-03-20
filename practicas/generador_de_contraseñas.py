import random

print("🔑 Generador de contraseñas simple")

# Definimos los caracteres que puede tener la contraseña
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"

# Pedimos la longitud de la contraseña
longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

# Generamos la contraseña escogiendo caracteres al azar
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña es:", contraseña)

# import random: usamos la librería para elegir cosas al azar.

# caracteres = "...": es un string que contiene letras, números y símbolos.

# longitud = int(input(...)): el usuario decide cuántos caracteres tendrá la contraseña.

# for i in range(longitud):: repetimos tantas veces como la longitud que pidió el usuario.

# random.choice(caracteres): elige un carácter aleatorio del string.

# contraseña += ...: vamos construyendo la contraseña sumando cada carácter.