import requests
from datetime import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def server_request(url):
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    try:
        payload = requests.get(url, headers=headers).json()
    except ValueError:
        s = requests.Session()
        payload = s.get("http://nseindia.com", headers=headers)
        payload = s.get(url, headers=headers).json()

    return payload


def top_valume():
    url= 'https://www.nseindia.com/api/live-analysis-volume-gainers'
    payload = server_request(url)  
    Date  = payload['timestamp']
    df_list = payload['data']
    df=pd.DataFrame(df_list)
    df.to_csv('Valume '+Date+'.csv') 
    print("-------")
    return payload


def active_equities(Num):
    url= f'https://www.nseindia.com/api/live-analysis-most-active-securities?index=volume&limit={Num}'
    payload = server_request(url) 
   
    Date  = payload['timestamp']
    df_list = payload['data']
    df=pd.DataFrame(df_list)
    df.to_csv('active_equities '+Date+'.csv') 
    return payload


# high or low
def highorlow_52week(range):
    if range == 'high' or range == 'low':
        url= f'https://www.nseindia.com/api/live-analysis-52Week?index={range}'
        payload = server_request(url) 
        Date  = payload['timestamp']
        df_list = payload['dataLtpGreater20']

        df=pd.DataFrame(df_list)
        df.to_csv(f'52week {range} ' +Date+'.csv') 
    else:
        msg = 'Wrong Parameter please enter currect parameter (high or low)'
        print(msg)
        payload = {'message':msg}
    return payload
    

def equity_predata(symbol, series, start_date, end_date):

    url = f"https://www.nseindia.com/api/historical/cm/equity?symbol={symbol}&series=[%22{series}%22]&from={start_date}&to={end_date}"
    payload = server_request(url)
    df = pd.DataFrame.from_records(payload["data"])
    file_name= symbol+' predata.csv'
    df.to_csv(file_name, index=None)
    
    # df.to_csv(r'{}'.format(file_name), index=None)   

    csv_data_model(file_name,symbol,start_date,end_date)

    return pd.DataFrame.from_records(payload["data"])


def fno_list():
    # Futures and Options list  
    url = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O"
    payload = server_request(url)

    df = pd.DataFrame.from_records(payload["data"])
    df.to_csv(r'fno_list.csv', index=None)
    fnolist = [] # Futures and Options list name
    count = 0 # Futures and Options count
    for x in range(count, len(payload['data'])):
        count = count+1
        fnolist = fnolist+[payload['data'][x]['symbol']]
    return fnolist, count


def equity_list():
    # https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies
    excel_file = pd.read_excel('MCAP31032023_0.xlsx')
    csv_file = excel_file.to_csv('31032023_equity_list.csv', index=False)
    data = pd.read_csv('31032023_equity_list.csv')
    symbol=data.Symbol
    return symbol 

def equitytop_gainers():
    url= 'https://www.nseindia.com/api/liveanalysis/gainers/allSec'
    payload = server_request(url)  
    Date  = payload['gainers']['timestamp']
    df_list = payload['gainers']['data']
    df=pd.DataFrame(df_list)
    df.to_csv('equitytop_gainers'+Date+'.csv') 
    return payload

def equitytop_loosers():
    url= 'https://www.nseindia.com/api/liveanalysis/loosers/allSec'
    payload = server_request(url)  
    Date  = payload['loosers']['timestamp']
    df_list = payload['loosers']['data']
    df=pd.DataFrame(df_list)
    df.to_csv('equitytop_loosers'+Date+'.csv') 
    return payload

def optionchain(symbol):
    symbol_name = symbol.replace('&', '%26')
    if symbol_name == 'NIFTY' or symbol_name == 'FINNIFTY' or symbol_name == 'BANKNIFTY':
        url= 'https://www.nseindia.com/api/option-chain-indices?symbol='+symbol_name
        payload = server_request(url)  
        
    else:
        url= 'https://www.nseindia.com/api/option-chain-equities?symbol='+symbol_name
        payload = server_request(url)

    return payload


