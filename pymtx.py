"""Main core module.
EXCLUSIVE FOR MATRIX OPERATIONS

Copyright present Backest-TheWisker 2022-2023
"""
import operator as _operator
import numpy as _np
from copy import deepcopy
from typing import Any


__all__ = [

]


#TODO ///////////////////////////////////////       ARITHMETIC FUNCTIONS        ////////////////////////////////////////////////

def opmtx(mtxs: list[list[list[int | float | str]]], optype: str, dtype: Any = int):
    """Convenience function that allows different operations with matrixs through a parameter in one function.
    
    - NOTE: You can type a optional/secret operation type ``osqrt`` to cause the first element to be raised to the power of 1 between the second index
    """

    #! PROBLEMA GRAVE: ALGUNAS OPERACIONES NO SE PUEDEN HACER PORQUE AL OPERAR CON CUALQUIER NUMERO PUEDE RESULTAR QUE SE DIVIDA POR ZERO
    #! SI UTILIZAS LA OPERACION "==" Y LE PASAS ALGO QUE NO SEA STR, TE DEVUELVE 1 como 'True' y 0 como 'False'
    ops = {
        '+': _operator.add,
        '*': _operator.mul,
        '**': _operator.pow,
        '-': _operator.sub,
        '/': _operator.truediv,
        '//': _operator.floordiv,
        '%': _operator.mod,
        '>': _operator.gt,
        '<': _operator.lt,
        '>=': _operator.ge,
        '<=': _operator.le,
        '==': _operator.eq,
        "||": _operator.abs, #DA ERROR PORQUE LE PASAMOS DOS PARAMETROS, HAY QUE DIFERENCIAR ENTRE OPERACIONES CON UNO O DOS PARAMETROS
        "..": _operator.concat,
        '<<': _operator.lshift,
        '>>': _operator.rshift,
        #'√'
        "osqrt": ...,    #kk ** (1/vv) -> onesqrt, instancing this to internal purposes
    }


    if not optype in ops.keys():
        raise TypeError("The operation type is not valid!!. Cannot operate with this operation type %s" % repr(dtype))
    elif dtype.__name__ not in [float.__name__, int.__name__, str.__name__]:
        raise TypeError("Data type must a reprentable data type (str, int, float)")


    operation = ops[optype]
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(operation(kk, vv) if optype != "osqrt" else kk * (1/vv)) for kk,vv in zip(k, v)])
    return r[0]


def conctx(mtxs: list[list[list[int | float]]], dtype: Any = int) -> list[list[int | float]]:
    return sumtx(mtxs, dtype)

def sumtx(mtxs: list[list[list[int | float]]], dtype: Any = int) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk + vv) for kk,vv in zip(k, v)])
    return r[0]

def submtx(mtxs: list[list[list[int | float]]], dtype: Any = int) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk - vv) for kk,vv in zip(k, v)])
    return r[0]

def mmtp(mtxs: list[list[list[int | float]]], dtype: Any = int) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk * vv) for kk,vv in zip(k, v)])
    return r[0]

def div_mtx(mtxs: list[list[list[int | float]]], dtype: Any = float) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk / vv) for kk,vv in zip(k, v)])
    return r[0]

def exp_mtx(mtxs: list[list[list[int | float]]], dtype: Any = int) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk ** vv) for kk,vv in zip(k, v)])
    return r[0]

def mod_mtx(mtxs: list[list[list[int | float]]], dtype: Any = float) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk % vv) for kk,vv in zip(k, v)])
    return r[0]

def xrt_mtx(mtxs: list[list[list[int | float]]], dtype: Any = float) -> list[list[int | float]]:
    assert dtype.__name__ in [float.__name__, int.__name__, str.__name__], "Data type must a reprentable data type (str, int, float)"
    r: list = [mtxs[0], []]
    for mtx in mtxs[1:]:
        r[1], r[0] = r[0], []
        for k,v in zip(r[1], mtx):
            r[0].append([dtype(kk ** (1/vv)) for kk,vv in zip(k, v)])
    return r[0]



#TODO ///////////////////////////////////////       SPATIAL FUNCTIONS        ////////////////////////////////////////////////

def reverse_matrix(matrix: list[list], h: bool = True) -> list[list[int]]:
    """
    (es): Invierte una matriz horizontal o verticalmente.\n
    (en): Reverses a matrix horizontal or vertically.\n

    Horizontal reversion:\n
        [1,  1,  0] ------> [0,  1,  1]\n
        [1,  0,  0] ------> [0,  0,  1]\n
        [0,  0,  1] ------> [1,  0,  0]\n

    Vertical reversion:\n
        [1,  0,  0] ------> [0,  0,  1]\n
        [1,  1,  1] ------> [1,  1,  1]\n
        [0,  0,  1] ------> [1,  0,  0]\n
    """
    r: list = []
    if h:
        for k in range(len(matrix)):
            r.append([matrix[k][kk] for kk in range(len(matrix[k])-1, -1, -1)])
    else:
        r.append(matrix[k] for k in range(len(matrix)-1, -1, -1))
    return r

