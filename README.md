For Problem 1
Pandas has to imported first for it to work so I imported pandas as pd
I downloaded the cars.csv file first and then to load the cars.csv file, pd.read_csv is used to read the downloaded .csv file and put into columns and rows of data
To display the first five rows, I used cars.head as this command prints out the needed in the problem which are the first five rows
To display the last five rows, I used cars.tail which is like the cars.head but this time, its the last five rows that were printed

For Problem 2
Pandas is imported as pd again to start
To display the first five rows with their columns being odd numbers, cars.iloc is used to locate the needed data using integers. :5 means the first five rows and ::2 is an interval to get every odd numbered column 
To get the row wherein Mazda RX4 is in, cars.loc is used to locate te whole row and I simply typed out the name of the model I needed the row of.
To get the cyl of Camaro Z28, the same code used in the previous problem can be applied with an addition of ['cyl] to indicate that the only thing to print is the cyl of the chosen model
To get the cyl and gear of the chosen cars, I first put them into a list called models and then I used cars.loc again with the inclusion of is.in which tells the program to consider the ones inside the list under models. After that, I typed in ['Model', 'cyl', 'gear'] at the end to indicate the ones that needed to be printed for the certain models of cars in the list.
