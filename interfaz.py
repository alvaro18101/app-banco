import os
import funciones
import datos

print('BIENVENIDO AL BANCO <Nombre del banco>')
print('\t1. Iniciar sesión')
print('\t2. Crear cuenta')
print('\t3. Me olvidé mi contraseña')
while True:
    numero = input('Presione un número del menú: ')
    try:
        numero = int(numero)
        if numero in range(1,4):
            break
    except:
        pass

validacion, cuenta = funciones.iniciarSesion()
while numero == 1 and validacion == False:
    print('Datos incorrectos')    
    validacion, cuenta = funciones.iniciarSesion()
else:
    print('Estás dentro de tu sesión')
    print(f'Bienvenido {cuenta}')

# if numero == 2:
#     app.nuevoUsuario()

# if numero 3:
#     app.cambiarContraseña()