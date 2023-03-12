from cProfile import label
from statistics import correlation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

excel = 'C:\\Users\\rhespinoza\\Downloads\\Human_Resources.csv'

emple_read = pd.read_csv(excel)


emple_read['Attrition'] = emple_read['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

emple_read['OverTime'] = emple_read['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

emple_read['Over18'] = emple_read['Over18'].apply(lambda x: 1 if x =='Y' else 0)



Age = emple_read[['Age','Attrition','OverTime','Over18']]

print(Age)

Age = emple_read[['Age','Over18']]
print(emple_read)

promedio_edad = emple_read['Age'].mean()
print(promedio_edad)

desc = emple_read.describe()
print(desc)

informacion = emple_read.info()
print(informacion)



#cambiar columna attrition 1 == Yes || 0 == No
emple_read['Attrition'] = emple_read['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

#cambiar columna Over18 1 == Yes || 0 == No

emple_read['OverTime'] = emple_read['OverTime'].apply(lambda y: 1 if y == 'Yes' else 0)

#cambiar columna Overtime 1 == Yes || 0 == No

emple_read['Over18'] = emple_read['Over18'].apply(lambda z: 1 if z =='Y' else 0)


#Verificar si faltan Datos 
sns.heatmap(emple_read.isnull(), yticklabels=False, cbar=False, cmap="Blues")

emple_read.hist(bins=30, figsize=(20,20), color= 'r')



left = emple_read[emple_read['Attrition'] == 1]

stayed = emple_read[emple_read['Attrition'] == 0]

total = len(emple_read)
total_left = len(left)
total_stayed = len(stayed)

por_left = 1.*(total_left/total)*100.
print(por_left)

por_stayed = 1.*(total_stayed/total)*100.
print(por_stayed)

desc_left = left.describe()
print(desc_left)

desc_stayed = stayed.describe()
print(desc_stayed)

#mapa calor 
correlations = emple_read.corr()
f, ax = plt.subplots(figsize = (20,20))
sns.heatmap(correlations, annot=True)
plt.show()

#ancho * largo
plt.figure(figsize=[25,12])
sns.countplot(x = 'Age', hue= 'Attrition', data= emple_read)
plt.show()

#Grafico

plt.figure(figsize=[30,20])
plt.subplot(411)
sns.countplot(x = 'JobRole', hue= 'Attrition', data= emple_read)
plt.subplot(412)
sns.countplot(x = 'MaritalStatus', hue= 'Attrition', data= emple_read)
plt.show()

plt.figure(figsize=[12,7])
sns.kdeplot(left['DistanceFromHome'], label ="Empleados que se marchan", shade = True, color = 'r')
sns.kdeplot(stayed['DistanceFromHome'], label ="Empleados que se quedan", shade = True, color = 'b')
plt.show()


plt.figure(figsize=[12,7])
sns.kdeplot(left['TotalWorkingYears'], label ="Empleados que se marchan", shade = True, color = 'r')
sns.kdeplot(stayed['TotalWorkingYears'], label ="Empleados que se quedan", shade = True, color = 'b')
plt.show()

#sueldo por genero
plt.figure(figsize=[15,10])
sns.boxplot(x = 'MonthlyIncome', y = 'Gender', data= emple_read)
plt.show()

#sueldo por rol de trabajo
plt.figure(figsize=[15,10])
sns.boxplot(x = 'MonthlyIncome', y = 'JobRole', data= emple_read)
plt.show()

