import random
import string

# Lista de usuarios
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5', 'usuario6', 'usuario7','usuario8', 'usuario9', 'usuario10']
for usuario in usuarios:
    print(usuario)

def generar_contraseña():
    longitud = 8  # Puedes ajustar la longitud de la contraseña según tus necesidades
    caracteres = string.ascii_letters + string.digits
    contraseña = ''
    contraseña += random.choice(string.ascii_uppercase)  # Añadir una letra mayúscula
    contraseña += random.choice(string.ascii_lowercase)  # Añadir una letra minúscula
    contraseña += random.choice(string.digits)  # Añadir un número
    for _ in range(longitud - 3):
        contraseña += random.choice(caracteres)  # Añadir caracteres aleatorios
    contraseña_lista = list(contraseña)
    random.shuffle(contraseña_lista)  # Mezclar los caracteres
    contraseña = ''.join(contraseña_lista)
    return contraseña

# Asignar contraseñas a cada cuenta de usuario
cuentas = {}
for usuario in usuarios:
    contraseña = generar_contraseña()
    cuentas[usuario] = contraseña
    telefono = input(f"Ingrese el número telefónico para {usuario}: ")
    if len(telefono) <= 8:
        print('Teléfono registrado')
    else:
            print("El número telefónico debe tener 8 caracteres o menos.")
    cuentas[usuario] = {'contraseña': contraseña, 'telefono': telefono}
    

# Imprimir las cuentas de usuario con sus contraseñas
for usuario, contraseña in cuentas.items():
    print(f"Usuario: {usuario}, Contraseña: {contraseña}")




