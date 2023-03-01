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

    df_ = pd.read_csv(config_['data']['data_file_2'])

    year_group_ = df_.groupby('Prod. year')
    year_group_mean_ = year_group_.mean()
    year_summary_ = year_group_mean_[['Price']]

    manufacturer_group_ = df_.groupby('Manufacturer')
    manufacturer_group_mean_ = manufacturer_group_.mean()
    manufacturer_summary_ = manufacturer_group_mean_[['Price']]

    def bar_plot_(df__, title_, save_name):
        if len(df__) <= 5:
            fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (15, 6))
            df__['Price'].plot.line(color = 'black', ax = ax, linewidth = 1.2)
            df__['Price'].plot.bar(ax = ax, color = 'grey')
            ax.tick_params(axis = 'x', rotation = 0)
            # ax.grid(axis = 'x')
            ax.bar_label(ax.containers[0])
            plt.title(title_, fontsize = 25)
            plt.ylabel('PRICE', fontsize = 25)
            plt.savefig(save_name)

        elif len(df__) > 5:
            fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (18, 6))
            df__['Price'].plot.line(color = 'black', ax = ax, linewidth = 1.2)
            df__['Price'].plot.bar(ax = ax, color = 'grey')
            ax.tick_params(axis = 'x', rotation = 90)
            # ax.grid(axis = 'x')
            # ax.bar_label(ax.containers[0])
            plt.title(title_, fontsize = 25)
            plt.ylabel('PRICE', fontsize = 25)
            plt.savefig(save_name)
    
    bar_plot_(df__ = year_summary_, title_ = 'Average Car Sales by Prod Year', save_name = config_['plot']['plot_1'])
    bar_plot_(df__ = manufacturer_summary_, title_ = 'Average Car Sales by Manufacturer', save_name = config_['plot']['plot_2'])

    def int_conv(col_):
        if col_ == '-':
            return np.nan
        else:
            return int(col_)

    df_['Levy'] = df_['Levy'].apply(int_conv)
    df_['Levy'] = df_['Levy'].fillna(value = df_['Levy'].mean())

    corr_df = pd.DataFrame(data = df_.corrwith(df_['Price']), columns = ['Correlation with Price'])
    corr_df = corr_df.sort_values(by = corr_df.columns[0] ,ascending=False)

    plt.figure(figsize = (5, 8))
    sns.heatmap(corr_df, cmap = 'summer', annot = True, center = True, annot_kws = {'color': 'black'}, linewidth = .3)
    plt.savefig(config_['plot']['plot_3'])

    def mileage_(col_):
        return int(col_.split(' ')[0])

    df_['Mileage'] = df_['Mileage'].apply(mileage_)

    def mileage_map_mini_(col_):
        if (col_ >= 0) & (col_ <= 10000):
            return 'Between 10km'
        elif (col_ > 10000) & (col_ <= 30000):
            return '10km to 30km'
        elif (col_ > 30000) & (col_ <= 100000):
            return '30km to 100km'
        elif (col_ > 100000):
            return '100km and above'

    df_['Mileage'] = df_['Mileage'].map(mileage_map_mini_)

    mileage_group_ = df_.groupby('Mileage')
    mileage_group_mean_ = mileage_group_.mean()
    mileage_summary_ = mileage_group_mean_[['Price']]

    bar_plot_(df__ = mileage_summary_, title_ = 'Average Car Sales by Mileage', save_name = config_['plot']['plot_4'])
    # 
    fig, ax = plt.subplots(1, 2, figsize = (15, 7))
    gear_df_ = pd.DataFrame(
        data = df_['Gear box type'].value_counts()
    )
    gear_df_.columns = ['Count']
    gear_df_

    sns.countplot(x = 'Gear box type', data = df_, ax = ax[0], color = 'black')
    ax[0].bar_label(ax[0].containers[0], color = 'black')
    ax[0].set_title('       CountPlot and Pie Plot showing Distribution of Cars based on their Gear Type', loc = 'left')
    # ax

    gear_df_['Count'].plot.pie(ylabel = '', autopct = '%.1f', cmap = 'gist_gray', subplots = True, ax = ax[1], textprops = {'color': 'blue'})
    fig.savefig(config_['plot']['plot_5'])
    # 

    gear_group_ = df_.groupby('Gear box type')
    gear_group_mean_ = gear_group_.mean()
    gear_summary_ = gear_group_mean_[['Price']]

    bar_plot_(df__ = gear_summary_, title_ = 'Average Car Sales by Gear Box Type', save_name = config_['plot']['plot_6'])

    plt.figure(figsize = (10,6))
    sns.boxplot(x = 'Color', y = 'Price', data = df_)
    plt.tick_params(axis='x', rotation = int('90'))
    plt.yticks(np.arange(0e7, 2.6e7, 5000000),
            ['0', '5M', '1B', '1.5B', '2B', '2.5B'])
    plt.title('Plot Showing Presence of Outliers in the Price Column, by Color of the Car')
    plt.savefig(config_['plot']['plot_7'])

    df_ = df_.sort_values(by = df_.columns[-1], ascending= False)
    df_ = df_.reset_index()
    df_ = df_.drop(0, axis = 0)

    not_categorical_ = df_._get_numeric_data().columns
    categorical_ = set(df_.columns).difference(not_categorical_)

    def engine_size(col_):
        if ('Turbo' in col_) & (float(col_.split(' ')[0]) <= 3):
            turbo_ = '<= 3' + ' turbo'
            return turbo_
        elif ('Turbo' in col_) & (float(col_.split(' ')[0]) > 3) & (float(col_.split(' ')[0]) <= 5):
            turbo_ = '> 3 & <= 5' + ' turbo'
            return turbo_
        elif ('Turbo' in col_) & (float(col_.split(' ')[0]) > 5) & (float(col_.split(' ')[0]) <= 10):
            turbo_ = '> 5 and <= 10' + ' turbo'
            return turbo_
        elif ('Turbo' in col_) & (float(col_.split(' ')[0]) > 10):
            turbo_ = '> 10' + ' turbo'
            return turbo_
        elif 'Turbo' not in col_ and (float(col_) <= 3):
            turbo_ = '<= 3' + ' No turbo'
            return turbo_
        elif 'Turbo' not in col_ and (float(col_) > 3) and (float(col_) <= 5):
            turbo_ = '> 3 & <= 5' + ' No turbo'
            return turbo_
        elif 'Turbo' not in col_ and (float(col_) > 5) and (float(col_) <= 10):
            turbo_ = '> 5 & <= 10' + ' No turbo'
            return turbo_
        elif 'Turbo' not in col_ and (float(col_) > 10):
            turbo_ = '> 10' + ' No turbo'
            return turbo_
    
    df_['Engine volume'] = df_['Engine volume'].apply(engine_size)

    df_.to_csv(config_['data']['data_file_3'])

if __name__ == "__main__":
    analyze()