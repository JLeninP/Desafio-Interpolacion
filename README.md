---
title: "Desafio Interpolación"
subtitle: ""
author: "Lenin Pocoaca"
date: "10-10-24"
---

# Grados de ebullición del agua a una altura $x$ sobre el nivel del mar.

Para esto se determinara una ecuación lineal que se ajuste mejor a los siguientes datos:

|Altura($ft$)|Temperatura($ºF$)|
|:-:|:-:|
|-1000|213.9|
|0|212|
|3000|206.2|
|8000|196.2|
|15000|184.4|
|22000|172.6|
|28000|163.1|

dicha ecuación se usará para hallar un valor aproximado de los grados de ebullición del agua para las siguientes alturas:

* 16404.2ft
* 11942.26ft (Altura de la ciudad de La Paz - Bolivia)
* 13615.49ft (Altura de la ciudad de El Alto - Bolivia)

Mediante polinomios de interpolación se hallara un polinomio $P(x)$ que se aproxime mejor a la función $f(x)$ (función desconocida), para hallar la temperatura a una altura $x_i$.

## Polinomio de Interpolación de Lgrange
Este polinomio esta determinado por:

$$P(X) = f(x_0)L{n,0}(x) + \cdots + f(x_n)L_{n,n}(x)$$

donde, para cada $k=0, 1, ..., n$

$$L{n,k}(x)=\frac{(x-x_0)(x-x_1)\cdots(x-x_{k-1})(x-x_{k+1})\cdots(x_k-x_n)}{(x_k-x_0)(x_k-x_1)\cdots(x_k-x_{k-1})(x_k-x_{k+1})\cdots(x_k-x_n)}$$
 ### Solución implementada en python
 ```{python}
import sys

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

X = [-1000, 0, 3000, 8000, 15000, 22000, 28000]
Y = [213.9, 212, 206.2, 196.2, 184.4, 172.6, 163.1]

xk1 = 16404.2
xk2 = 11942.26
xk3 = 13615.49

sys.stdout.write(f'\n==================SOLUCIÓN==================\n')

sys.stdout.write(f'\nPara 5000m:')
sys.stdout.write(f'\nAltura(m) = {str(xk1)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(interpLagrange(X, Y, xk1))}\n')

sys.stdout.write(f'\nPara la ciudad de La Paz:')
sys.stdout.write(f'\nAltura(m) = {str(xk2)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(interpLagrange(X, Y, xk2))}\n')

sys.stdout.write(f'\nPara la ciudad de El Alto:')
sys.stdout.write(f'\nAltura(m) = {str(xk2)}')
sys.stdout.write(f'\nTemperatura(ºF) = {str(interpLagrange(X, Y, xk3))}\n')
 ```
Se obtienen los siguientes resultados:
```{python}
==================SOLUCIÓN==================

Para 5000m:
Altura(m) = 16404.2
Temperatura(ºF) = 182.27643178207313

Para la ciudad de La Paz:
Altura(m) = 11942.26
Temperatura(ºF) = 189.1581716811097

Para la ciudad de El Alto:
Altura(m) = 11942.26
Temperatura(ºF) = 186.5054507665994
```

## Diferencias divididas de Newton

### Solución implementada en excel

