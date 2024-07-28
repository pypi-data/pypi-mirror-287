# StockExchange
stock data featch

    1. nse_main() -
    2. CSV Model -
        Convert Payload json data  data to CSV using Data frame 
        read CSV File => data = pd.read_csv(filename)
        Featch Csv Columns=> data.columns
        target = data.iloc[:, 5:]
        method- csv_data_model(filename,symbol,start_date,end_date)
        parameter -  filename, symbol, start_date, end_date

    3. Graph Model - 
        csv file data(CSV Model) represent as  graphical  format 
        Method - graph(data,symbol,start_date,end_date)
        parameter – data – CSV data  , symbol,start_date,end_date

        use - 
        symbol = 'BAJFINANCE
        series = 'EQ'
        start_date = ('12-05-2023')
        end_date = ('12-06-2023')
        data = pd.read_csv(filename)
        graph(data,symbol,start_date,end_date)

    4. Equity Pre Data-
        Equity pre histary featch 
        Method - equity_predata(symbol, series, start_date, end_date)
        parameter – Symbol, series, Start Date, End Date 
        Use - 
        symbol = 'BAJFINANCE
        series = 'EQ'
        start_date = ('12-05-2023')
        end_date = ('12-06-2023')
        equity_predata(symbol, series, start_date, end_date)

        Output - 
            • Create CSV File  of start date to end date  data 
                _id
                CH_SYMBOL
                Outcome
                CH_SERIES
                CH_MARKET_TYPE
                CH_TRADE_HIGH_PRICE
                CH_TRADE_LOW_PRICE
                CH_OPENING_PRICE
                CH_CLOSING_PRICE
                CH_LAST_TRADED_PRICE
                CH_LAST_TRADED_PRICE
                CH_PREVIOUS_CLS_PRICE
                CH_TOT_TRADED_QTY
                CH_TOT_TRADED_VAL
                CH_52WEEK_HIGH_PRICE
                CH_52WEEK_LOW_PRICE
                CH_TOTAL_TRADES
                CH_ISIN
                CH_TIMESTAMP
                TIMESTAMP
                createdAt
                updatedAt
                __v
                VWAP
                mTIMESTAMP

            • Plot graph in linear scal  using Graph method 


    6. Equity List- 
        NSE listed company List.
        Method-  equitytop_loosers()
        predata – MCAP31032023_0.xlsx (Download using link https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies)
        output – Teminal output Symbol of listed company
                Create CSV File 
                    Sr. No.
                    Symbol
                    Company Name
                    Market capitalization as on March 31, 2023 (Rs in Lakhs)

    7. Fno List -
        Futures and Options data file.
        Method – fno_list()
        Output - fnolist, count
            CSV File 

    8. Equity Top Gainers-
        Method – equitytop_gainers()
        output – create top gainer  csv file 


    9. Equity Top Loosers-
        Method – equitytop_loosers()

    10.  Option Chain-
        Option chain data dispaly in terminal 
        Indices OPTION – NIFTY, FINNIFTY, BANKNIFTY
        Equities  OPTION -  all symbol
        method  -optionchain(symbol)
        Use - fnolist = optionchain('NIFTY')		
	
    11. Top 25  Valume -
        method – top_valume()
        output – create csv File 


    12. MOST ACTIVE EQUITIES -
        method – active_equities(Num)
        parameter –> num – equities  num of stock 
        use -  active_equities(10)
        output -> create csv file top 10 active quities


    13. 52week High / Low stock -
        method – highorlow_52week(range)
        parameter ->range – “high”  (52week High Stock)
                          - “low”    (52week Low Stock)
        use  - highorlow_52week(“ high”)



    14 Volume Deliverable details data-
        methiod - VolumeDeliverable_moredetails(Symbol, fromdate, todate)
        parameter - symbol = 'ADANIENSOL'
                    fromdate=('26-07-2024')
                    todate=('26-07-2024')
        use -   month data  in ditails ltp
            VolumeDeliverable_moredetails(Symbol, fromdate, todate)

    15 Volume Deliverable -
        methiod - VolumeDeliverable(Symbol, fromdate, todate)
        parameter - symbol = 'ADANIENSOL'
                    fromdate=('26-07-2024')
                    todate=('26-07-2024')
        use - VolumeDeliverable(Symbol, fromdate, todate)