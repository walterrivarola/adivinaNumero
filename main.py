from random import *

nombre = input("Nombre del jugador: ")
aleatorio = randint(1, 101)
print(f"Un placer {nombre}, he pensando un número del 1 al 100. Puedes adivinarlo? Te doy 8 intentos")

print(aleatorio)

intentos = 0

for intentos in range(1,9):
    intento = int(input(f"{intentos} intento/s - Ingrese un número: "))
    while intento < 1:
        print("Recuerda que es un número de entre 1 al 100")
        intento = int(input(f"{intentos} intento/s - Ingrese un número: "))
    if intento == aleatorio:
        print(f"Felicidades {nombre}, has acertado y tan sólo necesitaste {intentos} intento/s")
    else:
        print("Lastima no acertaste, vuelve a intentarlo")
        intentos += 1