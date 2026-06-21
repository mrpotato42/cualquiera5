import random
cadena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud_contrasena = int(input("Introduzca un numero para definir el tamaño de su contraseña: "))

contrasena = ""

for i in range(longitud_contrasena):
    contrasena += random.choice(cadena)

print(contrasena)