# ! NO DEBERIAN ESTAR AQUI, CONSIDERAR CAMBIO DE NOMBRE Y QUE COÑO HACEN
def replace_mtx(mtxs: list[list[list]], _search: list = [], _replace: list = [0]) -> list[list[list]]:
    r: list = [[[] * v in mtx] for mtx in mtxs]
    for mtx in mtxs:
        rr: list = []
        for v in mtx:
            rrr: list = []
            for vv in v:
                rrr.append(vv if vv not in _search and len(_search) != 0 else _replace[_search.index(vv) if len(_search) != 0 else 0])
            rr.append(rrr)
        r.append(rr)
    return r

def fill_mtx(mtxs: list[list[list]], fill = 0) -> list[list[list]]:
    return replace_mtx(mtxs, _replace = [fill])



#TODO ///////////////////////////////////////       COMPARATION FUNCTIONS        ////////////////////////////////////////////////

def get_biggest(mtxs: list[list[list]], mtp: bool = True) -> list[list] | list[list[list]]:
    r: list = [msize(mtxs[0]), [mtxs[0]]]
    for v in mtxs[1::]:
        c: int = msize(v)
        r[1] = [v] if r[0] < c else r[1] + [v] if r[0] == c else r[1]
        r[0] = c if r[0] < c else r[0]
    return r[1] if len(r[1]) > 1 and mtp else r[1][0]

def get_smallest(mtxs: list[list[list]], mtp: bool = True) -> list[list] | list[list[list]]:
    r: list = [msize(mtxs[0]), [mtxs[0]]]
    for v in mtxs[1::]:
        c: int = msize(v)
        r[1] = [v] if r[0] > c else r[1] + [v] if r[0] == c else r[1]
        r[0] = c if r[0] > c else r[0]
    return r[1] if len(r[1]) > 1 and mtp else r[1][0]

def is_biggest(mtx: list[list], mtxs: list[list[list]]) -> bool:
    return msize(mtx) >= msize(get_biggest(mtxs, False))

def is_smallest(mtx: list[list], mtxs: list[list[list]]) -> bool:
    return msize(mtx) <= msize(get_smallest(mtxs, False))



#TODO ///////////////////////////////////////       MISCELLANEOUS UTILS FUNCTIONS        ////////////////////////////////////////////////

def msize(mtx: list[list]) -> int:
    #! plantear recursion para evaluar todos los depth
    n: int = 0
    for v in mtx:
        n += len(v) 
    return n

def pretty_view(matrix: list[list[int]]) -> None:
    "Easy, rapid method to get a pretty view of the matrix"
    print("-"*len(matrix)*4)
    for i in matrix:
        print(f"{i}")
    print("-"*len(matrix)*4)
    return

def reverse_index(inx: list[int, int], dpth: int, h: bool = True) -> list[int, int]:
    """
    (es): Invierte un indice de una matriz invertida horizontal o verticalmente para conseguir su equivalente en la matriz original.\n
    (en): Reverses an index of a reversed matrix horizontal or vertically to get its equivalent index for the original matrix.\n

    Horizontal reversion:\n
                           Reversed -> Original\n
        [0,  1,  0] ------> (0,0)   ->  (0,2)\n
        [1,  0,  1] ------> (0,1)   ->  (0,1)\n
        [0,  0,  1] ------> (0,2)   ->  (0,0)\n

    Vertical reversion:\n
                           Reversed -> Original\n
        [0,  1,  0] ------> (0,0)   ->  (2,0)\n
        [1,  0,  1] ------> (1,0)   ->  (1,0)\n
        [0,  0,  1] ------> (2,0)   ->  (0,0)\n   
    """
    tmp: list = [inx[0], inx[1]] if h else [inx[1], inx[0]]
    tmp[1] = [x for x in range(dpth-1, -1, -1)][tmp[1]]
    return tmp if h else [tmp[1], tmp[0]]

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

