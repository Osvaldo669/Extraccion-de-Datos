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
