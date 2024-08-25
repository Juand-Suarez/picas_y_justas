# ----------------------------------------------------------------------------------------
# PROGRAMA: Picas y fijas
# ----------------------------------------------------------------------------------------
# Descripción: Un juego muy conocido para pasar el tiempo es “picas y fijas”, el cual consiste 
# en tratar de adivinar un número en la menor cantidad de jugada_usuarios posible.
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
# Numero de jugada_usuarios

def generar_numero_secreto():
    """
    Genera un número secreto de 4 dígitos no repetidos, sin ceros al inicio.

    Returns:
    list: Lista de 4 dígitos únicos.
    """

    # Eliminamos el 0 de la lista de posibles dígitos para el primer lugar
    digitos = list(range(1, 10)) + [0]

    # Seleccionamos los primeros 4 dígitos, asegurando que el primero no sea 0
    numero_secreto = random.sample(digitos, 4)
    numero_secreto[0], numero_secreto[3] = numero_secreto[3], numero_secreto[0]  # Intercambiamos el primer y último dígito

    return numero_secreto

def calcular_picas(numero_secreto, jugada_usuario):
    """
    Cuenta el número de picas (dígitos correctos en posición incorrecta).

    Parametros:
        numero_secreto (list): Lista de 4 dígitos del número secreto.
        jugada_usuario (list): Lista de 4 dígitos del jugada_usuario del jugador.

    Returns:
        int: Número de picas.
    """
    picas = 0
    for i in range(4):
        if jugada_usuario[i] in numero_secreto and jugada_usuario[i] != numero_secreto[i]:
            picas += 1
    return picas

def calcular_fijas(numero_secreto, jugada_usuario):
    """
    Cuenta el número de fijas (dígitos correctos en posición correcta).

    Parametros:
        numero_secreto (list): Lista de 4 dígitos del número secreto.
        jugada_usuario (list): Lista de 4 dígitos del jugada_usuario del jugador.

    Returns:
        int: Número de fijas.
    """
    fijas = 0
    for i in range(4):
        if jugada_usuario[i] == numero_secreto[i]:
            fijas += 1
    return fijas


print("*** Programa para el Juego de Picas y Fijas ***\n")
print("Debes adivinar un número de 4 dígitos no repetidos.\n")


numero_secreto = generar_numero_secreto()
jugada_usuarios = 0

while True:

    jugada_usuario = input("Ingresa un número de 4 dígitos no repetidos: ")
    jugada_usuario = [int(d) for d in jugada_usuario]
    print(jugada_usuario)

    picas = calcular_picas(numero_secreto, jugada_usuario)
    fijas = calcular_fijas(numero_secreto, jugada_usuario)

    print(f"Picas: {picas}, Fijas: {fijas}")

    if fijas == 4:
        print(f"¡Felicidades! Adivinaste el número secreto en {jugada_usuarios} jugada_usuarios.")
        break

    jugada_usuarios += 1

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------

