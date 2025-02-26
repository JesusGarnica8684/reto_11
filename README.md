# Reto 11
1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
  * endswith() es un método para Strings en python que valora si una cadena termina en una secuencia específica, su sintaxis es:
    ```python
    string.endswith(value)
    ```
    Extraído de <a href="https://www.w3schools.com/python/ref_string_endswith.asp">referencia 1.</a>
    Por ejemplo:
    ```python
    red : str = "endswith() valora el que termina el string y regresa un booleano."
    flag = red.endswith("booleano.")
    print(flag)
    ```
  * startswith() así mismo con endswith() valora que un String tenga una secuencia específica, pero en este caso inicie como el valor que se ingresa.
    ```python
    red : str = "startswith() valora el que empieza el string y regresa un booleano."
    flag = red.startswith("starts")
    print(flag)
    ```
  * isalpha() valora que el string este compuesta solo de valores del alfabeto.
     ```python
    notalfa : str = "Esta cadena tiene numeros, deberia dar f4ls3."
    flag = notalfa.isalpha()
    print(flag)
    ``` 
  * isalnum() valora que el string este compuesta de solo valores alfanuméricos.
    ```python
    alfanumstr : str = "3st4 c4d3n4 3s 4lf4num3r1c4 deberia dar True"
    flag = alfanumstr.isalnum()
    print(flag)
    ```
  * isdigit() valora que el string este compuesta de solo valores numéricos.
    ```python
    numstr : str = "3434343414"
    flag = numstr.isalnum()
    print(flag)
    ```
  * isspace() valora que el string sea solo espacios.
    ```python
    nullstr : str = "    "
    flag = nullstr.isspace()
    print(flag)
    ```
  * istitle() valora si la cadena sigue el patrón del título, para esto cada palabra debe iniciar con mayúscula.
    ```python
    titlestr : str = "Acerca De La Ontologia Del Ser:"
    flag = titlestr.isspace()
    print(flag)
    ```
  * islower() revisa que todos los caracteres estén en minúsculas.
    ```python
    lowerstr : str = "acerca de la ontologia del ser:"
    flag = lowerstr.islower()
    print(flag)
    ```
  * isupper() revisa que todos los caracteres estén en mayúsculas.
    ```python
    upperstr : str = "ACERCA DE LA ONTOLOGIA DEL SER:"
    flag = upperstr.isupper()
    print(flag)
    ```
2. Procesar el <a href="https://www.py4e.com/code3/mbox.txt">archivo</a> y extraer:
 - Cantidad de vocales
 - Cantidad de consonantes
 - Listado de las 50 palabras que más se repiten

```python
import urllib.request
from collections import Counter
import re

url = "https://www.py4e.com/code3/mbox.txt"#guardo el url donde esta el .txt en una variable
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
)#Debido a que seguía apareciendo error al descargar el url, se utilizó un user agent para acceder al archivo y que no se bloqueara la accion.
harvest = urllib.request.urlopen(req) #recoge la informacion que se obtiene de la descarga
data = harvest.read() #guarda los datos del .txt en lenguaje maquina
mailinbox = data.decode("utf-8") #decodifica los datos a lenguaje de alto nivel con utf-8

def counting_rep_words (text : str): # se ingresa un string
    wpertext = re.findall(r"\b\w+\b", text.lower())  # se utiliza la funcion re.findall() para separar por un patrón regular las palabras, se 
    #utiliza el metodo lower para pasar todo a minusculas y no preocuparse por sensibilidad a mayusculas.
    count = Counter(wpertext) # cuenta la frecuencia de cada palabra
    return count # es un diccionario con las iteraciones de cada palabra en el texto las keys seran las palabras, sus valores asignados será la iteración en código 


if __name__=="__main__":
    vows = "aeiouAEIOU" # se crea un string con las vocales en mayusculas y minusculas
    sonants = "bcdfghjklmnfpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" # se crea un strig con las consonantes en mayusculas y minusculas
    count_vow : int = sum(mailinbox.count(vow) for vow in vows) # por medio de la función de sumatoria se hace un contador de la recurrencia de los caracteres en el string de vocales
    count_sonant : int = sum(mailinbox.count(sonant) for sonant in sonants) # por medio de la función de sumatoria se hace un contador de la recurrencia de los caracteres en el string de consonantes
    print(f"En total se presentan vocales {count_vow} cantidad de veces")
    print(f"En total se presentan consonantes {count_vow} cantidad de veces")
    print(f"{print(counting_rep_words(mailinbox).most_common(50))}")# con el diccionario se llama el modulo most_common de counting para encontrar los 50 elementos con mas iteracion en el diccionario

    # En caso que se desee se pregunta al usuario si desea ver el .txt
    showinbox : str = input("¿Desea ver el texto de la bandeja de entrada del correo? \n¿y/n?")
    if showinbox == "y":
        print(mailinbox[:])
    else:
        print(None)

```
