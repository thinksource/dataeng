import pandas as pd
import os
import json
column_names = ['FirstName', 'LastName', 'Company', 'BirthDate', 'Salary', 'Address', 'City', 'State', 'Post', 'Phone', 'Mobile', 'Email']
string_columns = ['Address', 'City', 'State', 'Post', 'Phone', 'Mobile', 'Email']
date_age = "Mar 1st, 2024"
# Read the CSV file
def read_csv(filename, separator='|'):

    """
    Reads the member-data.csv file and returns a DataFrame containing the data.
    The CSV file is read with '|' as the separator and the column names are specified
    in the column_names list.
    
    Returns:
        pd.DataFrame: Dataframe containing the data from the CSV file
    """

    df = pd.read_csv(filename, sep=separator, names=column_names, dtype={col: str for col in string_columns})
    return df

def transform_data(df):
    """
    Perform the following operations on the input DataFrame:

    1. Convert 'BirthDate' column to datetime type
    2. Create a new 'SalaryBucket' column and assign it 'A', 'B', or 'C' 
       based on ranges of 'Salary' values
    3. Format 'Salary' as currency
    4. Calculate 'Age' from 'BirthDate' and a given date
    5. Format 'BirthDate' as DD/MM/YYYY
    6. Create a 'FullName' column by concatenating 'FirstName' and 'LastName'
    7. Create a full address by concatenating 'Address', 'City', 'State', and 'Post'
    8. Drop 'FirstName' and 'LastName' columns
    """
    df['BirthDate'] = pd.to_datetime(df['BirthDate'], unit='s')
    df['SalaryBucket'] = pd.cut(df['Salary'], 
                            bins=[0, 50000, 100000, float('inf')],
                            labels=['A', 'B', 'C'], 
                            right=False)
    df['Salary'] = df['Salary'].apply(lambda x: '${:,.2f}'.format(x))
    df['Age'] = (pd.to_datetime(date_age) - pd.to_datetime(df['BirthDate'])).dt.days // 365
    df['Age'] = df['Age'].fillna(0).astype(int)
    df['BirthDate']= df['BirthDate'].dt.strftime('%d/%m/%Y')
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']
    df['Address'] = df['Address'] + ', ' + df['City'] + ' ' + df['State'] + ' ' + df['Post'].astype(str)
    # ***it is not differnt for the example file, just make sure Phone and Mobile have 10 digits***
    df['Phone'] = df['Phone'].apply(lambda x: x.zfill(10))
    df['Mobile'] = df['Mobile'].apply(lambda x: x.zfill(10))
    df.drop(columns=['FirstName', 'LastName'], inplace=True)
    return df

def load_data(df):
    os.makedirs('./output', exist_ok=True)

    js=df.to_json(None, orient='records', lines=True)
    with open('./output/data.json', 'w') as file:
         json.dump(js, file, indent=4)

if __name__ == '__main__':
    df = read_csv('member-data.csv')
    transform_data(df)
    load_data(df)
    print(df[[ 'FullName','Age', 'Address', 'Salary', 'SalaryBucket']])