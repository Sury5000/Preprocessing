import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")


# Data Descriptions 

print(df.head(5))

print(df.shape)

print(df.columns.tolist())

print(df.info())

print(df.describe())


# Data Manipulations

print(df[["age","sex"]].head(10))

print(df.loc[df["age"]>60,["class","age"]])  # loc used to select value by label name 

print(df.iloc[1][2]) # iloc used to select value by index value 

adult_women = df.query('age >= 30 and sex == "female"')  # query functions used to filter data

print(adult_women)


print(df.isna().sum())

# Filling Null value by various statistic calculation related to the features

df['age'] = df['age'].fillna(df['age'].median()) # Used Median due to outliers and high range

df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0]) # used mode due to Categorical type and low missing values

df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])


df = df.drop('deck', axis=1) # more than 70% are Nan value and will not help in further analysis so we removed it 

print(df.isna().sum())


print(df.duplicated().sum())  # Number of fully duplicated rows
df = df.drop_duplicates()


print(df.duplicated().sum()) 

