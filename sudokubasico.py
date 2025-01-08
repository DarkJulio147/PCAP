sudokuok = True
tablero = []

for i in range(9):
    fila = input(f"Mete un número para la línea {i + 1} (9 dígitos): ")
    if fila.isnumeric() and len(fila) == 9:
        if sorted(fila) != list("123456789"):
            print("La fila debe contener todos los dígitos del intervalo [1, 9] sin repetir.")
            sudokuok = False
            break
        else:
            tablero.append(fila)
    else:
        print("La fila debe contener exactamente 9 números.")
        sudokuok = False
        break

if sudokuok:
    print("El sudoku es válido.")
    print("Tablero:")
    for fila in tablero:
        print(fila)
else:
    print("El sudoku no es válido.")
