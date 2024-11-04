class Usuario:
    def __init__(self, nombre, numero_cuenta, contraseña, saldo):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.contraseña = contraseña
        self.saldo = float(saldo)

    def __str__(self):
        return self.nombre
    
    # def depositarDinero(self, saldo):
    #     return app.depositarDinero(self.saldo)

usuario1 = Usuario('Walter Matias Siesquén Abad', '0123456789', '1234', 600.50)
usuario2 = Usuario('Alvaro Alejandro Siesquén Abad', '72954528', '1810', 850)

usuarios = [usuario1, usuario2]

def obtenerAtributos(usuarios, dato):
    datos = []
    for usuario in usuarios:
        datos.append(getattr(usuario,dato))
    return datos

nombres = obtenerAtributos(usuarios, 'nombre')
numeros_cuentas = obtenerAtributos(usuarios, 'numero_cuenta')
contraseñas = obtenerAtributos(usuarios, 'contraseña')

# Guardado de datos en un .xlsx o .csv