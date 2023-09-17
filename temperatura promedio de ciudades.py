def temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de múltiples ciudades durante un período de tiempo.

    Args:
        datos (dict): Un diccionario que contiene los datos de temperatura por ciudad y semana.
                      La estructura debe ser: {'ciudad1': [temp1_semana1, temp1_semana2, ...],
                                               'ciudad2': [temp2_semana1, temp2_semana2, ...],
                                               ...}

    Returns:
        dict: Un diccionario con las temperaturas promedio por ciudad.
    """
    temperaturas_promedio = {}

    for ciudad , temperaturas_semana in datos.items ():
        # Calcula la temperatura promedio para cada ciudad
        promedio = sum ( temperaturas_semana ) / len ( temperaturas_semana )
        temperaturas_promedio [ ciudad ] = promedio

    return temperaturas_promedio


# Ejemplo de uso:
datos_temperatura = {
    'Ciudad QUITO': [ 15 , 16 , 15 , 14 ] ,
    'Ciudad GUAYAQUIL': [ 30 , 31 , 29 , 32 ] ,
    'Ciudad CUENCA': [ 20 , 19 , 21 , 18 ]
}

temperaturas_promedio = temperatura_promedio ( datos_temperatura )

for ciudad , promedio in temperaturas_promedio.items ():
    print ( f"La temperatura promedio en {ciudad} es: {promedio}°C" )
