import pandas as pd

class Usuario:
    def __init__(self, nombres, apellidos, numero_cuenta, contraseña, saldo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.contraseña = contraseña
        self.saldo = float(saldo)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
    # def depositarDinero(self, saldo):
    #     return app.depositarDinero(self.saldo)

# leer el archivo de la data, si no está el archivo, se tiene que crear
try:
    df = pd.read_csv('datos.csv')
except:
    df = pd.DataFrame(columns=['nombres', 'apellidos', 'numero_cuenta', 'contraseña', 'saldo'])
    usuario1 = Usuario('Walter Matias', 'Siesquén Abad', '0123456789', '1234', 600.50)
    usuario2 = Usuario('Alvaro Alejandro', 'Siesquén Abad', '72954528', '1810', 850)
    nuevo_dato1 = pd.DataFrame([vars(usuario1)])
    nuevo_dato2 = pd.DataFrame([vars(usuario2)])
    df = pd.concat([df, nuevo_dato1], ignore_index=True)
    df = pd.concat([df, nuevo_dato2], ignore_index=True)

df['numero_cuenta'] = df['numero_cuenta'].astype(str)
df['contraseña'] = df['contraseña'].astype(str)
df['saldo'] = df['saldo'].astype(float)

usuarios = []
usuario = []
for j in range(len(df)):
    for i in df.columns:
        usuario.append(df[i][0])
    print(j)
    usuarios.append(usuario)

print(usuarios)

def obtenerAtributos(usuarios, dato):
    datos = []
    for usuario in usuarios:
        datos.append(getattr(usuario,dato))
    return datos

# nombres = obtenerAtributos(usuarios, 'nombre')
# numeros_cuentas = obtenerAtributos(usuarios, 'numero_cuenta')
# contraseñas = obtenerAtributos(usuarios, 'contraseña')

# Guardado de datos en un .xlsx o .csv
df.to_csv('datos.csv', index=False, encoding='utf-8-sig')