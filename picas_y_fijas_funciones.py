# ----------------------------------------------------------------------------------------
# PROGRAMA: Funciones para Picas y Fijas
# ----------------------------------------------------------------------------------------
# Descripción: Este archivo contiene las funciones necesarias para el juego de Picas y Fijas,
#              incluyendo la generación del número secreto y el conteo de picas y fijas.
# ----------------------------------------------------------------------------------------
# Autor: Luis Carlos Díaz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import random

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# Las funciones deben recibir los datos en el formato adecuado para su correcto funcionamiento.

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# Las funciones deben devolver resultados precisos y actualizados según las operaciones realizadas.

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# No se requieren parámetros adicionales para estas funciones.

# <<Escriba desde aqui el código de las funciones...>>

def generar_numero_secreto():
    """
    Genera un número secreto de 4 dígitos no repetidos.

    Returns:
        list: Lista de 4 dígitos únicos.
    """
    digitos = list(range(10))
    random.shuffle(digitos)
    return digitos[:4]

def contar_picas(numero_secreto, intento):
    """
    Cuenta el número de picas (dígitos correctos en posición incorrecta).

    Args:
        numero_secreto (list): Lista de 4 dígitos del número secreto.
        intento (list): Lista de 4 dígitos del intento del jugador.

    Returns:
        int: Número de picas.
    """
    picas = 0
    for i in range(4):
        if intento[i] in numero_secreto and intento[i] != numero_secreto[i]:
            picas += 1
    return picas

def contar_fijas(numero_secreto, intento):
    """
    Cuenta el número de fijas (dígitos correctos en posición correcta).

    Args:
        numero_secreto (list): Lista de 4 dígitos del número secreto.
        intento (list): Lista de 4 dígitos del intento del jugador.

    Returns:
        int: Número de fijas.
    """
    fijas = 0
    for i in range(4):
        if intento[i] == numero_secreto[i]:
            fijas += 1
    return fijas

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
