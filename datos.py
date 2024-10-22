class Usuario:
    def __init__(self, nombre, numero_cuenta, contraseña):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.contraseña = contraseña

    def __str__(self):
        return self.nombre

matias = Usuario('Walter Matias Siesquén Abad', '0123456789', '1234')