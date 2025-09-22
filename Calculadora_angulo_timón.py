def calcular_excentricidad(porcentaje_necesario, radio_de_la_polea):
    excentricidad = (porcentaje_necesario * radio_de_la_polea)/100
    return(f"tienes que alejar el eje de la polea {excentricidad}cm para ganar un {porcentaje_necesario}% de giro")

def calcular_porcentaje(recorrido_original, recorrido_disponible):
    porcentaje = (recorrido_original/recorrido_disponible - 1) * 100
    return(porcentaje)


# cambia la variable excenticidad timón en onshape para obtener el diseño 3D 
# link al proyecto: https://cad.onshape.com/documents/b7df1c6d75dbca150c312733/w/0a975e62208bc7a5049a8817/e/4e7948d3884854bfda58f8e1
print("introduce todas las medidas con las mismas unidades")
recorrido_original = float(input("introduce el recorrido completo que tiene tu timón en el reposa: "))

recorrido_disponible = float(input("introduce el recorrido disponible que tiene tu timón: "))

porcentaje_necesario = calcular_porcentaje(recorrido_original,recorrido_disponible)

radio_de_la_polea = float(input("introduce el radio actual de tu timón: "))

print(calcular_excentricidad(porcentaje_necesario,radio_de_la_polea))