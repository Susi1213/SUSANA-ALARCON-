# Escritura de un archivo de texto
# Crea un nuevo archivo llamado my_notes.txt y escribe algunas notas personales

# Abre el archivo en modo escritura ('w')
with open ( 'my_notes.txt' , 'w' ) as archivo:
    # Escribe al menos tres líneas de notas personales en el archivo
    archivo.write ( "Mis notas personales:\n" )
    archivo.write ( "- Hoy es un día nublado.\n" )
    archivo.write ( "- Tengo que hacer el almuerzo.\n" )
    archivo.write ( "- Reunión a las 13:00 PM.\n" )

# Lectura de un archivo de texto
# Abre el archivo en modo lectura ('r')
with open ( 'my_notes.txt' , 'r' ) as archivo:
    # Lee el contenido del archivo línea por línea
    linea = archivo.readline ()
    while linea:
        # Muestra en la consola cada línea leída
        print ( linea.strip () )  # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        linea = archivo.readline ()

# El archivo se cerrará automáticamente cuando salgamos del bloque 'with'
