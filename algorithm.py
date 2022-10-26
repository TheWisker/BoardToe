def transform_matrix(table: list) -> list[int]:
    """Transforma una matriz bidimensional o superior con caracteres, a una matriz de la misma profundidad con valores numericos."""
    for i in range(len(table)):
        for _ in range(len(table)):
            if table[i][_] == "-":
                table[i][_] = -1
            elif table[i][_] == "0":
                table[i][_] = 0
            elif table[i][_] == "X":
                table[i][_] = 1
    return table
    


def check_matrix(matrix: list[str]):
    """``Metodo general para su aplicacion en matrices binarias o con caracteres que verifica con un booleano si un caracter o numero
    consigue una sucesion seguida diagonal, vertical u horizontalmente.``

    - El metodo verifica la matriz con ``4 submetodos``:
        - Primero verifica en busca de ``sucesiones horizontales``
        - Segundo verifica ``sucesiones verticales``
        - El tercero verifica ``sucesiones diagonales en tablas impares y pares (tablas con >=1 centros)``"""

    for subarrays in matrix:
            if subarrays[0] == "-":
                continue
            if all(elem == subarrays[0] for elem in subarrays):
                return True
        
    for i in range(len(matrix)):
        if (matrix[0][i] == "-" or matrix[-1][i] == "-") or (matrix[-1][i] != matrix[0][i]):
            continue
        checks = [matrix[_][i] for _ in range(1, len(matrix)-1)]
        if all(elem == matrix[0][i] for elem in checks):
            return True
    
    if len(matrix) % 2 != 0: 
            token = matrix[(len(matrix)//2)][(len(matrix)//2)]  #? centro de la matriz
        
            if token == "-":   
                return False

            if matrix[0][0] == matrix[-1][-1] and matrix[0][0] == token:
                for i in range(1, len(matrix)-1):  
                    if matrix[i][i] != token:
                        break
                    elif i == len(matrix)-2:   
                        return True

            if matrix[0][-1] == matrix[-1][0] and matrix[0][-1] == token:
                for i,s in zip(range(len(matrix)-1, 1, -1), range(1, len(matrix)-1), strict=True):
                    if matrix[i-1][s] != token:
                        break
                    elif s == len(matrix)-2:   
                        return True
    else:
        if matrix[0][0] == "-" or matrix[0][-1] == "-":     
            return False

        if matrix[0][0] == matrix[-1][-1]:
            for i in range(1, len(matrix)-1):  
                if matrix[i][i] != matrix[0][0]:
                    break
                elif i == len(matrix)-2:  
                    return True

        if matrix[0][-1] == matrix[-1][0]:
            for i,s in zip(range(len(matrix)-1,1), range(1, len(matrix)-1)):
                if matrix[i][s] != matrix[0][0]: 
                    break
                elif s == len(matrix)-2:  
                    return True
    return False


if __name__ == "__main__":
    raw_table = [
        ["-", "X", "0"],
        ["X", "0", "X"],
        ["-", "X", "0"]
    ]

    bin_matrix = transform_matrix(raw_table)
    print(bin_matrix)
    print(check_matrix(bin_matrix))
