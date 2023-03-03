import pandas as pd
import os
import yaml
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def data_split() -> None:
    os.chdir('C:/Users/Ayo Agbaje/Documents/Code/Python/GIGS/PYTHON_docs/py_files/Car-Price-Project')

    with open('params.yaml') as config__:
        config_ = yaml.safe_load(config__)

    df__ = pd.read_csv(config_['data']['data_file_4'])

    X = df__.drop('Price', axis = 1).values
    y = df__['Price'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = config_['base']['test_size'], random_state = config_['base']['random_state'])
    
    scale_ = MinMaxScaler(feature_range=(0,1))

    scale_.fit(X_train)
    X_train = scale_.transform(X_train)
    X_test = scale_.transform(X_test)

    X_train = pd.DataFrame(data = X_train,
                           columns = df__.columns[:-1])
    X_test = pd.DataFrame(data = X_test,
                           columns = df__.columns[:-1])
    y_train = pd.DataFrame(data = y_train,
                           columns = ['Price'])
    y_test = pd.DataFrame(data = y_test,
                          columns = ['Price'])
    
    X_train.to_csv(config_['data']['data_file_5'], index = 0)
    X_test.to_csv(config_['data']['data_file_6'], index = 0)
    y_train.to_csv(config_['data']['data_file_7'], index = 0)
    y_test.to_csv(config_['data']['data_file_8'], index = 0)

    print("Data Successfully Splitted and Saved")

if __name__ == "__main__":
    data_split()
