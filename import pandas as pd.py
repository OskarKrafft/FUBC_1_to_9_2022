import pandas as pd

## load data
df = pd.read_csv('./results/FUBC_1_to_9_data.csv')

print(df.head())

## print all column names
print(df.columns)

## show all possible values FUBC_report_number can take 
print(df['FUBC_report_number'].unique())


## filter for the FUBC_report_number == 9
wave_9 = df[df['FUBC_report_number'] == 9]
wave_9.describe()

## show list of countries in wave 9
print(wave_9['Country'].unique())
print(wave_9['Country'].nunique())
print(wave_9["Crop"].unique())
print(wave_9["Crop"].nunique())

# 64 countries are represented in wave 9

## show descriptives for Nan values in wave 9
print(wave_9.isna().sum())

## is there any metadata for the Nan variables?
print(wave_9['K20_pc_fert'].describe())