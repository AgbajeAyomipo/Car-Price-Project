import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score
from xgboost import XGBRegressor
import os
import numpy as np
import yaml
import seaborn as sns
import pandas as pd
import json
import joblib
import matplotlib.pyplot as plt

def evaluate() -> None:
    os.chdir('C:/Users/Ayo Agbaje/Documents/Code/Python/GIGS/PYTHON_docs/py_files/Car-Price-Project')

    with open('params.yaml') as config__:
        config_ = yaml.safe_load(config__)
    
    X_test = pd.read_csv(config_['data']['data_file_6'])
    y_test = pd.read_csv(config_['data']['data_file_8'])

    X_test = X_test[X_test.columns].values
    y_test = y_test['Price'].values

    xgbr = joblib.load(config_['model']['name'])

    preds_ = xgbr.predict(X_test)

    evs = explained_variance_score(y_true=y_test, y_pred=preds_)
    mae = mean_absolute_error(y_true=y_test, y_pred=preds_)
    mse = mean_squared_error(y_true=y_test, y_pred=preds_)
    rmse = np.sqrt(mse)

    _metric = {
        'Explained Variance Score': evs,
        'Mean Absolute Error': mae,
        'Mean Squared Error': mse,
        'Root Mean Squared Error': rmse
    }

    json.dump(
        obj = _metric,
        fp = open(config_['metric']['path'] + '/' 'metrics.json', 'w'),
        indent = 4,
        sort_keys=True
    )

    plt.figure(figsize = (6, 10))
    sns.scatterplot(x = y_test, y = preds_)
    plt.plot(preds_, preds_, color = 'red')

    plt.savefig(config_['plot']['plot_8'])

    print('Metrics have now been evaluated and results saved')

if __name__ == "__main__":
    evaluate()