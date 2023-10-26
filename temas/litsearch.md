# Herramientas para la búsqueda y descubrimiento de literatura

## 1. Semantic scholar

A través de *Research feeds* se pueden crear alertas de nuevos artículos que contengan ciertas palabras clave. Los algoritmos de semantic scholar aprenden de unas cuantas muestras que guardemos en nuestra biblioteca personal. De su FAQ:

> **How does Semantic Scholar work?**
> Semantic Scholar uses machine learning techniques to extract meaning and identify connections from within papers, then surfaces these insights to help scholars gain an in-depth understanding quickly.

Según la página, están trabajando en un sistema de preguntas y respuestas basado en gpt-3.5.

## 2. Connected papers. 

Es otra herramienta de exploración de artículos. Se puede buscar por título, DOI o palabras clave. Crea un grafo de artículos relacionados por su similitud. También, las búsquedas se pueden guardar en archivos .bib y cargarse en Zotero.

Por ejemplo:
10.1038/s42003-022-04080-7

## 3. Google scholar

Las búsquedas de GS no son tan refinadas como las de Semantic Scholar, pero se pueden usar los operadores booleanos y los filtros de fecha. También se pueden crear alertas de nuevos artículos.

Por ejemplo, para buscar artículos de habit formation, toluene, inhalants se tienen las siguientes opciones

*Búsqueda simple*

```
habit formation toluene inhalants
```

*Búsqueda de todos los términos*

```
+habit +formation +toluene +inhalants
```

*Búsqueda de términos exactos*

```
"habit formation" "toluene" "inhalants"
```

*Búsqueda de términos exactos con operadores booleanos*

```
"habit formation" AND "toluene" AND "inhalants" NOT "mice"
```

*Allintitle*: busca términos en el título. Por ejemplo, para buscar *habit formation* en el título y *inhalants* en cualquier parte del artículo, se usa el operador *allintitle*:

```
allintitle: "habit formation" inhalants
```

*intitle*: busca términos en el título. Por ejemplo, para buscar *habit formation* en el título y *inhalants* en cualquier parte del artículo, se usa el operador *intitle*:

```
intitle: "habit formation" inhalants
```

*Búsqueda con exclusión de términos*

```
habit formation toluene inhalants -clinical
```

*Around*: busca términos que estén cerca de otros. Por ejemplo, para buscar *habit formation* cerca de *toluene* a una distancia de 5 palabras, se usa el operador *around*:

```
"habit formation" AROUND(5) toluene
```

*Sinónimos ~*: busca términos que sean sinónimos de otros. 

```
~delay discounting
```

*intext*: busca términos en el texto. Por ejemplo, para buscar *habit formation* en el texto y *inhalants* en cualquier parte del artículo, se usa el operador *intext*:

```
intext: "habit formation" inhalants
```

*filetype*: links con especificaciones de tipo de archivo. Por ejemplo, para buscar archivos pdf que contengan *habit formation* y *inhalants*, se usa el operador *filetype*:

```
filetype:pdf "habit formation" inhalants
```

*Operadores booleanos*: OR, AND, - (exclusión)


## 4. Scopus

* Search within: TITLE-ABS-KEY
* Operadores de proximidad: Pre/n, W/n. Por ejemplo, para buscar *deep learning* cerca de *covid* en el título, se puede usar la siguiente búsqueda:

```
TITLE-ABS-KEY ( "deep learning" W/5 covid )
```

Si queremos que *deep learning* esté antes de *covid* por dos palabras, se usa el operador *pre*:

```
TITLE-ABS-KEY ( "deep learning" Pre/2 covid )
```

Diversos campos se pueden combinar con operadores booleanos. POr ejemplo, si quiero buscar qué investigaciones se han hecho con DRL, tolueno y ciclohexano, restringir la búsqueda a artículos, en neurociencias o psicología (porque los de química pura no me interesan):

```
( TITLE-ABS-KEY ( drl ) OR TITLE-ABS-KEY ( "differential reinforcement" ) ) AND ( TITLE-ABS-KEY ( toluene ) OR TITLE-ABS-KEY ( cyclohexane ) OR TITLE-ABS-KEY ( chx ) ) AND ( LIMIT-TO ( SUBJAREA , "NEUR" ) OR LIMIT-TO ( SUBJAREA , "PSYC" ) OR LIMIT-TO ( SUBJAREA , "PHAR" ) ) AND ( LIMIT-TO ( DOCTYPE , "ar" ) )
```

El operador *LIMIT-TO* permite restringir la búsqueda a ciertos campos, que especifico con *DOCTYPE* y *SUBJAREA*.

* Wildcards: * y ?

- `?` representa cualquier caracter singular. `wom?n` buscará woman y women. 
- `*` representa cualquier número de caractéres. `delay disc*` buscará delay discounting, delay discount, delay discounted, etc.

## 5. Pubmed

Búsqueda avanzada. Se pueden usar operadores booleanos (AND, OR, NOT) combinado con diversos campos. 

Scopus:

TITLE-ABS-KEY ( "deeplarning" ) OR TITLE-ABS-KEY ( "deep learning" ) W/4 TITLE-ABS-KEY ( covid ) AND ( LIMIT-TO ( SUBJAREA , "MEDI" ) OR LIMIT-TO ( SUBJAREA , "HEAL" ) ) AND ( LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "cr" ) )


(("exercise"[Text Word] OR "physical activity"[Text Word] AND "depre*"[Text Word] ) AND "Meta-Analysis"[Publication Type] AND "2018/10/25 00:00":"2025/01/01 05:00"[Date - Publication]) AND (y_10[Filter])