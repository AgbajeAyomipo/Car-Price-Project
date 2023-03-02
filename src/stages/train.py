import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from xgboost import XGBRegressor
import os
import yaml
import pandas as pd
import joblib

def train() -> None:
    os.chdir('C:/Users/Ayo Agbaje/Documents/Code/Python/GIGS/PYTHON_docs/py_files/Car-Price-Project')

    with open('params.yaml') as config__:
        config_ = yaml.safe_load(config__)
    
    X_train = pd.read_csv(config_['data']['data_file_5'])
    y_train = pd.read_csv(config_['data']['data_file_7'])

    xgbr = XGBRegressor(
        n_estimators = config_['base']['params']['n_estimators'],
        max_depth = config_['base']['params']['max_depth'],
        learning_rate = config_['base']['params']['learning_rate']
    )

    xgbr.fit(X_train, y_train)

    joblib.name(xgbr, config_['model']['name'])

    print('Model Successfully trained')

if __name__ == "__main__":
    
    train()


