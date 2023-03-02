import pandas as pd
import os
import yaml
from yaml import safe_load

def featurize() -> None:
    os.chdir('C:/Users/Ayo Agbaje/Documents/Code/Python/GIGS/PYTHON_docs/py_files/Car-Price-Project')

    with open('params.yaml') as config__:
        config_ = safe_load(config__)

    df_ = pd.read_csv(config_['data']['data_file_3'])

    category_map_ = {
        'Universal': 0,
        'Jeep': 1,
        'Coupe': 2,
        'Sedan': 3,
        'Pickup': 4,
        'Minivan': 5,
        'Goods wagon': 6,
        'Microbus': 7,
        'Cabriolet': 8,
        'Hatchback': 9,
        'Limousine': 10
        }
    manufacturer_map = {
        'LAMBORGHINI': 0,
        'MERCEDES-BENZ': 1,
        'PORSCHE': 2,
        'LAND ROVER': 3,
        'BMW': 4,
        'LEXUS': 5,
        'BENTLEY': 6,
        'TOYOTA': 7,
        'JAGUAR': 8,
        'JEEP': 9,
        'FORD': 10,
        'HYUNDAI': 11,
        'HONDA': 12,
        'MITSUBISHI': 13,
        'AUDI': 14,
        'CHEVROLET': 15,
        'OPEL': 16,
        'FERRARI': 17,
        'KIA': 18,
        'PEUGEOT': 19,
        'SUZUKI': 20,
        'VOLKSWAGEN': 21,
        'MAZDA': 22,
        'HUMMER': 23,
        'SSANGYONG': 24,
        'ASTON MARTIN': 25,
        'TESLA': 26,
        'GAZ': 27,
        'MINI': 28,
        'CADILLAC': 29,
        'NISSAN': 30,
        'SKODA': 31,
        'ACURA': 32,
        'SUBARU': 33,
        'INFINITI': 34,
        'LINCOLN': 35,
        'RENAULT': 36,
        'MASERATI': 37,
        'GMC': 38,
        'BUICK': 39,
        'DODGE': 40,
        'CHRYSLER': 41,
        'FIAT': 42,
        'VOLVO': 43,
        'სხვა': 44,
        'SCION': 45,
        'CITROEN': 46,
        'MERCURY': 47,
        'ALFA ROMEO': 48,
        'VAZ': 49,
        'MOSKVICH': 50,
        'HAVAL': 51,
        'ISUZU': 52,
        'SATURN': 53,
        'DAEWOO': 54,
        'LANCIA': 55,
        'DAIHATSU': 56,
        'GREATWALL': 57,
        'UAZ': 58,
        'SAAB': 59,
        'PONTIAC': 60,
        'SEAT': 61,
        'ZAZ': 62,
        'ROVER': 63,
        'ROLLS-ROYCE': 64
        }
    leather_map_ = {
        'Yes': 0,
        'No': 1
        }
    wheel_position_map = {
        'Left wheel': 0,
        'Right-hand drive': 1
        }
    engine_volume_map = {
        '> 3 & <= 5 No turbo': 0,
        '> 5 and <= 10 turbo': 1,
        '<= 3 turbo': 2,
        '> 3 & <= 5 turbo': 3,
        '> 5 & <= 10 No turbo': 4,
        '<= 3 No turbo': 5,
        '> 10 No turbo': 6
        }
    fuel_type_map_ = {
        'Petrol': 0,
        'Diesel': 1,
        'Hybrid': 2,
        'Plug-in Hybrid': 3,
        'LPG': 4,
        'CNG': 5,
        'Hydrogen': 6
        }
    drive_wheel_map_ = {
        '4x4': 0,
        'Rear': 1,
        'Front': 2
        }
    color_map_ = {
        'Black': 0,
        'White': 1,
        'Silver': 2,
        'Grey': 3,
        'Blue': 4,
        'Orange': 5,
        'Brown': 6,
        'Carnelian red': 7,
        'Red': 8,
        'Green': 9,
        'Yellow': 10,
        'Beige': 11,
        'Golden': 12,
        'Pink': 13,
        'Sky blue': 14,
        'Purple': 15
        }
    mileage_map_ = {
        'Between 10km': 0,
        '10km to 30km': 1,
        '30km to 100km': 2,
        '100km and above': 3
        }
    gear_map_ = {
        'Tiptronic': 0,
        'Automatic': 1,
        'Manual': 2,
        'Variator': 3
        }
    doors_map_ = {
        '04-May': 0,
        '02-Mar': 1,
        '>5': 2
        }
    
    df_['Manufacturer'] = df_['Manufacturer'].map(manufacturer_map)
    df_['Category'] = df_['Category'].map(category_map_)
    df_['Leather interior'] = df_['Leather interior'].map(leather_map_)
    df_['Fuel type'] = df_['Fuel type'].map(fuel_type_map_)
    df_['Engine volume'] = df_['Engine volume'].map(engine_volume_map)
    df_['Mileage'] = df_['Mileage'].map(mileage_map_)
    df_['Gear box type'] = df_['Gear box type'].map(gear_map_)
    df_['Drive wheels'] = df_['Drive wheels'].map(drive_wheel_map_)
    df_['Doors'] = df_['Doors'].map(doors_map_)
    df_['Wheel'] = df_['Wheel'].map(wheel_position_map)
    df_['Color'] = df_['Color'].map(color_map_)

    model_df_ = pd.get_dummies(df_['Model'], drop_first = True)
    df__ = pd.concat([df_, model_df_], axis = 1)
    df_ = df_.drop(['ID', 'Model'], axis = 1)

    df_.to_csv(config_['data']['data_file_4'])

    print('Data Successfully Featurized and Saved')

if __name__ == "__main__":
    featurize()