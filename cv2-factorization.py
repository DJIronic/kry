import math
import random
import time

# Definice funkcí trial_division, pollards_rho a factorize_with_pollards_rho

def trial_division(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    g = 1
    def f(x):
        return (x*x + 1) % n
    while g == 1:
        x = f(x)
        y = f(f(y))
        g = math.gcd(abs(x - y), n)
    if g == n:
        return None
    return g

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

# Měření času
n = 805165465313416541

start_time = time.time()
print("Faktory čísla", n, "metodou primitivního zkoušení:", trial_division(n))
end_time = time.time()
print("Čas primitivního zkoušení:", end_time - start_time, "sekund")

start_time = time.time()
print("Faktor čísla", n, "Pollardovou rho metodou:", pollards_rho(n))
end_time = time.time()
print("Čas Pollardovy rho metody:", end_time - start_time, "sekund")

start_time = time.time()
pollards_factors = factorize_with_pollards_rho(n)
end_time = time.time()
print("Faktor(y) čísla", n, "Pollardovou rho metodou s dodatečnou faktorizací:", pollards_factors)
print("Čas Pollardovy rho metody s dodatečnou faktorizací:", end_time - start_time, "sekund")
