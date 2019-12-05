#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_core.ipynb (unless otherwise specified).

__all__ = ['combine_files', 'city_with_largets_population_from_df', 'total_population_per_country_from_df']

#Cell
import pandas as pd
import pandavro as pdx
from pathlib import Path

#Cell
def combine_files(json_filepath, arvo_filepath, csv_filepath, output_filepath):
    """Combines the three files, eliminates duplicates and it sorts the resulting dataset by City Name. Creates
    a csv file in output_filepath and returns a dataframe with its content
    """
    #reading all the three files
    df = pd.read_json(json_filepath)
    df = df.append(pd.read_csv(csv_filepath))
    df = df.append(pdx.read_avro(arvo_filepath))
    #dropping duplicates
    df = df.drop_duplicates()
    #sorting by Name
    df = df.sort_values(by='Name')
    #writing to csv
    df.to_csv(output_filepath)
    return pd.read_csv(output_filepath)

#Cell
def city_with_largets_population_from_df(df):
    return df.sort_values(by='Population',ascending=False)[:1][['Name']].iloc[0]['Name']

#Cell
def total_population_per_country_from_df(df, country_code):
    return df.loc[df['CountryCode']==country_code].groupby('CountryCode').Population.sum().iloc[0]