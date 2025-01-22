#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:12:51 2025

@author: henrybergeson
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_data(years):
    combined_df = pd.DataFrame()
    for i in years:
        url = f"https://www.pro-football-reference.com/years/{i}/rushing.htm"
        print(url)#URL of website to be scraped
        page = requests.get(url) #Save the URL
        
        soup = BeautifulSoup(page.text, 'html') #Save the HTML Data
        
        table =  soup.find('table') # Save the html table into the variable labeled 'table'
        
        
        
        th_titles = soup.find_all('th', scope = 'col') #Find the titles of the column names in the dataset
        
        
        table_th_titles = [title.text.strip() for title in th_titles]
        unique_list = []
        for item in table_th_titles:
            if item not in unique_list:
                unique_list.append(item) # strip /n and clean titles
        print(unique_list)
        unique_list.remove("Rk") #For some reason this must be ran for some data sets and not for others
        
        
        
        
        
        year_df = pd.DataFrame(columns = unique_list) #Create a new dataframe with columns labeled with the correct titles
        
        
        column_data = table.find_all('tr') 
        
        for row in column_data[2:-1]: 
            #Get the individual data from each row. Index based on the position of the element in the df and add into the correct location in the df
            row_data = row.find_all('td')
            
            individual_row_data = [data.text.strip() for data in row_data]
            
            
            length = len(year_df)
            year_df.loc[length] = individual_row_data
        year_df["Year"] = i
        
        # Append the current year's data to the combined dataframe
        combined_df = pd.concat([combined_df, year_df], ignore_index=True)
    
    combined_df.to_csv(r'/Users/henrybergeson/Documents/NFL Player Data/2024 Passing Data.csv') #Copy the dataframe to a csv file

get_data([2024, 2023, 2022, 2021, 2020, 2019])
    
    