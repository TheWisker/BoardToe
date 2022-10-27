"Main file to benchmark the game performance and game algorithms"


from timeit import Timer

table = [
        ["0", "0", "-"],
        ["X", "-", "X"],
        ["-", "0", "0"]
    ]

def benchmark(stmt, n=1000, r=3, **kwargs):
    timer = Timer(stmt, **kwargs)
    best = min(timer.repeat(r, n))

    usec = best * 1e6 / n
    #* Retorna el mejor tiempo en indice 0 y los 5 primeros e indice 1
    return usec

def run_tests(title, dictests: dict):
    print(title)
    print("-"*60)
    for name, usec in dictests.items():
        print(f'\t{name:<12} | Time -> {usec:01.4f} μs\n')
    print("\tConvertion: 1 μs = 0.001 ms = 0.00001 s")
    print("-"*60)
    


tests1 = {
    
    "Empty list method 1": benchmark("[['-' for _ in range(len(table))] for _ in range(len(table))]", globals= {"table": table}),
    "Empty list method 2": benchmark(
    """
for _ in range(0, len(table)):
    master_table.append([])
for c in master_table:
        c.append("-" for _ in range(0, len(table)))
    """, globals= {"master_table": [], "table": table}
    ),
    "Replace by index 1": benchmark(
    """
for i in range(len(table)):
    for _ in range(len(table)):
        if table[i][_] == "-":
            table[i][_] = -1
        elif table[i][_] == "0":
            table[i][_] = 0
        elif table[i][_] == "X":
            table[i][_] = 1
    """ ,
        globals= {"table": table}
    ),
    "Replace by index 2": benchmark(
        """
t = []
for i in range(len(table)):
    for _ in range(len(table)):
        if table[i][_] == "-":
            t[i][_] = -1
        elif table[i][_] == "0":
            t[i][_] = 0
        elif table[i][_] == "X":
            t[i][_] = 1
        """ ,
        globals= {"table": table}
    )
}

bot_tests_suite = {
    "Check matrix horizontal algorithm": benchmark(
        """
def check_matrix(matrix: list[int]) -> bool | list[tuple[int, tuple[int, int]]]:
    results: list[tuple[int, tuple[int, int]]] = []

    for i, subarrays in enumerate(matrix):

        if all(elem == -1 for elem in subarrays) or all(elem != -1 for elem in subarrays):   
            #* si alguna lista es totalmente vacia, que continue 
            continue
        elif all(elem == subarrays[0] for elem in subarrays):   #* si una lista esta completa, ha ganado
            return 0
        matches: list[int] = [x for x in subarrays if x == -1]  #* almacena los elementos que estan vacios

        if len(subarrays)-len(matches) == len(subarrays)-1:
            alr_list = [x for x in subarrays if x not in matches]
            if all(x == alr_list[0] for x in alr_list):
                results.append((alr_list[0], (i, subarrays.index(matches[0]))))
            else:
                continue
    return results
        """
    , globals = {"results": [], "table": table}
    ),
}
        
run_tests("Pruebas 1", tests1)
run_tests("Bot Suite (Core)", bot_tests_suite)