def rotate_matrix(matrix: list[list[int]], nofrots: int = 1, numpymethod: bool = False, returnm: bool = True, ) -> list[list[int]] | None:
    """
    ``Rota una matriz en sentido horario. La rotacion es de  90 Grados predeterminadamente``
    - NOTE: ``4 rotaciones equivalen a 360 grados, es decir, a la posicion original.``

    ### Hasta x2 veces mas rapido que el metodo de rotacion de matrices de ``numpy``
    
    ### Ejemplo
    ```
    1. Original matrix:        2. Rotating 1 time (default rotation):

        Original               Rotated 90 degrees
        [0,0,1]                [0,1,0]
        [1,0,1]                [1,0,0]
        [0,1,1]                [1,1,1]
    ```
    """
    assert isinstance(matrix, list) and 3 <= len(matrix), f"Param @matrix must be a list and depth <= 3, no {type(matrix).__name__}"
    assert isinstance(nofrots, int) or nofrots <= 4, f"You are trying to rotate the matrix 360 degrees (Original position)!!"

    if nofrots > 1:
        for _ in range(nofrots):
            matrix = rotate_matrix(matrix, nofrots, numpymethod, returnm)
        return matrix

    if numpymethod:
        m = _np.array(matrix, dtype=int)
        _np.rot90(m, 1, (-1, 0))
        return m if returnm else None

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
    
    return matrix if returnm else None

def hcheck(matrix: list[list[int]]) -> list[list[int | tuple[int, int]]] | list:
    """``Metodo general usado para comprobar si algun jugador esta a un movimiento de hacer una sucesion horizontal.``
    #### NOTE! Este metodo se puede aplicar para comprobar una sucesion en cualquier direccion, tan solo rotando la matriz.
    
    ### Ejemplo:
    >>>    [0,1,0],
    >>>    [1,0,0],
    >>>    [1,1,-1]
    
    - En este caso la lista de indice ``2`` (``[1,1,-1]``) es una sucesion horizontal de los mismos elementos menos 1 elemento que esta vacio.
    - En ese caso se devuelve la ficha que gana y la posicion que falta para completar esa sucesion horizontal -> ``(1, (2,2))``
    """
    assert isinstance(matrix, list) or not all(isinstance(e, list) for e in matrix) or not matrix, "@index param must be list containing tuples that contain integers"

    results: list = []

    for i, subarray in enumerate(matrix):

        if all(elem == subarray[0] for elem in subarray) or not -1 in subarray or subarray.count(-1) > 1:
            continue  
        #* sabemos que las listas que tenemos solo tienen un -1
        empty_index: int = subarray.index(-1)
        if len(set(subarray)) == 2:     
            results.append([subarray[empty_index-1], (i, empty_index)])
    return results

def dcheck(matrix: list[tuple[int]]) -> list[list[int | tuple[int, int]]] | list:
    #TODO: HAY QUE ARREGLARLO IMPLEMENTANDO EL REVERSE MATRIX
    """
    ``Metodo usado para comprobar si algun jugador esta a un movimiento de hacer una sucesion diagonal.``

    ### Ejemplo:
    >>>    [0,1,1],
    >>>    [1,0,0],
    >>>    [1,-1,-1]

    - En este caso hay una diagonal desde el indice ``[0,0]`` hasta ``[-1][-1]``
    - En ese caso se devuelve la ficha que gana y la posicion que falta para completar esa sucesion diagonal -> ``(0, (2,2))``
    """

    r = []  #? para almacenar los datos finales
    templist = [matrix[i][i] for i in range(len(matrix))]
    
    if templist.count(-1) == 1 and len(set(templist)) == 2:
        empty_index = templist.index(-1)
        r.append([templist[empty_index-1], (empty_index, empty_index)])

    templist.clear()

    for a,i in zip(range(len(matrix)), range(len(matrix)-1, -1, -1), strict=True):
        templist.append(matrix[a][i]) 
        if templist.count(-1) == 2 or len(set(templist)) > 2:
            r.pop()
            break
        elif templist[-1] == -1 and templist.count(-1) == 1 and len(set(templist)) == 2:
            r.append([templist[templist.index(-1)-1], (a, i)])
        
    return r

def check_win(matrix: list[list[int]], player: dict[str,]) -> list[list]: 
    """Comprueba y devuelve que jugadores pueden ganar colocando una sola ficha
    - NOTE: La funcion puede devolver una lista vacia si ningun jugador esta a un movimiento de ganar
    - NOTE 2: Si los dos jugadores comparten una posicion, se muestran las dos posiciones, no una.
    """
    wins: list = []

    if not player["token"] in ["X", "0"]:
        raise TypeError(f"Player token must be X or 0, not {repr(player['token'])}")

    pltoken = 1 if player["token"] == "X" else 0

    deeplist = deepcopy(matrix)      #? memoize list, to create a new list in a new memory object
    rotmatx = rotate_matrix(deeplist)

    if hcheck(matrix):
        wins.extend([p for p in hcheck(matrix) if p[0] == pltoken])
    if hcheck(rotmatx):
        wins.extend(rotate_index([p for p in hcheck(rotmatx) if p[0] == pltoken], len(rotmatx)))  #* Vertical check (Rotate matrix)
    if dcheck(matrix):
        wins.extend([p for p in dcheck(matrix) if p[0] == pltoken])
    
    return wins

