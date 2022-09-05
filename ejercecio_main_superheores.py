'''
Desafío #00:

A)Analizar detenidamente el set de datos
B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
D)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
G)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
H)Calcular e informar cual es el superhéroe más y menos pesado.
I)Ordenar el código implementando una función para cada uno de los valores informados.
J)Construir un menú que permita elegir qué dato obtener

{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
},

'''
from data_stark import lista_personajes

#B)Recorrer La lista Imprimendo El Nombre Por consola :
def imprimir_todos_nombres():
        
        for imprimir_nombre in lista_personajes :
            print(imprimir_nombre["nombre"])

#C) Recorre la lista Imprimiento el nombre y la altura por consola 
def imprimir_nombres_y_alturas ():
    for imprimir_nombre in lista_personajes :
        print(imprimir_nombre["nombre"],imprimir_nombre["altura"])


#D)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto () :
    heroe_de_maxima_altura = lista_personajes[0]
    for imprimir_nombre in lista_personajes :
                if( float(imprimir_nombre["altura"]) > float (heroe_de_maxima_altura["altura"]) ):
                    heroe_de_maxima_altura = imprimir_nombre
    print("el heroe mas alto es " , heroe_de_maxima_altura["nombre"] ,"la altura del heroe es : " , heroe_de_maxima_altura["altura"])

#E) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO) 
def heroe_mas_Bajo () :
    heroe_de_minima_altura = lista_personajes[0]
    for imprimir_nombre in lista_personajes :
                if( float(imprimir_nombre["altura"]) < float (heroe_de_minima_altura["altura"]) ):
                    heroe_de_minima_altura = imprimir_nombre
    print("el heroe mas bajo es " , heroe_de_minima_altura["nombre"] ,"la altura del heroe es : " , heroe_de_minima_altura["altura"])

#F)F)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
def definir_promedio_de_altura ():
    cantidad_heroes = 0
    acumulador_altura = 0
    for imprimir_nombre in lista_personajes :
        acumulador_altura =float (acumulador_altura) + float (imprimir_nombre["altura"])
        cantidad_heroes+= 1
    print("el promedio de altura es " ,   acumulador_altura / cantidad_heroes)

#G)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)  
    def definir_altura_mas_bajo_y_mas_alto ():
        heroe_mas_alto()
        heroe_mas_Bajo()

#H)Calcular e informar cual es el superhéroe más y menos pesado.


def heroe_mas_liviano():
    heroe_de_minimo_peso = lista_personajes[0]
    for imprimir_nombre in lista_personajes:
        if(float(imprimir_nombre["peso"]) < float(heroe_de_minimo_peso["peso"])):
            heroe_de_minimo_peso = imprimir_nombre
    print("el heroe menos pesado  es ",
        heroe_de_minimo_peso["nombre"], "el peso  del heroe es : ", heroe_de_minimo_peso["peso"])

def heroe_mas_pesado():
    heroe_de_maximo_peso = lista_personajes[0]
    for imprimir_nombre in lista_personajes:
        if(float(imprimir_nombre["peso"]) > float(heroe_de_maximo_peso["peso"])):
            heroe_de_maximo_peso = imprimir_nombre
    print("el heroe mas pesado  es ",
        heroe_de_maximo_peso["nombre"], "el peso  del heroe es : ", heroe_de_maximo_peso["peso"])


while(True):
    mensaje =  ''' 
                B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
                C)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
                D)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
                E)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
                F)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
                G)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
                H)Calcular e informar cual es el superhéroe más y menos pesado.
                I)Pulse N para salir.
                '''
    print(mensaje)

    respuesta=input("ingrese un valor : ")
    if (respuesta =="B"):
        imprimir_todos_nombres()
    elif(respuesta =="C" ) :
        imprimir_nombres_y_alturas ()
    elif(respuesta =="D" ):
        heroe_mas_alto ()
    elif(respuesta =="E" ):
        heroe_mas_Bajo ()
    elif(respuesta =="F" ): 
        definir_promedio_de_altura ()
    elif(respuesta =="H" ):
        heroe_mas_pesado()
        heroe_mas_liviano()
    elif(respuesta=="N"):
        break    
