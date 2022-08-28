'''
Ejercicio Integrador 02

La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, 
tenes 25% de descuento sobre el precio bruto.
El importe total a pagar, BRUTO sin descuento.
El importe total a pagar con descuento (Solo si corresponde).
*Informar el tipo de alimento más caro.
*El promedio de precio por kilo en total. 


'''
acumulador_de_peso=0
acumulador_de_precio = 0 
precio_alimento_mas_caro =''
alimento_mas_caro=''
bandera_alimento_mas_caro = True
contador_productos=0

while True:

    
    tipo_alimento = input("ingrese su alimento")

    while(True) : 
        peso_producto = int(input("ingrese un peso entre 10 y 100 kilos"))
        if(peso_producto > 9 and peso_producto < 101) :
            break 

    while(True) :
        precio_por_kilo = int(input("ingrese un precio por kilo mayor a 0"))
        if(precio_por_kilo > 0 ) : 
            break

    tipo_variedad = input("ingrese una vieradad 'v' , 'a' , 'm' ;(para vegetal , animal , o mezcla) ")
    while tipo_variedad != 'v' and tipo_variedad != 'a' and tipo_variedad != 'm' :
        tipo_variedad = input("ingrese una vieradad 'v' , 'a' , 'm' ;(para vegetal , animal , o mezcla) ")

    
    
    

    if(bandera_alimento_mas_caro == True):
            precio_alimento_mas_caro = precio_por_kilo
            alimento_mas_caro = tipo_alimento
            bandera_alimento_mas_caro= False
    elif  (precio_alimento_mas_caro < precio_por_kilo ) :
            precio_alimento_mas_caro = precio_por_kilo
            alimento_mas_caro = tipo_alimento

    acumulador_de_peso = acumulador_de_precio + peso_producto
    acumulador_de_precio = acumulador_de_precio + precio_por_kilo 
    contador_productos += 1
    
    respuesta = input("¿desea seguir ingresando un tipo de ingrediente para su compra?")
    if(respuesta=="no"):
        break
    

promedio_precio_por_kilo = acumulador_de_precio / contador_productos

if(acumulador_de_peso >300):
            precio_descuento= acumulador_de_precio / 100 * 25
            precio_total = acumulador_de_precio - precio_descuento
            print("el precio total es " , precio_total)
elif(acumulador_de_peso >100 ):
            precio_descuento= acumulador_de_precio / 100 * 15
            precio_total = acumulador_de_peso - precio_descuento
            print("el precio total es " , precio_total)
else:
            precio_total = acumulador_de_precio
            print("el precio total es " , precio_total)   

print("el promedio de precio por kilo es : ", promedio_precio_por_kilo )
print("el alimento mas caro es ", alimento_mas_caro)
