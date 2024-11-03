from datos import numeros_cuentas
from datos import contraseñas

def iniciarSesion():
    cuenta = input("Ingrese usario: ")
    contraseña = input("Ingrese contraseña: ")
    if (cuenta in numeros_cuentas) == False or (contraseña in contraseñas) == False:
        print("Datos Incorrectos")
        return False
    else:
        print("Ingreso exitoso")
        return True

def depositarDinero(saldo):
    while True:
        deposito = input("Ingrese el monto a depositar: ")
        try:
            deposito = float(deposito)
            if deposito > 0:
                break
        except:
            pass
    saldo += deposito
    print(f'Saldo actual: S/ {saldo}')

def retirarDinero(saldo):
    while True:
        retiro = input("Ingrese el monto a retirar: ")
        try:
            retiro = float(retiro)
            if retiro > 0 and retiro<=saldo:
                break
        except:
            pass
    saldo -= retiro
    print(f'Saldo actual: S/ {saldo}')