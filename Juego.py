
def juego():
    while True:
        print("**** Bienvenido a Piedra, Papel, Tijeras ****")
        herramientas ={1:"Tijeras", 2:"Papel", 3:"Piedra"}
        maquina = randrange(1,4)
        clave = int(input("""
        Haz tu eleccion: 
        [1] Tijeras
        [2] Papel
        [3] Piedra
        >>"""))
        print("\n Tu eleccion es ", herramientas[clave].upper())
        star = input("\nEsta listo para jugar digita [S] y si desea cambiar de opción digita [C]: ").upper()
        if star == "S":
            if maquina == 1 and clave == 2:
                print ("\nPerdiste Gano la Maquina con", herramientas[maquina]," y tu sacaste ",herramientas[clave],"\n")
            elif maquina == 2 and clave == 3:
                print ("\nPerdiste Gano la Maquina con", herramientas[maquina]," y tu sacaste ",herramientas[clave],"\n")
            elif maquina == 3 and clave == 1:
                print ("\nPerdiste Gano la Maquina con", herramientas[maquina]," y tu sacaste ",herramientas[clave],"\n")
            elif maquina == clave:
                print ("\nEmpate... maquina saco ", herramientas[maquina]," y tu ",herramientas[clave],"\n")
            else:
                print ("\n!Felicitaciones¡ ganaste con ",herramientas[clave]," a la maquina ", herramientas[maquina],"\n")
            empezar = input("Quieres jugar de nuevo [S] o [N]: ").upper()
            if empezar == "S":
                continue
            else:
                print("\n Gracias por jugar")
                break
        elif star == "C":
            continue       


    # point enter
if __name__ == "__main__":
    from random import randrange
    juego()

