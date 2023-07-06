''' DataFrame'''

from datapackage import Package
import pandas as pd
from matplotlib import pyplot as plt

def fetch_data():
    
    data_url = 'https://datahub.io/core/s-and-p-500/datapackage.json'

    # to load Data Package into storage
    package = Package(data_url)
    
    
    # create dataframe
    df_base = pd.DataFrame()
    
    # to load only tabular data
    resources = package.resources
    for resource in resources:
        if resource.tabular:
            df_base = pd.concat([df_base, pd.read_csv(resource.descriptor['path'])])
            
    # Change index type 
    df_base['Date'] = pd.to_datetime(df_base['Date'])
    df_base = df_base.set_index('Date')
    
                       
    return df_base


def join():
    
    # define range
    start = '2017-01-01'
    end = '2018-04-01'
    
    # create DataFrame
    dates = pd.date_range(start, end)
    df = pd.DataFrame(index=dates)
    
    # join
    dfSPY = fetch_data()
    df_joined = df.join(dfSPY)
    
    return df_joined
    
def slice_df():
    dfSPY = fetch_data()
    
    df = dfSPY.loc['2017-03-29':'2018-04-01', 'Dividend':'Real Earnings']
    
    return df
def normalize(df):
    return df / df.iloc[0,:]
    
def plot(df):
    df = normalize(df)
    p = df.plot(title="S&P", fontsize=8)
    p.set_xlabel("Date")
    p.set_ylabel("Amount")
    plt.show()

if __name__ == '__main__':
    #print(join())
    print(plot(slice_df()))
