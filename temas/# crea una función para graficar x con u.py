# crea una función para graficar x con un histograma

import matplotlib.pyplot as plt

def graficar(x):
    plt.hist(x)
    plt.show()
    
x = [1, 2, 1, 3, 3, 1, 2, 1, 5, 1]

graficar(x)


# Crear una función para hacer un histograma de x; 
# la función debe llamarse histograma y debe tener un argumento x; 
# debe verificar que x sea numérico y si no lo es, debe imprimir un mensaje de error;
# como título, debe decir "histograma de x" y como etiqueta del eje x debe decir "x", 
# y del eje y debe decir "Frecuencia"

def histograma(x):
    if type(x) == int or type(x) == float:
        plt.hist(x)
        plt.title("Histograma de x")
        plt.xlabel("x")
        plt.ylabel("Frecuencia")
        plt.show()
    else:
        print("Error: x debe ser numérico")
        
x = [1, 2, 1, 3, 3, 1, 2, 1, 5, 1]

histograma(x)


segundos = 10000
minutos = segundos / 60
horas = minutos / 60
dias = horas / 24
semanas = dias / 7



#%% crear una función que simule el modelo de Rescorla-Wagner con los siguientes argumentos:
# n: número de ensayos
# alfa: learning rate
# beta: saliencia del estímulo
# reforzamiento: lista de 1s y 0s
# la ecuación elemental es: deltaVi = alfa * beta * (reforzamiento - V[i-1])
# la ecuación de actualización es: Vi = V[i-1] + deltaVi

def rescorla_wagner(n, alfa, beta, reforzamiento):
    V = [0]
    for i in range(1, n):
        deltaVi = alfa * beta * (reforzamiento[i] - V[i-1])
        Vi = V[i-1] + deltaVi
        V.append(Vi)
    return V
  
#%%

import numpy as np
import matplotlib.pyplot as plt

n = 100
alfa = 0.1
beta = 0.5
reforzamiento = np.ones(n)

V = rescorla_wagner(n, alfa, beta, reforzamiento)
x = np.arange(0, n, 1)
plt.plot(x, V)
# %% crear vector de reforzamiento con una distribución binomial
n=100000
reforzamiento = np.random.binomial(1, 0.5, n)
V = rescorla_wagner(n, alfa, beta, reforzamiento)
x = np.arange(0, n, 1)
plt.plot(x, V)
# %%
# simular para k animales, luego promediar todas las simulaciones; graficar cada simulación individual con gris transparente, y el promedio de todas ellas en rojo

k = 100
n = 100
alfa = 0.1
beta = 0.5
V = np.zeros((k, n))
for i in range(k):
    reforzamiento = np.random.binomial(1, 0.5, n)
    V[i, :] = rescorla_wagner(n, alfa, beta, reforzamiento)
    x = np.arange(0, n, 1)
    plt.plot(x, V[i, :], color="gray", alpha=0.1)
    
plt.plot(x, np.mean(V, axis=0), color="red")
# %%
# simular extinción para la mitad de los ensayos; es decir, para la mitad de n, el reforzamiento es 1, y para la otra mitad es 0

n = 100
alfa = 0.6
beta = 0.5
reforzamiento = np.concatenate((np.ones(int(n/2)), np.zeros(int(n/2))))

V = rescorla_wagner(n, alfa, beta, reforzamiento)
x = np.arange(0, n, 1)
plt.plot(x, V)
# %%
