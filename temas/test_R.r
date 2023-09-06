# Cargar ggplot2
library(ggplot2)

# crear función para normalizar x
normalizar <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

# crear función para histograma de x, con color rojo

histograma <- function(x) {
  return(ggplot(data.frame(x = x), aes(x = x)) + 
           geom_histogram(fill = "red", color = "black") + 
           theme_bw())
}

# probar la función histograma

histograma(1:100)

# crear la función histograma usando los graficos de R base, el histograma debe:
# - tener color rojo
# - Ser stepfilled
# - Tener el título "histrograma de x"

histograma2 <- function(x) {
  return(hist(x, col = "red", main = "histograma de x", freq = FALSE, breaks = "FD", border = "black", xlab = "x", ylab = "Frecuencia"))
}

