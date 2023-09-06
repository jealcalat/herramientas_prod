#%% importar matplotlib, pandas, numpy y seaborn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#%%
# realizar una función para normalizar x
def normalizar(x):
    x_norm = (x - x.mean()) / x.std()
    return x_norm
  
#%% Crear una función para graficar x con un histograma

def graficar(x):
    plt.hist(x)
    plt.show()
    
x = np.random.normal(0, 1, 1000)
graficar(x)
#%%    
# Crear una función para hacer un histograma de x; 
# la función debe llamarse histograma y debe tener un argumento x; 
# debe verificar que x sea numérico y si no lo es, debe imprimir un mensaje de error;
# como título, debe decir "Histograma de x" y como etiqueta del eje x debe decir "x", 
# y del eje y debe decir "Frecuencia"

def histograma(x):
    if isinstance(x, (int, float, complex)):
        print("Error: x no es numérico")
    else:
        plt.hist(x)
        plt.title("Histograma de x")
        plt.xlabel("x")
        plt.ylabel("Frecuencia")
        plt.show()

histograma(x)
# %% cargar el conjunto de datos Iris desde seaborn y explorarlo con head, info y describe

iris = sns.load_dataset("iris")
iris.head()
iris.info()
iris.describe()

# %% crear un pairsplot de iris con seaborn

sns.pairplot(iris)

# %% crear función que simule el modelo de Rescorla-Wagner para adquisición de condicionamiento clásico

# def rescorla_wagner(n_trials, alpha, beta, lambda_):
#     v = np.zeros(n_trials)
#     delta = np.zeros(n_trials)
#     for i in range(1, n_trials):
#         delta[i] = lambda_ - v[i - 1]
#         v[i] = v[i - 1] + beta * alpha * delta[i]
#     return v
  
def rescorla_wagner(n, alpha, beta, reforzamiento):
    V = [0]
    for i in range(1, n):
        deltaV = alpha * beta * (reforzamiento[i] - V[i-1])
        V.append(V[i-1] + deltaV)
    return V
  
# %% simular el modelo de Rescorla-Wagner con alpha = 0.1, beta = 0.5, lambda = 1 y 100 trials

reforzamiento = np.ones(100)
v = rescorla_wagner(100, 0.1, 0.5, reforzamiento)
# graficar
plt.plot(v)
plt.xlabel("Trial")
plt.ylabel("V")
plt.show()
# %% simular con reforzamiento proveniente de una binomial con p = 0.5

reforzamiento = np.random.binomial(1, 0.5, 100)
v = rescorla_wagner(100, 0.1, 0.5, reforzamiento)
# graficar
plt.plot(v)
plt.xlabel("Trial")
plt.ylabel("V")

# %%
