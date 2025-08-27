from utilidades import *

def main():
    print("\t\tVERIFICADOR / GENERADOR DE CONTRASEÑAS")
    while True:
        print("\n1. Generar contraseña automática")
        print("2. Verificar la fuerza de mi contraseña")
        opcion = input("\nIngrese una opción (1, 2): ")
        print("-------------------------------------")

        try:
            opcion = int(opcion)
            
            if opcion == 1:
                print(f"Tu contraseña es: {generar_contraseña()}") 
                print("-------------------------------------")       
                         
            elif opcion == 2:
                contraseña = input("Ingrese contraseña: ")
                puntuacion, nivel, entropia = fuerza_contraseña(contraseña)
                print(f"Contraseña: {contraseña}\nPuntuación: {puntuacion}%\nNivel: {nivel}\nEntropía: {entropia} bits")
                print("-------------------------------------")  
            else:
                print("Opción no válida (1, 2).")
                print("-------------------------------------")

        except Exception as x:
            print("\nIngresa una opción correcta. ")
            print(f"ERROR: {type(x).__name__}")
            print("-------------------------------------")
    

if __name__ == "__main__":

    main()
