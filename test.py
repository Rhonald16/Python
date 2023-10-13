import csv
import re

# Abre el archivo CSV original en modo lectura y el nuevo archivo en modo escritura
with open('lan.csv', 'r') as archivo_entrada, open('datos_modificados_lan.csv', 'w', newline='') as archivo_salida:
    lector_csv = csv.reader(archivo_entrada)
    escritor_csv = csv.writer(archivo_salida)

    # Define tu expresión regular
    expresion_regular = r'([A-Z0-9]+-GP-\d+)'

    # Nombres para las nuevas columnas
    #nombres_columnas = ["address", "prefix"]
    #nombre_columna_nueva = "Agregar"

    for fila in lector_csv:

        if '/' in fila[2]:
            # Divide la columna "Address + prefix" en dos partes en función del separador "/"
            partes = fila[2].split('/')

            # Reemplaza la columna original con la primera parte y agrega la segunda parte como una nueva columna
            fila[2] = partes[0]
            fila.append(partes[1])

        


        # Agrega los nombres de las nuevas columnas
        #fila.extend(nombres_columnas)

        # Agrega una nueva columna con el valor 1 y un nombre
        #fila.append('1')


        coincidencias = re.findall(expresion_regular, fila[3])

        if coincidencias:
        #     # Combina las coincidencias sin guiones y sin espacios
            nueva_cadena = ''.join(coincidencias).replace("-", "")
            fila[3] = fila[3].replace(coincidencias[0], nueva_cadena)

        # Escribe la fila modificada en el archivo de salida
        escritor_csv.writerow(fila)
