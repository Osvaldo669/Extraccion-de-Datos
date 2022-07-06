import pandas as pds
import numpy as np		   
import os

datos = pds.read_csv(r"Document\\covid_19_data.csv")


print (datos)


print(datos.head())
print("************************************************************************************")
print(datos.tail())
print("************************************************************************************")
print(datos)
print("************************************************************************************")
print(datos.info())
print("************************************************************************************")
print(datos.describe())


import pandas as pds
import numpy as np
import os

datos = pds.read_csv(r"Document\\covid_19_data.csv")
pais = datos.groupby('Country/Region')[['Confirmed','Deaths']].sum()
resultado = pais.nlargest(10, 'Confirmed')
print(resultado)
resultado.plot(kind='bar')