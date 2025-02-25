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
