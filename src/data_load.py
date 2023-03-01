import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import os
import yaml

def data_load() -> None:
    os.chdir('../')

    with open('params.yaml') as config__:
        config_ = yaml.safe_load(config__)
    reset_cols_ = ['ID', 'Levy', 'Manufacturer', 'Model', 'Prod. year',
               'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
               'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color',
               'Airbags', 'Price']
    df_ = df_[reset_cols_]
    df_.to_csv(config_['data']['data_file_2'])

    print('Data Loaded Successfully')

if __name__ == "__main__":
    data_load()