def adjacent_check(matrix: list[list[int]], n: int) -> list[tuple[int, tuple[int, int]]]: #[(player, (x,y))]
    "Function that returns a list with the adjacent positions to each player"
    return [].extend(row_check(matrix, n)).extend(row_check(rotate_matrix(matrix), n, True)).extend(cross_check(matrix, n))

def row_check(matrix: list[list[int]], n: int, rt: bool = False) -> list[tuple[int, list[int, int]]]:
    r: list = []
    for k,v in enumerate(matrix):
        if len(set(v)) == 2 and all(x in set(v) for x in [-1, n]):
            rr: list = []
            for kk,vv in enumerate(v):
                if vv == -1:
                    rr.append(rotate_index([k, kk], len(matrix)) if rt else [k, kk])
            r.append((v.count(-1), rr))
    return r

def cross_check(matrix: list[list[int]], n: int) -> list[list[tuple[int, list[int, int]]]]:
    return [].extend(dgn_check(matrix, n)).extend(dgn_check(reverse_matrix(matrix), n, True))

def dgn_check(matrix: list[list[int]], n: int, rt: bool = False) -> tuple[int, list[list[int, int]]]:
    r: list = []
    dgn: list = [matrix[i][i] for i in range(len(matrix))]
    if len(set(dgn)) == 2 and all(x in set(dgn) for x in [-1, n]):
        for k,v in enumerate(dgn):
                r.append(reverse_index([k, k], len(matrix)) if rt else [k, k])
    return (dgn.count(-1), r)

def rotate_index(inx: list[int, int] | list[list[int, int]], depth: int, backwards: bool = True) -> list[int, int]:
    """
    NOTE: The method only accepts square methods for now

    ## Parameters:

        ``@index``: The index as [x, y]
        ``@matrix_depth``: The matrix length, 
        ``@backwards``: If it should rotate backwards (default forwards)
    - Example:

        rotate_index([0,0], 3, False) -> [0,2]
    """
    if isinstance(inx, (list, tuple)):
        return [rotate_index(i) for i in inx]

    r: list = [inx[0], inx[1]] if backwards else [inx[1], inx[0]]
    r[1] = r[0]
    r[0] = depth-1-inx[1]
    return r if backwards else [r[1], r[0]]



#TODO ///////////////////////////////////////       TODO FUNCTIONS        ////////////////////////////////////////////////

def filter(): #Filter results by number of ocurrences
    ...
def transpose_matrix():
    ...
def randomize_mtx():
    ...
def extend_mtx():
    ...
def copy_mtx():
    ...
def add_dimension():
    ...
def sub_dimension():
    ...



if __name__ == "__main__":
    from dis import dis

    models: dict[str, str] = {

        1: [
            ["X", "-", "X"],
            ["0", "-", "0"],
            ["X", "0", "X"],

        ],
        2: [
            ['0', '-', '0', '0', '0'],
            ['-', '-', '-', '0', '0'],
            ['0', '-', '-', '0', '0'],
            ['0', '0', '-', '-', '-'],
            ['X', 'X', 'X', 'X', 'X']
        ],
        5: [
            ['0', '-', '0', '0', '0'],
            ['-', '-', '-', '0', 'X'],
            ['0', '-', '-', '0', 'X'],
            ['0', '0', '-', '-', 'X'],
            ['0', '0', '0', '0', '0']
        ],
        3: [
            [0,  1,   0, 0],
            [1, -1,  -1, -1],
            [1,  1,   0,  0],
            [1, -1,  -1,  0]
        ],
        4: [
            ['X', '0', '-', 'X', '0', 'X', '0', '0'],
            ['-', '-', '0', 'X', 'X', '-', '0', '0'],
            ['X', '0', 'X', 'X', '-', '0', 'X', '-'],
            ['X', '0', '0', 'X', '0', '0', 'X', '0'],
            ['X', '0', '0', '0', 'X', 'X', '-', 'X'],
            ['X', '0', '-', 'X', '-', 'X', 'X', '-'],
            ['X', '0', '0', 'X', 'X', '0', 'X', '0'],
            ['0', '0', 'X', 'X', '0', 'X', '-', 'X']
        ],
        6: [
            [4, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ],
        7: [
            [-5, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ],
        8: [
            [4, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ],
        9: [
            [4, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ]
} 
#print(fill_mtx([models[6], models[7]]))
print(opmtx([models[6], models[7]], "||", str))
#pretty_view(add_mtx([models[6], models[7], models[8], models[9]]))