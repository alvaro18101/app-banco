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

if numero == 1:
    # iniciar sesion
    validacion, cuenta = funciones.iniciarSesion()
    while validacion == False:
        print('Datos incorrectos')    
        validacion, cuenta = funciones.iniciarSesion()
    else:
        print('Estás dentro de tu sesión')
        print(f'Bienvenido {cuenta.nombre.split(' ')[0]}')
        print('\t1. Depositar dinero')
        print('\t2. Retirar dinero')
        print('\t3. Transferir dinero')
        while True:
            numero2 = input('Presione un número del menú: ')
            try:
                numero2 = int(numero)
                if numero2 in range(1,4):
                    break
            except:
                pass
        
        if numero2 == 1:
            # Depositar dinero
            funciones.depositarDinero(cuenta.saldo)
        
        # if numero2 == 2:
        #     # retirar dinero
            
        
        # if numero2 == 3:
        #     # transferir dinero
            


# if numero == 2:
#     # crear cuenta
#     app.nuevoUsuario()

if numero == 3:
    # recuperar contraseña
    numero_cuenta = input('Ingresa el número de cuenta: ')