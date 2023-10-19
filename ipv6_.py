import ipaddress
import csv

def comprimir_direccion_ipv6(ipv6):
    direccion, mascara = ipv6.split('/')
    direccion_comprimida = ipaddress.IPv6Address(direccion).compressed
    return f"{direccion_comprimida}"

try:
    with open('ipv6.csv', 'r') as archivo_entrada, open('datos_modificados.csv', 'w', newline='') as archivo_salida:
        lector_csv = csv.reader(archivo_entrada)
        next(lector_csv)  # Ignora la primera fila (encabezados)

        escritor_csv = csv.writer(archivo_salida)
        escritor_csv.writerow(["IPv6_comprimida","Nombre_OLT"])  # Agrega encabezados al archivo de salida

        for fila in lector_csv:
            if len(fila) >= 3:  # Verifica que la fila tenga al menos 3 elementos
                direccion_ipv6 = fila[2]
                try:
                    direccion_comprimida = comprimir_direccion_ipv6(direccion_ipv6)
                    print(direccion_comprimida)
                    escritor_csv.writerow([direccion_comprimida, fila[3]])  # Escribe en el archivo de salida
                except (ipaddress.AddressValueError, ValueError) as e:
                    print(f"Error al procesar la dirección IPv6 en la fila {fila}: {e}")
            else:
                print(f"La fila {fila} no tiene suficientes elementos para procesar la dirección IPv6")
except FileNotFoundError as e:
    print(f"Error al abrir el archivo: {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")