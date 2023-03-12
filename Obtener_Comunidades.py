from platform import architecture
import re
import json

#
ips = []
comunidades = []

#parseo

patron_ip_ipv4 = r"^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
patron_ip_ipv6 = r"^\s*([A-F0-9:]+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
patron_communidades = r"^\s+Community: (.*)"
patron_communidad = r"7303:5\d+"
tipo_ip = '4' 
ruta_1 = 'C:\\Users\\rhespinoza\\OneDrive - Logicalis\\Proyectos\\Reporte\\BEL1RR_Ipv4_ORIGINAL.txt'

with open(ruta_1) as archivo:
    for i, line in enumerate(archivo.readlines()):
        ip = re.search(patron_ip_ipv4 if tipo_ip == '4' else patron_ip_ipv6 , line)
        comunidad_cruda = re.search(patron_communidades, line)

        if ip:
            ips.append(ip.group().strip().replace('.', '-') )
            #ips.append(ip.group().strip())
        
        if comunidad_cruda:
            comunidad = re.findall(patron_communidad, comunidad_cruda.group() ) or ["No_tiene"]
            comunidades.append(comunidad)
        
        #Codigo para detectar bloques de ips sin line de comunidades
        if  len(ips) > len(comunidades) + 1:
            print(line, "\n", ips[-1], "\n", comunidades[-1], f"\n       {i}")
            #print(f"{i}")
            break
    


resultado_final = tuple(zip(ips, comunidades))


with open(f'C:\\Users\\rhespinoza\\OneDrive - Logicalis\\Proyectos\\Reporte\\Data\\filtro_comunidades_ipv{tipo_ip}.csv', 'w') as archivo:
    for i in range(len(resultado_final)):
        archivo.write(  str(resultado_final[i][0]  )  + ',' + str(resultado_final[i][1]  )  + '\n')



#print(ips)
# print()
#print(comunidades)

print(len(ips))
print(len(comunidades))