def csv_data_model(filename,symbol,start_date,end_date):
    data = pd.read_csv(filename)
    graph(data,symbol,start_date,end_date)
    close_price = data.CH_LAST_TRADED_PRICE
    open_price = data.CH_OPENING_PRICE
    outcome_val = []
    for i, j in zip(close_price, open_price):
        if i < j:
            outcome_val.append(True)
        else:
            outcome_val.append(False)
    data.insert(2, column="Outcome", value=outcome_val)
    print("columns.name --------")
    print(data.columns)
    target = data.iloc[:, 5:]
    # print(target)

    label = data.Outcome
    ml_model(target, label)


def ml_model(target, label):
    train_data, test_data, train_label, test_label = train_test_split(
        target, label, test_size=2)

    # print("train_data", train_data)
    # print("test_data",test_data)
    # print("train_label",train_label)
    # print('test_label',test_label)

    # algo=KNeighborsClassifier()
    # algo.fit(train_data,train_label)

    # predict=algo.predict(test_data)
    # print(predict)

    # test_data_new=([[5,96,74,18,67,33.6,0.997,43]])
    # ans=algo.predict(test_data_new)


def graph(data,symbol,start_date,end_date):
    x = data.CH_TIMESTAMP
    y = data.CH_LAST_TRADED_PRICE
    plt.plot(x, y, color='#58b970', label="Regreation Line")
    plt.scatter(x, y, color='#ef5423', label="scatter Plot")
    plt.xlabel('X-TIMESTAMP')
    plt.ylabel('Y-LAST_TRADED_PRICE')
    plt.legend()
    plt.title(symbol+ ' ' +start_date + ' to '+end_date)
    plt.show()



#symbol month data  (from to date)
def VolumeDeliverable_moredetails(Symbol, fromdate, todate):
    url=f'https://www.nseindia.com/api/historical/securityArchives?from={fromdate}&to={todate}&symbol={Symbol}&dataType=priceVolumeDeliverable&series=ALL'
  
    payload = server_request(url)
    # path = folder_create()
    df_list = payload['data']
    extracted_data = [{'date': entry['CH_TIMESTAMP'],'symbol':entry['CH_SYMBOL'], 'total_traded': entry['CH_TOT_TRADED_QTY'],'delevery_valume': entry['COP_DELIV_QTY'],'last_trade_price': entry['CH_LAST_TRADED_PRICE'],'52WEEK_HIGH_PRICE': entry['CH_52WEEK_HIGH_PRICE']} for entry in df_list]

    df=pd.DataFrame(extracted_data)
    df.to_csv(f'valume_deliverable_all{todate}_{Symbol}.csv') 
    return extracted_data  

#daly delivary valume 
def VolumeDeliverable(Symbol, fromdate, todate):
    url=f'https://www.nseindia.com/api/historical/securityArchives?from={fromdate}&to={todate}&symbol={Symbol}&dataType=deliverable&series=ALL'
  
    payload = server_request(url)
    # path = folder_create()
    df_list = payload['data']
    extracted_data = [{'Symbol': entry['COP_SYMBOL'],'Date':entry['COP_TRADED_DT'], 'Trades_qty': entry['COP_TRADED_QTY'],'delevery_valume': entry['COP_DELIV_QTY']} for entry in df_list]    
    df=pd.DataFrame(extracted_data)
    df.to_csv(f'valume_deliverable'+todate+'.csv') 
    
    return extracted_data


def main():
    symbol = 'BAJFINANCE'
    series = 'EQ'
    start_date = ('12-05-2023')
    end_date = ('12-06-2023')
    predata = equity_predata(symbol, series, start_date, end_date)
    fno_list()
    equitytop_gainers()
    data = equitytop_loosers()
    sy=highorlow_52week('high')
    top_valume()
    

if __name__ == "__main__":
    main()
