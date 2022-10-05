'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    
    lista_personajes = funciones.cargar_json("C:/Users/Electro PC/Desktop/promacion_l/data.json")
    lista_para_archivo = lista_personajes.copy()
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            key = "height"
            mostrar_csv = key
            lista_para_archivo = funciones.mostrar(lista_personajes,"height")
        elif(respuesta=="2"):
            key = "height"
            mostrar_csv = key
            lista_para_archivo=funciones.sort_ordenamiento_personaje(lista_personajes,"height","asc")
            funciones.mostrar(lista_para_archivo,"height")
        elif(respuesta=="3"):
            key = "mass"
            mostrar_csv = key
            lista_para_archivo=funciones.sort_ordenamiento_personaje(lista_personajes,key,"desc")
            funciones.mostrar(lista_para_archivo,"mass")
        elif(respuesta=="4"):
            buscador = input("ingrese un heroe para buscar ")
            funciones.buscar_heroes(lista_personajes,buscador)
        elif(respuesta=="5"):
            mostrar_csv = key
            funciones.exportar_arvhivo(lista_para_archivo,"C:/Users/Electro PC/Desktop/promacion_l/data.csv",mostrar_csv)
        elif(respuesta=="6"):
            break


starwars_app()
#lista_personajes = funciones.cargar_json("C:/Users/Electro PC/Desktop/promacion_l/data.json")
#print(lista_personajes)
#print(funciones.buscar_peronsaje_mas_alto(lista_personajes,"height"))
