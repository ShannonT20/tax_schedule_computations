import pandas as pd
import numpy as np

def calculate_tax_paid_quartely(
        data:pd.DataFrame,
        opening_balance:str,
        tax_paid:str,
        tax_charged:str,
        closing_balance:str,
        months:str
        
) -> pd.DataFrame :
    data = data[:-3].T
    list_month = data.index[data.index.str.contains(months,regex=True)]
    for index,quarter in enumerate(list_month):
        data.loc[quarter,tax_paid] = np.where(
            index == 0,
            - data.loc[:list_month[index],tax_charged].sum(),
            data.loc[:list_month[index-1],tax_charged].sum() - data.loc[:list_month[index],tax_charged].sum()
        )

    data = data.fillna(0)
    data.reset_index(names='',
        inplace=True
    )
    for i in  range(0,len(data)-1):
        data.loc[i,closing_balance] = data.loc[i,opening_balance:tax_paid].sum()
        data.loc[i+1,opening_balance] = data.loc[i,closing_balance]
    data.set_index(
        '',
        inplace=True)
    data.index.name = ''

    data = data.applymap(lambda x: '{:,.2f}'.format(x)).Tsou
    return data