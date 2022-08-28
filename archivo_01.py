'''La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, 
de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.

Se debe informar lo siguiente:
a)Del más caro de los barbijos, la cantidad de unidades y el fabricante.
b)Del ítem con más unidades, el fabricante.
c)Cuántas unidades de jabones hay en total.'''




#tipo_producto = ''
precio = 0 
cantidad = 0 
marca = ''
fabricante = ''

marca_barbijo_caro = ''
cantidad_barbijo_caro = 0 
fabricante_barbijo_caro = ''
precio_barbijo_caro = ''

item_mas_unidades = ''
fabricante_mas_unidades = ''

cantidad_jabones = 0


for iteracion  in range(5):



    tipo_producto = input('ingrese tipo de producto (jabon , barbijo , alcohol) ')
    while tipo_producto != 'barbijo' and tipo_producto !=  'jabon' and tipo_producto !=  'alcohol':
        tipo_producto = input('ingrese tipo de producto (jabon , barbijo , alcohol) ')

    while (True) :
      precio = int(input('ingrese precio : ')) 
      if precio > 99 and precio < 301 : 
        break

    while (True) :
      cantidad = int(input('ingrese cantidad : ')) 
      if cantidad > 0 and cantidad < 1000 : 
        break
    
    marca = input('ingrese marca')


    fabricante = input('ingrese fabrincante ')

    if tipo_producto == 'barbijo':
      
      if precio > precio_barbijo_caro:
        #en caso de que sea mas caro que el anterior
        precio_barbijo_caro = precio 
        cantidad_barbijo_caro = cantidad
        fabricante_barbijo_caro = fabricante
        
    elif tipo_producto == 'jabon':
        cantidad_jabones += cantidad 
    
    if cantidad > item_mas_unidades : 
        item_mas_unidades = cantidad 
        fabricante_mas_unidades = fabricante    

print('barbijo mas caro hay ', cantidad_barbijo_caro ,' y la fabrica ', fabricante_barbijo_caro)
print('el item con mas unidades lo fabrica ' , fabricante_mas_unidades)
print('jabones hay ' , cantidad_jabones)
print('fin del programa')


        




