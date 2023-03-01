import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import yaml

def analyze() -> None:
    os.chdir('../')

    with open('params.yaml') as config__:
        config_ = yaml.safe_load(config__)
    
    year_group_ = df_.groupby('Prod. year')
    year_group_mean_ = year_group_.mean()
    year_summary_ = year_group_mean_[['Price']]
