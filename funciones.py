import re 
import json



def cargar_json(archivo:str)->list[dict]:

    '''
    recibe un archivo json en forma de str
    lo devuelve en forma de lista 
    '''
    with open(archivo,"r") as  documento :
        resultado_lista = json.load(documento)
        resultado_lista = dict(resultado_lista)
        lista_final=list[dict](resultado_lista["results"])

        return lista_final

def validar_entero(lista:list, key:str)->int:
    '''
    recibe una lista
    con una clave str
    valida la clave para volverla entero
    ''' 
    if lista:
        for personaje in lista:
            clave = personaje[key] 
            clave = int(personaje[key]) 
        return clave

def mostrar(lista:list,key:str):

    '''
    recibe una lista y muestra el nombre 
    y la altura de los personajes 
    '''
    for personaje in lista :
        mensaje = print(f"nombre :{personaje['name']} | {key.capitalize()}  : {personaje[key]} ")

    return mensaje

def buscar_personaje_mas_alto_mas_bajo(lista:list,key:str,modo:str)->str:
    '''
    recibe una lista y una key 
    modo asc o desc
    busca el peronsaje mas alto y lo devuelve 
    '''
    validar_entero(lista,key)
    indice_mas_alto_mas_bajo = 0 
    for i in range(len(lista)) : 
        if modo == "asc" and float(lista[i][key]) < float(lista[indice_mas_alto_mas_bajo][key]) :
            indice_mas_alto_mas_bajo = i
        if modo == "desc" and float(lista[i][key]) >float(lista[indice_mas_alto_mas_bajo][key]) :
            indice_mas_alto_mas_bajo = i
    retorno = indice_mas_alto_mas_bajo
    return retorno

def sort_ordenamiento_personaje(lista:list,key:str,modo:str):
    '''
    recibe una lista y la ordena de menor a mayor 
    dependedienendo de la key
    '''
    lista_copiada = lista.copy()
    print(lista_copiada)
    for i in range(len(lista)):
        indice_mas_alto_mas_bajo = buscar_personaje_mas_alto_mas_bajo(lista_copiada[i:],key,modo)+i
        lista_copiada[i],lista_copiada[indice_mas_alto_mas_bajo] = lista_copiada[indice_mas_alto_mas_bajo],lista_copiada[i]
    return lista_copiada

def exportar_arvhivo(lista:list,path:str,key:str):
    ''' 
    recibe una lista y exporta los datos a csv
    '''
    with open(path,"w") as archivo:
        for personaje in lista:
            archivo.write("nombre :{0} |    {2} | {1}\n".format(personaje["name"],personaje[key],key))


def buscar_heroes(lista:list,buscador:str):
    '''
    recibe una lista y busca si hay un personaje con ese nombre 
    '''
    print("\n")
    for personaje in lista:
        if re.search(buscador,personaje["name"],re.IGNORECASE):
            print("Nombre : {0} |  height :  - {1} | mass : {2} | gender {3} ".format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"]))
    print("\n")
