#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:12:51 2025

@author: henrybergeson
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.spotrac.com/nfl/market-value' #URL of website to be scraped
page = requests.get(url) #Save the URL

soup = BeautifulSoup(page.text, 'html') #Save the HTML Data

table =  soup.find('table') # Save the html table into the variable labeled 'table'



th_titles = soup.find_all('th') #Find the titles of the column names in the dataset

table_th_titles = [title.text.strip() for title in th_titles] # strip /n and clean titles


df = pd.DataFrame(columns = table_th_titles) #Create a new dataframe with columns labeled with the correct titles


column_data = table.find_all('tr') #Find the rows in the dataset and save them under the variable column_data

for row in column_data[1:]: #Get the individual data from each row. Index based on the position of the element in the df and add into the correct location in the df
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
    #print(individual_row_data)
    
df.to_csv(r'/Users/henrybergeson/Documents/NFL Player Data/Player Data.csv') #Copy the dataframe to a csv file