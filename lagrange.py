import sys
import math
def interpLagrange(X, Y, xk):
    res = 0
    n = len(X)
    L = [1]*(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i] *= (xk - X[j])/(X[i] - X[j]) 
        res += Y[i] * L[i]
    return res

def error(X, xk, yk):
    E = 1
    n = len(X)
    L = 1
    for j in range(n):
        L *= (xk - X[j])/(xk - X[j]) 
    for j in range(n):
        E *= L/ math.factorial(n+1) * (xk - X[j])
    return L

X = [-1000, 0, 3000, 8000, 15000, 22000, 28000]
Y = [213.9, 212, 206.2, 196.2, 184.4, 172.6, 163.1]

xk1 = 16404.2
xk2 = 11942.26
xk3 = 13615.49

yk1 = interpLagrange(X, Y, xk1)
yk2 = interpLagrange(X, Y, xk2)
yk3 = interpLagrange(X, Y, xk3)

sys.stdout.write(f'\n==================SOLUCIÓN==================\n')

sys.stdout.write(f'\nPara 5000m:')
sys.stdout.write(f'\nAltura(m) = {str(xk1)} + {error(X, xk1, yk1)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(yk1)}\n')

sys.stdout.write(f'\nPara la ciudad de La Paz:')
sys.stdout.write(f'\nAltura(m) = {str(xk2)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(yk1)}\n')

sys.stdout.write(f'\nPara la ciudad de El Alto:')
sys.stdout.write(f'\nAltura(m) = {str(xk2)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(yk3)}\n')

