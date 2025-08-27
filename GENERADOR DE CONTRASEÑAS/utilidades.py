import secrets
import string
import math
import colorama 


simbolos = "@#$%!*"
caracteres = string.ascii_letters + string.digits

#Se usa secret por los valores criptográficamente
def generar_contraseña():
    return ''.join(secrets.choice(caracteres + simbolos) for _ in range(12))

def fuerza_contraseña(password):

    conteo = 0
    if any(c.islower() for c in password): conteo += 26
    if any(c.isupper() for c in password): conteo += 26
    if any(c.isdigit() for c in password): conteo += 10
    if any(c in "@#$%!*" for c in password):conteo += 6

    entropia = len(password) * math.log2(conteo) if conteo > 0 else 0

    if len(password) < 8:
        longitud = 0
    elif len(password) < 12:
        longitud = 20
    else:
        longitud = 40

    tipos = 0
    if any(c.islower() for c in password): tipos += 10
    if any(c.isupper() for c in password): tipos += 10
    if any(c.isdigit() for c in password): tipos += 10
    if any(c in "@#$%!*" for c in password): tipos += 10

    puntuacion = min(100, tipos + longitud)
    
    if puntuacion < 50 or entropia < 28:
        nivel = "Débil"
    elif puntuacion < 80 or entropia < 36:
        nivel = "Media"
    else:
        nivel = "Fuerte"

    return puntuacion, nivel, round(entropia,2)

