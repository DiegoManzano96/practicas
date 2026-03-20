import random
print("🔥 Menú interactivo en consola")

while True:
    # Mostramos las opciones
    print("\nElige una opción:")
    print("1. Saludar")
    print("2. generador de contraseña")
    print("3. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":

    
        while True:
            nombre = input("ingresa nombre y apellido")
            print("1.saludo formal")
            print("2. saludo informal")
            print("3. Salir")
            subopcion = input("ingresar tipo de saludo")

            if subopcion == "1":
                print("buenos dias " + nombre)
            elif subopcion == "2":
                print("hola " + nombre)
            elif subopcion == "3":
                print("Hasta luego 👋")
                break  # aquí termina el programa
            else:
                print("⚠️ Opción inválida, intenta de nuevo")

    elif opcion == "2":
        while True:
            print("1. crear contraseña")
            print("2. Salir")
            subopcion = input("ingresar opcion")        

            if subopcion == "1":
                                 
                    # Definimos los caracteres que puede tener la contraseña
                    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"

                    # Pedimos la longitud de la contraseña
                    longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

                    # Generamos la contraseña escogiendo caracteres al azar
                    contraseña = ""
                    for i in range(longitud):
                        contraseña += random.choice(caracteres)

                    print("Tu contraseña es:", contraseña)
                
                    
            elif opcion == "2":
                print("Hasta luego 👋")
                break  # aquí termina el programa
        else:
            print("⚠️ Opción inválida, intenta de nuevo")                 

                  
        print("Tu número favorito es el 7")
    elif opcion == "3":
        print("Hasta luego 👋")
        break  # aquí termina el programa
    else:
        print("⚠️ Opción inválida, intenta de nuevo")