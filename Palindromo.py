def main():
    print("\n\t******** Bienvenido a de Palindromos ********\n")
    palabra = input(">>> Escribe una palabra: ").lower().replace(" ", "")
    if palabra == palabra[::-1]:
        print("Es palindromo")
    else:
        print("No es Palindromo")
    condicion = input("\nDesea escribir otra palabra? [S] o [N]: ").upper()
    if condicion == "S":
        main()
    else:
        print("Gracias por usar el programa")
        sys.exit()
        

if __name__ == "__main__":
    import sys
    main()