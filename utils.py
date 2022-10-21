def multiple_instcheck(vars: tuple, checks: tuple | None, manual_check: list = None):
    """Function to simplicity the ``isinstance()`` checks.
    This function allow to check if n elements are instance of a type.
    
    >>> foo = 34
    >>> poo = '34'

    - Instead of:

    >>> if isinstace(foo, int) and isinstance(poo, int):
    >>>    ...

    - We do:

    >>> if not _multiple_instcheck((foo, poo), int):
    >>>     ...
    """
    if not manual_check and checks is None:
        raise AttributeError("Checks parameter must be passed if not 'manual_checks' is passed")

    if manual_check is not None:
        if isinstance(manual_check, (list, tuple)):
            return any(elem == mck for elem, mck in zip(vars, manual_check, strict=True))
        return all(elem == manual_check for elem in vars)
    else:
        return all(isinstance(e, checks) for e in vars)


def multiple_replace(rawstr: str, reml: tuple[tuple], count: int = -1):
    """Replacement optimized function."""
    assert isinstance(rawstr, str), "'rawstr' parameter must be the string representation where the characters will be replaced"
    assert isinstance(reml, tuple), "'reml' must be a tuple containing old-new values to be replaced"
    
    for i in reml:
        rawstr = rawstr.replace(i[0], i[1], count)
    return rawstr


def cls():
    from os import system, name
    if name == "nt":
        system("cls")
    else:
        return system("clear")