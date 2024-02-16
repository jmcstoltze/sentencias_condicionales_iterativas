import sys

# Se declara la variable mensaje como una cadena vacía
mensaje = ''

# Ingreso de datos
w_peso = float(sys.argv[1])
h_altura = float(sys.argv[2])

# Ejemplo de validación de datos ingresados
if w_peso <= 0 or h_altura <= 0:
    mensaje = 'ERROR'

# Si se pasa la validación de datos realiza el cálculo y clasificación, de lo contrario muestra mensaje de error
if mensaje == 'ERROR':
    print(mensaje + ': ¡Debe ingresar valores correctos!')
else:
    # Cálculo del índice de masa corporal
    imc = round(w_peso/((h_altura/100)**2),2)

    # Iteración para determinar la clasificación del IMC
    if imc < 18.5:
        mensaje = 'Bajo peso'
    elif (18.5 <= imc < 25):
        mensaje = 'Adecuado'
    elif (25 <= imc < 30):
        mensaje = 'Sobrepeso'
    elif (30 <= imc < 35):
        mensaje = 'Obesidad Grado I'
    elif (35 <= imc < 40):
        mensaje = 'Obesidad Grado II'
    else:
        mensaje = 'Obesidad Grado III'
    
    # Muestra el cálculo del IMC
    print('Su IMC es: ', imc)
    print('La clasificación OMS es: ' + mensaje)
