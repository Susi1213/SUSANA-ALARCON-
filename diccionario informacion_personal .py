# Crear un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Camen Suares" ,
    "edad": 35 ,
    "ciudad": "Cuenca" ,
    "numero de telefono": "096841235" ,
    "profesion": "psicóloga"
}

# Acceder a los valores de las claves
nombre = informacion_personal [ "nombre" ]
edad = informacion_personal [ "edad" ]
ciudad = informacion_personal [ "ciudad" ]
telefono = informacion_personal [ "numero de telefono" ]
profesion = informacion_personal [ "profesion" ]

# Imprimir la información personal
print ( "Nombre:" , nombre )
print ( "Edad:" , edad )
print ( "Ciudad:" , ciudad )
print ( "Número de Teléfono:" , telefono )
print ( "Profesión:" , profesion )

# Verificar si la clave "correo electronico" existe y agregarla si no existe
if "correo electronico" not in informacion_personal:
    informacion_personal [ "correo electronico" ] = "ana@example.com"

# Eliminar la clave "edad" del diccionario
del informacion_personal [ "edad" ]

# Imprimir el diccionario final
print ( "\nDiccionario Final:" )
print ( informacion_personal )
