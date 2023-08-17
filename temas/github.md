# GitHub

GitHub es una plataforma de desarrollo colaborativo para alojar proyectos utilizando el sistema de control de versiones Git. El código se almacena de forma pública, aunque también los repositorios pueden ser privados. La plataforma permite que varios programadores trabajen en equipo sobre un mismo código y que puedan corregir errores, copiar el código de otros repositorios y enviar sus propias modificaciones al servidor original.

## ¿Qué es Git?

Git es un sistema de control de versiones distribuido, gratuito y de código abierto. Su principal utilidad es llevar un registro de los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que sea posible recuperar versiones específicas más adelante.

## ¿Qué es un repositorio?

Un repositorio es un espacio donde se almacenan los archivos de un proyecto. Puede estar ubicado en el disco duro de un ordenador local o en un servidor remoto. Un repositorio remoto es un repositorio alojado en Internet, en algún servicio de almacenamiento como GitHub, Bitbucket o GitLab.

Los repositorios pueden ser copiados (clonados) de un servidor a otro, de modo que se pueda trabajar en ellos de forma remota. En este caso, el repositorio remoto, en un servidor como GitHub, se considera el repositorio principal, mientras que el repositorio local es una copia del mismo.

Estos repositorios pueden ser usados de forma colaborativa o individual. En el caso de los repositorios individuales, un desarrollador puede trabajar en un proyecto en varios ordenadores, sincronizando los cambios entre ellos. Esta es una de las principales ventajas que veo que un científico se familiarice con Git y GitHub, ya que puede trabajar en un proyecto en su ordenador de trabajo, en su ordenador personal, en el portátil, etc. y mantener todos los repositorios sincronizados. 

Si, por ejemplo, su trabajo involucra análisis de datos rutinarios (por ejemplo, procesar archivos de MED crudos, estandarizados con la misma estructura), tener un repositorio con los scripts de análisis y los datos en GitHub, le permitirá acceder a ellos desde cualquier ordenador, y mantenerlos sincronizados, y además, si en algún momento necesita compartirlos con alguien, o si él mismo necesita esos mismos scripts en un futuro, puede hacerlo de forma sencilla, y además los scripts de análisis siempre estarán actualizados. Y si quiere volver a una versión anterior, también puede hacerlo fácilmente buscando en el historial de cambios.

Tanto en R como en Python, un investigador o un laboratorio podrían tener sus propios paquetes o módulos, que contengan funciones que se usan de forma rutinaria, y que se pueden compartir entre los miembros del grupo. Estos paquetes o módulos pueden ser almacenados en GitHub, y cada miembro del grupo puede instalarlos en su ordenador. DE esta manera en un mismo laboratorio se podrían tener estándares tanto de bases de datos como de análisis. 

## GitHub desktop

GitHub desktop es una aplicación que permite trabajar con repositorios de GitHub de forma gráfica, sin necesidad de usar la línea de comandos. Manejar comandos puede ser intimidante para algunos usuarios, y GitHub desktop es una buena alternativa para ellos. Es la herramienta que estaremos usando en este curso.