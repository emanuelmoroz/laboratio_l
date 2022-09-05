
'''En la base de datos de la división de armamento de industrias Wayne se tiene una información la cual están con la necesidad de cambiar el formato la lista de habilidades
con sus respectivos puntos de combate, actualmente cada una de ellas está presente como un diccionario pero para su nuevo sistema requieren que el tipo de dato sea una tupla la 
cual albergue solamente el nombre de la habilidad y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de las habilidades deben estar dentro de una lista de habilidades, 
la cual debe ser el valor de una key que conforme un diccionario, como key par albergarlas usaremos “habilidades_UTN”.
Formato de resultado esperado:

{
"habilidades_UTN": [("habilidad_alfa", número), ("habilidad_beta", número)] etc.
}

Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores de manera ordenada y prolija, conjuntamente con la key que integra dicha estructura de datos.

EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.'''


from collections import _OrderedDictItemsView
from re import L
from typing import OrderedDict


habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }

]
lista_nueva = []

for tupla in habilidades:
    clave_nombre = tupla['Nombre'] , tupla['Poder']  
    nuevas_claves = (clave_nombre) 
    lista_nueva.append(nuevas_claves)

tupla = tuple(lista_nueva)
habilidades_UTN = {'Habilidades_UTN': tupla}
habilidad_utn = habilidades_UTN["Habilidades_UTN"]

print("habilidades_UTN:")
contador = 1
for habilidad_y_poder in habilidad_utn:
    print("habilidad :" , contador ,":", habilidad_y_poder[0], "|" , "poder :",habilidad_y_poder[1])
    contador += 1
