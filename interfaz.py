import funciones

print('BIENVENIDO AL BANCO <Nombre del banco>')
print('1. Iniciar sesión')
print('2. Crear cuenta')
print('3. Me olvidé mi contraseña')
while True:
    numero = input('Presione un número del menú: ')
    try:
        numero = int(numero)
        if numero in range(1,4):
            break
    except:
        pass


if numero == 1:
    funciones.iniciarSesion()

# if numero == 2:
#     app.nuevoUsuario()

# if numero 3:
#     app.cambiarContraseña()