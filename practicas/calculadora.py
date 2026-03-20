while True:
    n1 = float(input("primer numero"))
    n2 = float(input("segundo numero"))

    print("Elige la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5 salir")
    opcion = input("ingresar operacion")

    

    if opcion == "1":
        print(n1 + n2)
    elif opcion == "2":
        print(n1 - n2)
    elif opcion == "3":
        print(n1 * n2)
    elif opcion == "4":
        if n2 != 0 :
            print(n1 / n2)
    elif opcion == "5":
        print("hasta luego")
        break
    else:
        print("opcion invalida")


