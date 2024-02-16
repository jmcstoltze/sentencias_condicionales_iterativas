
# Importación de librerías
import random
import sys

# Declaración de variables y sus valores
jugadas = ['piedra', 'papel', 'tijera']
jugada_maquina = random.choice(jugadas)
jugada_usuario = sys.argv[1].lower()

# Validación de la jugada
if (jugada_usuario != 'piedra' and jugada_usuario != 'papel' and jugada_usuario != 'tijera'):
    print ('Argumento inválido: Debe ser piedra, papel o tijera.')
else:
    # En caso de que usuario juegue piedra
    if jugada_usuario == 'piedra':
        if jugada_maquina == 'piedra':
            resultado = 'Empate!!'
        elif jugada_maquina == 'papel':
            resultado = 'Perdiste!!'
        else:
            resultado = 'Ganaste!!'
    # En caso de que usuario juegue papel
    elif jugada_usuario == 'papel':
        if jugada_maquina == 'papel':
            resultado = 'Empate!!'
        elif jugada_maquina == 'tijera':
            resultado = 'Perdiste!!'
        else:
            resultado = 'Ganaste!!'

    # En caso de que usuario juegue tijera
    else: 
        if jugada_maquina == 'tijera':
            resultado = 'Empate!!'
        elif jugada_maquina == 'piedra':
            resultado = 'Perdiste!!'
        else:
            resultado = 'Ganaste!!'

    # Se imprime el resultado en pantalla
    print ('Tú jugaste ' + jugada_usuario.capitalize())
    print ('Computador jugó ' + jugada_maquina)
    print (resultado)
