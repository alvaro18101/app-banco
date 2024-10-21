# saldo=float(input("INGRESE SU SALDO: "))
# deposito=float(input("INGRESE MONTO A DEPOSITAR: "))

def depositarDinero(saldo, deposito):
    monto_final = saldo+deposito
    return monto_final

# print(depositarDinero(saldo, deposito))

def iniciarSesion():
    usuario0="0123456789"
    contraseña0="1234"
    usuario=input("Ingrese usario: ")
    contraseña=input("Ingrese contraseña: ")
    if usuario!=usuario0 or contraseña!=contraseña0:
        print("Datos Incorrectos")
    else:
        print("Ingreso exitoso")

iniciarSesion()