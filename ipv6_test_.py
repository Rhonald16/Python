import ipaddress
import csv

def comprimir_ipv6(ipv6):
    cadena,mascara = ipv6.split('/')
    dir_comprimida = ipaddress.IPv6Address(cadena).compressed
    return dir_comprimida


try:
    with open('ipv6.csv', 'r') as archivo_entrada, open('datos_modificados_ipv6_test.csv', 'w', newline='') as archivo_salida:
        lector_csv = csv.reader(archivo_entrada)
        next(lector_csv)  # Ignora la primera fila (encabezados)

        escritor_csv = csv.writer(archivo_salida)
        escritor_csv.writerow(["IPv6_comprimida","Nombre_OLT", "mascara"])  # Agrega encabezados al archivo de salida

        for fila in lector_csv:
            dir_ipv6 = fila[2]

            if dir_ipv6:

                dir_comprimida = comprimir_ipv6(dir_ipv6)

                #print(dir_comprimida)

                escritor_csv.writerow([dir_comprimida, fila[3]])  # Escribe en el archivo de salida
                


except FileNotFoundError as e:
    print(f"El archivo no se puede abrir: {e}")

except Exception as e:
    print(f"error inesperado: {e}")

    