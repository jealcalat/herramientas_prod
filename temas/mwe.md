# MWE: minimal working example

Un MWE es un ejemplo que se pueda ejecutar y que muestre el problema que se quiere resolver con la mínima cantidad de código posible. Por ejemplo, supongamos que queremos preguntar en StackOverflow cómo hacer un gráfico de dispersión en R y ajustar una línea recta. Un MWE sería el siguiente:

```r
# Generar datos
x <- rnorm(100)
y <- 2*x + rnorm(100)

# Ajustar modelo
mod <- lm(y ~ x)

# Graficar
plot(x, y)
# Agregar línea de ajuste
# ???
```

El código que compartamos en nuestra pregunta debe tener tres características:

1. Debe ser reproducible. Es decir, debe poder ejecutarse en cualquier computadora sin errores.
2. Debe ser mínimo. Es decir, debe tener la mínima cantidad de código posible para mostrar el problema.
3. Debe ser completo. Es decir, debe incluir todo el código necesario para reproducir el problema.

El siguiente sería un mal ejemplo. ¿Por qué?

```python
x = np.random.randn(100)
y = 2*x + np.random.randn(100)
plt.scatter(x, y)
```

El siguiente sería un mejor ejemplo. ¿Por qué?

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = 2*x + np.random.randn(100)
plt.scatter(x, y)
```

**Para escribir código que sea reproducible:**

*Describe el problema* 

"No funciona" no es lo suficientemente descriptivo como para ayudar a las personas a comprender tu problema. En su lugar, diles a otros lectores cuál debería ser el comportamiento *esperado*. Diles a otros lectores cuál es la redacción exacta del mensaje de error y qué línea de código lo genera. Utiliza un resumen *breve* pero descriptivo de tu problema como título de su pregunta.

*Elimine cualquier asunto que no sea relevante para el problema*

Si tu código depende de un archivo de datos, un paquete o una biblioteca, asegúrese de que el código que compartes incluya una forma de acceder a esos datos o paquetes, o coloca una copia de datos mínima dentro de tu pregunta, o en un link a un repositorio de GitHub.

*Verifica que tu ejemplo reproduce el problema* 

Si solucionaste el problema sin darte cuenta mientras redactabas el ejemplo pero no lo volviste a probar, querrás saberlo antes de pedirle ayuda a otra persona.

**Para escribir código que sea mínimo:**

*Reiniciar desde cero*

Crea un nuevo programa y agrega solo lo necesario para ver el problema. Utiliza nombres simples y descriptivos para funciones y variables; no copies los nombres que estás utilizando en su código existente.

*Divide y conquistaras*

Si no estás seguro de cuál es el origen del problema, comienza a eliminar el código poco a poco hasta que el problema desaparezca y luego vuelva a agregar la última parte.

**Para escribir código que sea completo:**


No uses imágenes de código. Copia el texto real de tu editor de código, pégalo en la pregunta y luego formatealo como código.

Usa bloques de código individuales para cada archivo o fragmento que incluyas. Proporciona una descripción del propósito de cada bloque.

## Ejemplos de MWEs con buen resultado:

[Ejemplo 1](https://stackoverflow.com/questions/63352807/r-maximum-likelihood-estimation-of-a-exponential-mixture-using-optim): estimar parámetros de una mezcla de distribuciones exponenciales. En dicho ejemplo, coloqué la ecuación del modelo que quería ajustar, mi intento fallido de solución y los datos que utilicé para probar mi código (una simulación). La primera respuesta que me dieron me indicó el error que estaba cometiendo y me dio una solución. La segunda respuesta me dio una solución alternativa usando un paquete de R diferente del que yo estaba usando.

[Ejemplo 2](https://stackoverflow.com/questions/73479169/find-the-break-point-and-compare-slopes?rq=3): encontrar breakpoints en una serie de datos. El autor compartió el conjunto de datos con el que estaba trabajando, posteriormente ajusto una función y mostró el gráfico. Luego planteó su problema de forma concisa y el resultado esperado. Recibió dos respuestas que resolvían, de forma diferente, su problema.

[Ejemplo 3](https://stackoverflow.com/questions/47880875/column-of-sequence-with-repeated-elements-based-on-column-with-dates): crear una nueva columna de sesiones a partir de fechas únicas. Coloqué el data.frame para reproducir el problema, el código que estaba utilizando y el resultado esperado. Había más de una respuesta correcta.

[Ejemplo 4](https://stackoverflow.com/questions/52480904/broken-stick-or-piecewise-regression-with-2-breakpoints): ajustar un modelo de regresión con dos puntos de quiebre. Coloqué el código que estaba utilizando, un breve contexto del problema y el resultado esperado en forma de imagen. Un usuario preguntó de dónde venían esos datos, pero en este caso particular eso era irrelevante. Al final, me dieron más de dos respuestas que resolvían mi problema aunque con diferente grado de satisfacción.

Los anteriores consejos quizá también funcionarían en ChatGpt, solo que con su actual capacidad, el resultado esperado no puede ser una imagen, de forma que tendríamos que plantearlo en forma de texto.

## Hacer un ejercicio de MWE en R/Python aplicable a sus datos