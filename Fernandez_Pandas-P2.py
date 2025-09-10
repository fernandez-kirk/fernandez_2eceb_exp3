# coding: utf-8
PROBLEM 1:
import pandas as pd
cars = pd.read_csv('cars.csv')
cars
cars = pd.read_csv('cars.csv')
cars
cars.head()
cars.tail()
print(cars.iloc[:5, ::2]) 
print{"\nb. row with model = 'Mazda RX4': ")
print(cars.loc[cars['Model'] == 'Mazda RX4'])
print("\nb. row with model = 'Mazda RX4': ")
print pandas as pd
import pandas as pd
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].is in (models), ['Model', 'cyl', 'gear']])
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].is in (models), ['Model', 'cyl', 'gear']])
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].is in (selected_models), ['Model', 'cyl', 'gear']])
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin (selected_models), ['Model', 'cyl', 'gear']])
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin (models), ['Model', 'cyl', 'gear']])
get_ipython().run_cell_magic('writefile', 'Fernandez_Pandas-P2.py', '')
