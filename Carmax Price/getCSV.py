
"""
drop '-' in FuelType and 'Not Priced' in Price
and return column ['Mileage', 'Price_str', 'FuelType', 'Year', 'usedYear', 'Price_int']
"""
import pandas as pd

def get_fuelType_tuple():
    return {
        "Electric" : ['Electric Fuel System','Electric','Plug-In Electric/Gas'],
        "Hybrid" : ['Flexible Fuel','Hybrid','Gasoline/Mild Electric Hybrid'],
        "Gasoline" : ['Gasoline Fuel', 'Gasoline'],
        "Diesel" : ['Diesel Fuel','Diesel']
    }

def cleanFuelType(fuelType : str):
    if fuelType in ['Electric Fuel System','Electric','Plug-In Electric/Gas']:
        return "Electric"
    elif fuelType in ['Flexible Fuel','Hybrid','Gasoline/Mild Electric Hybrid']:
        return "Hybrid"
    elif fuelType in ['Gasoline Fuel', 'Gasoline']:
        return "Gasoline"
    else:
        return "Diesel"


    
def get_car_csv():
    carData = pd.read_csv('datasets/cars_raw.csv')
    feature = ['Mileage','Price','FuelType','Year']
    carData = carData[feature]
    carData['usedYear'] = 2023 - carData['Year']
    carData.columns = ['Mileage', 'Price_str', 'FuelType', 'Year', 'usedYear']

    indexNoFuelType = carData[carData['FuelType'].str.contains('-')].index
    carData.drop(indexNoFuelType,inplace = True)

    indexNoPrice = carData[carData['Price_str'].str.contains('Not Priced')].index
    carData.drop(indexNoPrice,inplace = True)
    
    carData['Price_int'] = carData.Price_str.str.replace('$','').str.replace(',','').astype('int')

    carData['FuelType'] = carData["FuelType"].map(cleanFuelType)


    return carData


