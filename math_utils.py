# Codigo minimo para green

def es_par(n: int) -> bool:
    if (n%2 == 0):
        return True
    else:
        return False

def es_multiplo_de(n:int , m: int) -> bool:
    if m == 0:
        return False
    return (n % m) == 0
