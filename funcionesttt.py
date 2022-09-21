from random import randrange

# Crea una tabla matriz 2D ordenada, de 3x3.
tabla = [[3 * i + 1 + j for j in range(3)] for i in range(3)]


# Dibujando el tablero de Ta-Te-Ti
def dibujo():
    print()
    print((" "*38)+"+-------+"+"-------+"+"-------+")
    for n in range(3):
        print((" "*38)+"|       |"+"       |"+"       |")
        print((" "*38)+f"|   {tabla[n][0]}   |   {tabla[n][1]}   |   {tabla[n][2]}   |")
        print((" "*38)+"|       |"+"       |"+"       |")
        print((" "*38)+"+-------+"+"-------+"+"-------+")
        

# Verifica si hay espacios libres (sin "x" ó "o")
def espaciosLibres(tabla):
    campos = []
    for fila in range(3):
        for columna in range(3):
            if tabla[fila][columna] not in ["x", "o"]:
                campos.append((fila, columna))
    return campos
                    

# Definiendo el algoritmo de los movimientos aleatorio de la máquina.      
def Maquina(tabla, libres):
    cont = len(libres)
    if cont > 0:    # Si hay espacios libres
        marca_x = randrange(cont)
        fila, columna = libres[marca_x] # Esto va sacando espacios. Disminuye len(espacioLibre()). Se usa como condicional
        if marca_x >= 0 and marca_x < 10:
            if tabla[fila][columna] != "o" and tabla[fila][columna] != "x": # Si la elección está libre.
                tabla[fila][columna] = "x"
                indice = libres.index((fila, columna))
                del libres[indice]
            else:
                Maquina(tabla, libres)
        else:
            Maquina(tabla, libres)


# Definiendo el algoritmo de los movimientos del usuario.
def usuario(tabla, tab, libres):
    cont = len(libres)
    marca_o =  int(input("Elije un espacio para tu movimiento ► "))
    f, c = tab[marca_o-1]
    if cont > 0:
        if (marca_o > 0 and marca_o < 10):   # Si la opcion esta entre 1 y 9
            if (tabla[f][c] != "o" and tabla[f][c] != "x"):
                tabla[f][c] = "o"
                indice = libres.index((f, c))
                del libres[indice]
            else:
                print("¡ups!, lugar ocupado, intenta otro")
                usuario(tabla, tab, libres)
            return "o"
        else:
            usuario(tabla,tab, libres)
    else:
        print("¡ya no hay lugares!")
        return "empate"
   

# Condiciones para la victoria
def victoria(tabla, marca):
    # Victoria por conjunción horizontal   
    for i in range(3):
        if tabla[i].count(marca) == 3:
            return True
    # Victoria por conjunción vertical
    for j in range(3):
        if (tabla[0][j] == marca and tabla[1][j] == marca and tabla[2][j] == marca) is True:
            return True
    # Victoria por conjuncion diagonal:
    return((tabla[0][0] == marca and tabla[1][1] == marca and tabla[2][2] == marca) 
                or (tabla[2][0] == marca and tabla[1][1] == marca and tabla[0][2] == marca))
 
 
# Condiciones para el empate   
def empate(tabla, libres):
    for i in ["x", "o"]:
        if  victoria(tabla, i) is not True and len(libres) == 1:
            return True

margen = ("=".center(100, "="))
print(margen)
