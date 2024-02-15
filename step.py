def baby_step_giant_step(a, b, p):
    import math

    # Vypočítá velikost kroků
    n = int(math.ceil(math.sqrt(p - 1)))
    print("Počet kroků:", n)

    # Baby steps - vytvoří slovník pro a^j mod p
    baby_steps = {pow(a, j, p): j for j in range(n)}
    
    # Vypočítá a^-n mod p (obří krok)
    c = pow(a, n * (p - 2), p)
    
    # Giant steps - postupně hledá shodu s baby steps
    for i in range(n):
        y = (b * pow(c, i, p)) % p
        if y in baby_steps:
            return i * n + baby_steps[y]

    return None

# Hodnoty pro náš případ
a = 5  #Generátor grupy (základ)
b = 21  #Prvek grupy
p = 107 #Modulo (velikost grupy, prvočíslo)

x = baby_step_giant_step(a, b, p)
print(f"x = {x}")