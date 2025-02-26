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
    return count 


if __name__=="__main__":
    vows = "aeiouAEIOU" # se crea un string con las vocales en mayusculas y minusculas
    sonants = "bcdfghjklmnfpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" # se crea un strig con las consonantes en mayusculas y minusculas
    count_vow : int = sum(mailinbox.count(vow) for vow in vows) # por medio de la función de sumatoria se hace un contador de la recurrencia de los caracteres en el string de vocales
    count_sonant : int = sum(mailinbox.count(sonant) for sonant in sonants) # por medio de la función de sumatoria se hace un contador de la recurrencia de los caracteres en el string de consonantes
    print(f"En total se presentan vocales {count_vow} cantidad de veces")
    print(f"En total se presentan consonantes {count_vow} cantidad de veces")
    print(f"{print(counting_rep_words(mailinbox).most_common(50))}")

    # En caso que se desee se pregunta al usuario si desea ver el .txt
    showinbox : str = input("¿Desea ver el texto de la bandeja de entrada del correo? \n¿y/n?")
    if showinbox == "y":
        print(mailinbox[:])
    else:
        print(None)
