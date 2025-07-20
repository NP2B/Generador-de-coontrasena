import random

def generar_contraseña():
    caracteres = "&$#@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    #se usa para atrapar errores
    try:
        longitud = int(input("Introduce la longitud de tu contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser un número positivo.")
            return
    # qué hacer si ocurre ese error
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    contraseña = ""
    for _ in range(longitud):
        contraseña += random.choice(caracteres)

    print(f"Tu contraseña generada es:{contraseña}")

# Llamar a la función
generar_contraseña()
