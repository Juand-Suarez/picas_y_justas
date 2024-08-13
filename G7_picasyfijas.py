# ----------------------------------------------------------------------------------------
# PROGRAMA: Picas y fijas
# ----------------------------------------------------------------------------------------
# Descripción: Un juego muy conocido para pasar el tiempo es “picas y fijas”, el cual consiste 
# en tratar de adivinar un número en la menor cantidad de intentos posible.
# ----------------------------------------------------------------------------------------
# Autor: Victor Hernandez Lopez ,Juan Suarez Padilla, Johan Sánchez Sánchez

# Version: 1.0
# [12.08.2024]
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import random   # modulo de python para generar valores random

# ----------------------------------------------------------------------------------------
# PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# jugada_usuario: numero natural de cuatro digitos

# ----------------------------------------------------------------------------------------
# POS-CONDICIONES
# ----------------------------------------------------------------------------------------
# Numero de intentos

import random

def generar_numero_secreto():
    digitos = list(range(10))  # Dígitos del 0 al 9
    numero_secreto = random.sample(digitos, 4)
    return numero_secreto
def calcular_picas(numero_secreto, jugada_usuario):
    picas = sum(1 for d1, d2 in zip(numero_secreto, jugada_usuario) if d1 == d2)
    return picas
def calcular_fijas(numero_secreto, jugada_usuario):
    fijas = sum(1 for d1, d2 in zip(numero_secreto, jugada_usuario) if d1 == d2)
    return fijas


numero_secreto = generar_numero_secreto()
intentos = 0

while True:

    jugada_usuario = input("Ingresa un número de 4 dígitos no repetidos: ")
    jugada_usuario = [int(d) for d in jugada_usuario]
    print(jugada_usuario)

    picas = calcular_picas(numero_secreto, jugada_usuario)
    fijas = calcular_fijas(numero_secreto, jugada_usuario)

    print(f"Picas: {picas}, Fijas: {fijas}")

    if fijas == 4:
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
        break

    intentos += 1

