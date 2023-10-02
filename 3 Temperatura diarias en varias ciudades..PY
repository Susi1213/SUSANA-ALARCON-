# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes" , "temp": 68} ,
            {"day": "Martes" , "temp": 81} ,
            {"day": "Miércoles" , "temp": 72} ,
            {"day": "Jueves" , "temp": 70} ,
            {"day": "Viernes" , "temp": 83} ,
            {"day": "Sábado" , "temp": 86} ,
            {"day": "Domingo" , "temp": 52}
        ] ,
        [  # Semana 2
            {"day": "Lunes" , "temp": 56} ,
            {"day": "Martes" , "temp": 79} ,
            {"day": "Miércoles" , "temp": 93} ,
            {"day": "Jueves" , "temp": 80} ,
            {"day": "Viernes" , "temp": 82} ,
            {"day": "Sábado" , "temp": 84} ,
            {"day": "Domingo" , "temp": 53}
        ] ,
        [  # Semana 3
            {"day": "Lunes" , "temp": 67} ,
            {"day": "Martes" , "temp": 81} ,
            {"day": "Miércoles" , "temp": 75} ,
            {"day": "Jueves" , "temp": 72} ,
            {"day": "Viernes" , "temp": 84} ,
            {"day": "Sábado" , "temp": 90} ,
            {"day": "Domingo" , "temp": 85}
        ] ,
        [  # Semana 4
            {"day": "Lunes" , "temp": 75} ,
            {"day": "Martes" , "temp": 78} ,
            {"day": "Miércoles" , "temp": 80} ,
            {"day": "Jueves" , "temp": 79} ,
            {"day": "Viernes" , "temp": 84} ,
            {"day": "Sábado" , "temp": 87} ,
            {"day": "Domingo" , "temp": 91}
        ]
    ] ,
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes" , "temp": 62} ,
            {"day": "Martes" , "temp": 64} ,
            {"day": "Miércoles" , "temp": 68} ,
            {"day": "Jueves" , "temp": 70} ,
            {"day": "Viernes" , "temp": 73} ,
            {"day": "Sábado" , "temp": 75} ,
            {"day": "Domingo" , "temp": 79}
        ] ,
        [  # Semana 2
            {"day": "Lunes" , "temp": 63} ,
            {"day": "Martes" , "temp": 66} ,
            {"day": "Miércoles" , "temp": 70} ,
            {"day": "Jueves" , "temp": 72} ,
            {"day": "Viernes" , "temp": 75} ,
            {"day": "Sábado" , "temp": 77} ,
            {"day": "Domingo" , "temp": 81}
        ] ,
        [  # Semana 3
            {"day": "Lunes" , "temp": 61} ,
            {"day": "Martes" , "temp": 65} ,
            {"day": "Miércoles" , "temp": 68} ,
            {"day": "Jueves" , "temp": 70} ,
            {"day": "Viernes" , "temp": 72} ,
            {"day": "Sábado" , "temp": 76} ,
            {"day": "Domingo" , "temp": 80}
        ] ,
        [  # Semana 4
            {"day": "Lunes" , "temp": 54} ,
            {"day": "Martes" , "temp": 77} ,
            {"day": "Miércoles" , "temp": 89} ,
            {"day": "Jueves" , "temp": 51} ,
            {"day": "Viernes" , "temp": 64} ,
            {"day": "Sábado" , "temp": 77} ,
            {"day": "Domingo" , "temp": 84}

        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia [ 'temp' ]
        print ( suma )
