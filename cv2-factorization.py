import math
import random
import time

def trial_division(n):
    factors = []
    #Overime delitelnost 2 a pripadne pridame 2 jako faktor
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    #provedeme cyklus od 3 do 2 s krokem 2, pokud delitelne beze zbytku, pridame faktor
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def pollards_rho(n):
    #overime delitelnost 2
    if n % 2 == 0:
        return 2
    #generace nahodnych cisel x a y
    x = random.randint(2, n - 1)
    y = x
    g = 1
    #definice uzite funkce pro pollardovu metodu
    def f(x):
        return (x*x + 1) % n
    while g == 1:
        x = f(x)
        y = f(f(y)) #pro y spustime funkci dvakrat za sebou, tim vznikne druha ciselna rada, ktera utika te prvni (postup zelvy a kralika)
        g = math.gcd(abs(x - y), n)
    if g == n:
        return None
    return g

#Nasledna primitivni faktorizace po provedeni pollardovi metody pro rozdeleni pripadneho slozeneho cisla
def factorize_with_pollards_rho(n):
    factor = pollards_rho(n)
    if factor is None:
        return [n]
    if factor == n:
        return [n]
    factors = trial_division(factor)
    if len(factors) == 1 and factors[0] == factor:
        return [factor]
    else:
        return factors


n = 4242731 #rozkladana hodnota
start_time = time.time()
print("\n")
print("Faktory čísla", n, "metodou primitivního zkoušení:", trial_division(n))
end_time = time.time()
print("Čas primitivního zkoušení:", end_time - start_time, "sekund")

start_time = time.time()
print("\n")
print("Faktor čísla", n, "Pollardovou rho metodou:", pollards_rho(n))
end_time = time.time()
print("Čas Pollardovy rho metody:", end_time - start_time, "sekund")

start_time = time.time()
pollards_factors = factorize_with_pollards_rho(n)
end_time = time.time()
print("\n")
print("Faktor(y) čísla", n, "Pollardovou rho metodou s dodatečnou faktorizací:", pollards_factors)
print("Čas Pollardovy rho metody s dodatečnou faktorizací:", end_time - start_time, "sekund")
