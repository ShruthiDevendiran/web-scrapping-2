from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome('/chromedriver.exe')
browser.get(START_URL)

dwarf_stars_data = []
time.sleep(10)

def scrape(url):
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parser')

        temp_list = []

        tables = soup.find_all('table')
        table_body = tables.find_all('tbody')
        table_rows = table_body.find_all('tr')

        for rows in table_rows:
                table_cols_data = rows.find_all('td')
                table_cols = table_cols_data.strip()

                temp_list.append(table_cols)

        dwarf_stars_data.append(temp_list)

brown_stars_data = []

for i in range(0,len(dwarf_stars_data)):
        Star_name = dwarf_stars_data[i][0]
        Radius = dwarf_stars_data[i][9]
        Mass = dwarf_stars_data[i][8]
        Distance = dwarf_stars_data[i][5]      

        required_data = [Star_name,Radius,Mass,Distance]

        brown_stars_data.append(required_data)

scrape(START_URL)

headers = ['Star_name','Radius','Mass','Distance']

brown_star_df_1 = pd.DataFrame(brown_stars_data,colums=headers)

brown_star_df_1.to_csv("brown_stars.csv",index = True, index_label="id")



    