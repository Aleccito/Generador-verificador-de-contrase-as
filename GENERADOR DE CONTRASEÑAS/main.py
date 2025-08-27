from utilidades import *

def main():
    print("\t\tVERIFICADOR / GENERADOR DE CONTRASEÑAS")
    print("\n1. Generar contraseña automatica")
    print("2. Verificar mi fuerza de mi contraseña")
    
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print(f"Tu contraseña es: {generar_contraseña()} ")
        
    if opcion == 2:
        contraseña = input("Ingrese contraseña: ")
        puntuacion, nivel, entropia = fuerza_contraseña(contraseña)
        print(f"Contraseña: {contraseña}\nPuntuación: {puntuacion}%\nNivel: {nivel}\nEntropía: {entropia} bits")
    

if __name__ == "__main__":
    main()