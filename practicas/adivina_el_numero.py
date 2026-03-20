numero_secreto = 8

while True:  # bucle infinito hasta que aciertes
    intento = int(input("Adivina un número entre 1 y 10: "))
    
    if intento < numero_secreto:
        print("El número secreto es más grande 📈")
    elif intento > numero_secreto:
        print("El número secreto es más pequeño 📉")
    else:
        print("¡Felicidades! 🎉 Adivinaste el número.")
        break  # rompe el bucle cuando aciertas