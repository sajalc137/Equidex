from bs4 import BeautifulSoup as BSoup
import pandas as pd
import requests

def get_data(ticker):
    try:
        url = "https://www.screener.in/company/"
        url += str(ticker)
        response = requests.get(url)
        response.raise_for_status()
    except:
        return None

    soup = BSoup(response.content, 'html.parser')

    ratios = soup.find('ul', id='top-ratios')
    
    list_items = ratios.find_all('li')
    data = []
    for item in list_items:
        spans = item.find_all('span')
        row_data = [span.text.strip() for span in spans]
        data.append(row_data)
    df = pd.DataFrame(data)
    col=[0,2]
    row=[0,1,3,4,5,7]
    df=df.iloc[row,col]

    return dict(zip(df[0], df[2]))
