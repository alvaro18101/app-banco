saldo=float(input("INGRESE SU SALDO: "))
deposito=float(input("INGRESE MONTO A DEPOSITAR: "))

def depositarDinero(saldo, deposito):
    monto_final = saldo+deposito
    return monto_final

print(depositarDinero(saldo, deposito))