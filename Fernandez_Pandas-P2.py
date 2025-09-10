# coding: utf-8
import pandas as pd

print(cars.iloc[:5, ::2]) 
print{"\nb. row with model = 'Mazda RX4': ")
print(cars.loc[cars['Model'] == 'Mazda RX4'])
print("\nb. row with model = 'Mazda RX4': ")

print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].is in (models), ['Model', 'cyl', 'gear']])

models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin (models), ['Model', 'cyl', 'gear']])
get_ipython().run_cell_magic('writefile', 'Fernandez_Pandas-P2.py', '')
