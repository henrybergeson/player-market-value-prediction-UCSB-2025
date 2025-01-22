#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:05:27 2025

@author: henrybergeson
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.nfl.com/stats/player-stats/category/receiving/2024/reg/all/receivingreceptions/desc'

# Starting URL (first page)
#url = base_url + '?aftercursor=AAAASwAAAEtANgAAAAAAADFleUp6WldGeVkyaEJablJsY2lJNld5SXlNaUlzSWpNeU1EQTBZVFExTFRRMk1qWXRPVEk0Tnkxak5EVTBMVFEzT1dJNU5ESmpZbVF5TmlJc0lqSXdNalFpWFgwPQ=='
df = pd.DataFrame
# Loop through pages and scrape data
for page_num in range(1, 100):  # Scraping the first 5 pages as an example
      # Scraping the first 5 pages as an example
    print(f"Scraping page {page_num}...")
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape data from the page (e.g., player stats table)
    # Add your scraping logic here (e.g., extract player stats, store in a dataframe)
   #URL of website to be scraped
    page = requests.get(url) #Save the URL

    soup = BeautifulSoup(page.text, 'lxml') #Save the HTML Data

    table =  soup.find('table') # Save the html table into the variable labeled 'table'
    if table == None:
        break



    th_titles = soup.find_all('th') #Find the titles of the column names in the dataset

    table_th_titles = [title.text.strip() for title in th_titles] # strip /n and clean titles

    if page_num == 1:  # Only create the dataframe for the first page
        df = pd.DataFrame(columns=table_th_titles)
    #df = pd.DataFrame(columns = table_th_titles) #Create a new dataframe with columns labeled with the correct titles

    
    column_data = table.find_all('tr') #Find the rows in the dataset and save them under the variable column_data

    for row in column_data[1:]: #Get the individual data from each row. Index based on the position of the element in the df and add into the correct location in the df
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        length = len(df)
        df.loc[length] = individual_row_data
        #print(individual_row_data)
        
    #print(df)
    
        

    # Look for the next `aftercursor` value for pagination
    next_cursor = None
    next_page = soup.find('div', {'class': 'nfl-o-table-pagination'})
    
    # Check for 'next' page link
    #print(next_page)
    #print(next_page['href'])
    for link in soup.find_all('a', href=True):  # Only consider <a> tags with an 'href' attribute
        if 'aftercursor' in link.get('href', ''):  # Use .get() to avoid KeyError
            next_page = link['href']
            #print(next_page)
    
            
    if next_page:
        #next_cursor = next_page['href']  # Get the new URL with updated aftercursor
        url = 'https://www.nfl.com' + next_page
        #print(url)# Construct new URL for the next page
        

    
df.to_csv(r'/Users/henrybergeson/Documents/NFL Player Data/Player Data 5.csv')



