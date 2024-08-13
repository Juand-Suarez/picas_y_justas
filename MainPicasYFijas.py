# ----------------------------------------------------------------------------------------
# PROGRAMA: MainPicasYFijas
# ----------------------------------------------------------------------------------------
# Descripción: Programa principal para el juego de Picas y Fijas. Permite al usuario intentar
#              adivinar un número secreto de 4 dígitos no repetidos y proporciona retroalimentación
#              sobre el número de picas y fijas en cada intento.
# ----------------------------------------------------------------------------------------
# Autor: Luis Carlos Díaz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from picas_y_fijas_funciones import generar_numero_secreto, contar_picas, contar_fijas

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# Las funciones importadas deben estar correctamente implementadas y probadas en el archivo picas_y_fijas_funciones.py.

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# El programa debe devolver la cantidad de picas y fijas para cada intento del usuario.

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# No se requieren parámetros adicionales para este programa.

# <<Escriba desde aqui el código del programa...>>

def main():
    print("*** Programa para el Juego de Picas y Fijas ***")
    
    numero_secreto = generar_numero_secreto()
    intentos = 0
    print("Debes adivinar un número de 4 dígitos no repetidos.")

    while True:
        intento = input("Ingresa tu intento: ")
        intento = [int(d) for d in intento]

        picas = contar_picas(numero_secreto, intento)
        fijas = contar_fijas(numero_secreto, intento)
        intentos += 1

        print(f"Picas: {picas}, Fijas: {fijas}")

        if fijas == 4:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------