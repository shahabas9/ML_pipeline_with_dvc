import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import yaml




def load_data(data_url:str)-> pd.DataFrame:
    try:
        df= pd.read_csv(data_url)
        return df
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the csv file from {data_url}.")
        print(e)
        raise
    except Exception as e:
        print("Error : an unexpected error occured while loading the data.")
        print(e)
        raise

def preprocess_data(df:pd.DataFrame)->pd.DataFrame:
    try:
        df.drop(columns=['tweet_id'],inplace=True)
        final_df = df[df['sentiment'].isin(['happiness','sadness'])]
        final_df['sentiment'].replace({'happiness':1, 'sadness':0},inplace=True)
        return final_df
    except KeyError as k:
        print(f"Error : Missing column {k} in the dataframe")
        print(k)
        raise
    except Exception as e:
        print(f"Error : An error occured while during the preprocessing")
        print(e)
        raise

def save_data(train_data:pd.DataFrame,test_data:pd.DataFrame,data_path:str)->None:
    try:
        data_path=os.path.join(data_path,"raw")
        os.makedirs(data_path,exist_ok=True)
        train_data.to_csv(os.path.join(data_path,"train.csv"),index=False)
        test_data.to_csv(os.path.join(data_path,"test.csv"),index=False)
    except Exception as e:
        print(f"Error : An error occured while saving the data.")
        print(e)
        raise

def main():
    try:
        df=load_data('https://raw.githubusercontent.com/entbappy/Branching-tutorial/refs/heads/master/tweet_emotions.csv')
        final_df=preprocess_data(df)
        train_data,test_data=train_test_split(final_df,test_size=0.2,random_state=36)
        save_data(train_data,test_data,"data")

    except Exception as e:
        print(f"Error : Failed to complete data ingestion process")
        print(f"Error : {e}")
        

if __name__ =="__main__":
    main()
