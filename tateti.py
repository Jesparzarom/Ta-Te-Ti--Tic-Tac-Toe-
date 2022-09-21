from funcionesttt import*

libres = espaciosLibres(tabla)
tab = libres[:][:]

print("¡Empieza la maquina!".center(100))
tabla[1][1] = "x"

print(margen)
dibujo()
print(margen)

juego = True
while juego:
    if empate(tabla, libres)is True:    # Si la función es verdadera, se empata el juego.
        print(">>> ¡EMPATE! <<<".center(100))
        break 
    else:
        # Usuario
        usuario(tabla,tab, libres)
        print(margen)
        print("Tu marca 'o'".center(100))
        dibujo()
        print(margen)
        if victoria(tabla, "o") is True:    # Si la función es verdadera, gana el usuario.
            print(">>> ¡GANASTE! <<<".center(100))
            break

        #Maquina
        Maquina(tabla, libres)
        print(margen)
        print("Marca de la maquina 'x'".center(100))
        dibujo()
        print(margen) 
        if victoria(tabla, "x") is True:    # Si la funcion es verdadera, gana la máquina.
            print(">>> ¡UPS... TE GANÉ! xD <<<".center(100))
            break
input("Presione [Enter] para finalizar")
print(" ¡Bye!")
print(" \n" * 5)
