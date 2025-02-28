from datos import usuarios

def iniciarSesion():
    cuenta = input("Ingrese número de cuenta: ")
    contraseña = input("Ingrese contraseña: ")
    for usuario in usuarios:
        if cuenta == usuario.numero_cuenta:
            if contraseña == usuario.contraseña:
                return (True, usuario)
            else:
                return (False, 0)

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