"""Main core module"""


from pyparsing import empty


def transform2matrix(table: list[list[int]], reverse_method: bool = None) -> list:
    """
    ``Transforma una tabla bidimensional o superior con caracteres,
    a una matriz de la misma profundidad con valores numericos o viceversa.``\n
    - Para pasar de una matriz binaria a una de caracteres, poner como ``True`` el parametro ``reverse_method``
    """
    assert isinstance(table, list) and 3 <= len(table), f"Param @matrix must be a list and depth <= 3, no {type(table).__name__}"

    if reverse_method is not None:
        for i in range(len(table)):
            for _ in range(len(table)):
                if table[i][_] == -1:
                    table[i][_] = "-"
                elif table[i][_] == 0:
                    table[i][_] = "0"
                elif table[i][_] == 1:
                    table[i][_] = "X"
        return table
        
    for i in range(len(table)):
        for _ in range(len(table)):
            if table[i][_] == "-":
                table[i][_] = -1
            elif table[i][_] == "0":
                table[i][_] = 0
            elif table[i][_] == "X":
                table[i][_] = 1
    return table


def rotate_matrix(matrix: list[list[int]], nofrots: int = 1) -> list[list[int]]:
    """
    ``Rota una matriz en sentido horario. La rotacion es de  90 Grados predeterminadamente``
    1. Original matrix:
    ```
        [0,0,1]
        [1,0,1]
        [0,1,1]
    ```

    2.  Rotating ``1`` time (default rotation):
    ``` 
        [0,1,0]
        [1,0,0]s
        [1,1,1]
    ```
    """
    
    assert isinstance(matrix, list) and 3 <= len(matrix), f"Param @matrix must be a list and depth <= 3, no {type(matrix).__name__}"
    assert isinstance(nofrots, int) or nofrots <= 4, f"You are trying to rotate the matrix 360 degrees (Original position)!!"

    if nofrots > 1:
        for _ in range(nofrots):
            matrix = rotate_matrix(matrix)
        return matrix

    N = len(matrix)

    #transponemos la matriz hacia las abujas del reloj (90 Grados)
    for i in range(N):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        
    #aqui cambias las columnas (columnas de intercambio)
    for i in range(N):
        for j in range(N // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - j - 1]
            matrix[i][N - j - 1] = temp
    
    return matrix


def hcheck(matrix: list[list[int]]) -> list:
    """``Metodo que comprueba si en la matrix existe una lista que contiene una sucesion horizontal de los mismos elementos.``
    
    Ejemplo:
    >>>    [0,1,0],
    >>>    [1,0,0],
    >>>    [1,1,-1]
    
    - En este caso la lista de indice ``2`` (``[1,1,-1]``) es una sucesion horizontal de los mismos elementos menos 1 elemento que esta vacio.
    - En ese caso se devuelve la ficha que gana y la posicion que falta para completar esa sucesion horizontal -> ``(1, (2,2))``
    """

    results: list = []

    for i, subarrays in enumerate(matrix):

        if all(elem == -1 for elem in subarrays) or all(elem != -1 for elem in subarrays) or all(elem == subarrays[0] for elem in subarrays):   
            #* si alguna lista es totalmente vacia o ningun elemento es -1 o son iguales, que continue 
            continue

        empty_index: int = subarrays.index(-1)    # sabemos que las listas tienen al menos un -1, buscamos su indice
        if all(x == subarrays[0] for x in subarrays if subarrays.index(x) != empty_index):
            results.append((subarrays[0], (i, empty_index))) #* (jugador que gana, (posicion donde puede ganar))
        else:
            continue
    return results


def check_adjacent(matrix: list[list[int]]) -> list[tuple[int, tuple[int, int]]]: #[(player, (x,y))]
    "Fucntion that returns a list with the adjacent positions to each player"
    assert isinstance(matrix, list) and 3 <= len(matrix), f"Param @matrix must be a list and depth <= 3, no {type(matrix).__name__}"


def rotate_index(index: tuple[int, int], depth: int) -> tuple[int, int]:
    result: list[int, int] = []
    """
   | [1,1,1],
   | [0,0,1],
   | [0,1,0]

    [0, 0 ,1],
    [1, 0 ,1],
    [0, 1 ,1]



    (0,0) (2,0)
    (0,1) (1,0)
    (0,2) (0,0)

    [0,1,2]

    (1,0) (0,1)
    (1,1) (1,1)
    (1,2) (2,1)

    (2,0) (2,2)
    (2,1) (1,2)
    (2,2) (0,2)
    """
    result.append(sorted([x for x in range(depth)], reverse = True)[index[0]])
    result.append(index[0])
    return result
    

def check_enemy_win(binmatrix: list[list[int]]) -> list: #Checks if the enemy player can win in one movement  and returns the results like: [(player, (x,y))]
    results: list = []
    
    results.extend(hcheck(binmatrix)) #Horizontal
    results.extend(rotate_index(hcheck(rotate_matrix(binmatrix)))) #Vertical ROTATE RESULTS
    
    #DIAGONAL METHOD    
        
    return results



def check_matrix(matrix: list[int]) -> bool | list[tuple[int, tuple[int, int]]]: #Checks if anyone has won the game
    """"""
    assert isinstance(matrix, list), f"Param @matrix must be a list, no {type(matrix).__name__}"
    
    hcheck(matrix) #Horizontal
    hcheck(rotate_matrix(matrix)) #Vertical
    
    if len(matrix) % 2 != 0: 
            token = matrix[(len(matrix)//2)][(len(matrix)//2)]  #? centro de la matriz
        
            if token == "-":   
                return False

            if matrix[0][0] == matrix[-1][-1] and matrix[0][0] == token:
                for i in range(1, len(matrix)-1):  
                    if matrix[i][i] != token:
                        break
                    elif i == len(matrix)-2:   
                        return 0

            if matrix[0][-1] == matrix[-1][0] and matrix[0][-1] == token:
                for i,s in zip(range(len(matrix)-1, 1, -1), range(1, len(matrix)-1), strict=True):
                    if matrix[i-1][s] != token:
                        break
                    elif s == len(matrix)-2:   
                        return 0
    else:
        if matrix[0][0] == "-" or matrix[0][-1] == "-":     
            return False

        if matrix[0][0] == matrix[-1][-1]:
            for i in range(1, len(matrix)-1):  
                if matrix[i][i] != matrix[0][0]:
                    break
                elif i == len(matrix)-2:  
                    return 0

        if matrix[0][-1] == matrix[-1][0]:
            for i,s in zip(range(len(matrix)-1,1), range(1, len(matrix)-1)):
                if matrix[i][s] != matrix[0][0]: 
                    break
                elif s == len(matrix)-2:  
                    return 0
    return




def show_matrix(matrix: list[list[int]]) -> None:
    print("-"*len(matrix)*4)
    for i in matrix:
        print(f"{i}")
    print("-"*len(matrix)*4)
    return


if __name__ == "__main__":
    raw_matrix = [
        ["-", "0", "X", "0", "-", "X"],
        ["X", "0", "X", "-", "X", "X"],
        ["X", "0", "-", "0", "X", "X"],
        ["X", "0", "X", "-", "X", "X"],
        ["X", "0", "X", "X", "X", "X"],
        ["0", "-", "0", "0", "X", "0"]
    ]

    bin_matrix = transform2matrix(raw_matrix)
    # print(bin_matrix)
    #print(check_matrix(bin_matrix))
    # print(rotate_matrix(bin_matrix))

    print(check_enemy_win(bin_matrix))
    # print(hcheck(rotate_matrix(bin_matrix)))
   
    
