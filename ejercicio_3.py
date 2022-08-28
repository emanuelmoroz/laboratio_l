''' 

La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes,
para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
El sexo y nombre de Heroe | Heroína de mayor edad.
La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
El promedio de edad entre Heroinas.
El promedio de edad entre Heroes de fuerza.

'''

bandera_edad_heroe_mayor=True
acumulador_de_edad_Heroinas = 0  
acumulador_de_heroes_fuerza = 0
contador_de_heroinas = 0
contador_de_heroes_fuerza = 0 
contador_de_heroinas_confym = 0

while(True) : 

        nombre_heroe=input("ingrese nombre de heroe / heroina por favor ")
        while (True):
                edad_heroe = int(input('ingrese edad : ')) 
                if(edad_heroe < 17) : 
                        edad_heroe = int(input('ingrese edad : ')) 
                        break

        sexo = input("ingrese sexo por favor  : 'm' , 'f' o 'nb' ")
        while(sexo!="m" and sexo != "f" and sexo != "nb") : 
                        sexo = input("ingrese sexo por favor  : 'm' , 'f' o 'nb' ")

        habilidad_heroe = (input("ingrese habilidad del heroe por favor : 'fuerza' , 'magia' o 'inteligencia'"))
        while(habilidad_heroe !="fuerza" and habilidad_heroe != "magia" != habilidad_heroe != "inteligencia"):
                        habilidad_heroe = (input("ingrese habilidad del heroe por favor : 'fuerza' , 'magia' o 'inteligencia'"))

        if(bandera_edad_heroe_mayor==True):
                edad_mayor_heroe = edad_heroe
                nombre_mayor_heroe=nombre_heroe
                bandera_edad_heroe_mayor=False
        elif(edad_mayor_heroe < edad_heroe):
                edad_mayor_heroe = edad_heroe
                nombre_mayor_heroe = nombre_heroe   


        if(habilidad_heroe == "fuerza"):
                nombre_heroe_mas_joven_fuerza = nombre_heroe
                edad_heroe_mas_joven_de_fuerza = edad_heroe
                acumulador_de_heroes_fuerza=acumulador_de_heroes_fuerza + edad_heroe
                contador_de_heroes_fuerza += 1
                if(edad_heroe < edad_heroe_mas_joven_de_fuerza):
                        nombre_heroe_mas_joven_fuerza = nombre_heroe
                        edad_heroe_mas_joven_de_fuerza = edad_heroe   

        if(sexo=="f"):
                contador_de_heroinas += 1
                acumulador_de_edad_Heroinas = acumulador_de_edad_Heroinas + edad_heroe
                if(habilidad_heroe == "fuerza" or habilidad_heroe == "magia"):
                        contador_de_heroinas_confym += 1    

        
        respuesta=input("¿desea seguir ingresando algun heroe?")
        if(respuesta=="no"):
                break

promedio_edad_heroinas = acumulador_de_edad_Heroinas / contador_de_heroinas
promedio_edad_heroes_de_fuerza = acumulador_de_heroes_fuerza / contador_de_heroes_fuerza

print("el hereo mas joven con fuerza  es :", nombre_heroe_mas_joven_fuerza ,"con"  
,edad_heroe_mas_joven_de_fuerza, " años de  edad")
print("el heroe mas grande es " , nombre_mayor_heroe,  "con",
edad_mayor_heroe, " años de edad ")
print("la cantidad de heroinas que tienen magia o fuerza son : " , contador_de_heroinas_confym)
print("el promedio de edad de heroinas es : " , promedio_edad_heroinas ) 
print("el promedio de edad de heroes de  fuerza es : " , promedio_edad_heroes_de_fuerza)
