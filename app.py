import csv
import re

# Abre el archivo CSV original en modo lectura y el nuevo archivo en modo escritura
with open('lan.csv', 'r') as archivo_entrada, open('datos_modificados.csv', 'w', newline='') as archivo_salida:
    lector_csv = csv.reader(archivo_entrada)
    escritor_csv = csv.writer(archivo_salida)

    # Define tu expresión regular
    expresion_regular = r'.+-([A-Z0-9]+\-GP\-\d+)-.+'


    for fila in lector_csv:

        coincidencias = re.findall(expresion_regular, fila[3])
        # print(coincidencias,type(coincidencias))

        if coincidencias:

            limpiar = ''.join(coincidencias).replace('-','')

            fila[3] = fila[3].replace(coincidencias[0], limpiar)
            
            print(fila[3])

        # Escribe la fila modificada en el archivo de salida
        escritor_csv.writerow(fila)
        


