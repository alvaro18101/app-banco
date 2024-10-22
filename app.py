def depositarDinero():
    while True:
        saldo = input("Ingrese su saldo: ")
        try:
            saldo = float(saldo)
            if saldo >= 0:
                break
        except:
            pass

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
    

depositarDinero()

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