#graphics
import matplotlib.pyplot as plt
#data management
import pandas as pd
#numerical operations
import numpy as np
#api yahoo finance
import yfinance as yf

class FinanceManager:
    
    def __init__(self,inputs):
        self.inputs = inputs
        print(f"welcome {inputs['username']} to the financial manager app!"+'\n')
        print('----------'+'\n')
        
        #always run
        self.readdb()
        run = True
        while run:
            self.MENU()
            run = self.keeprunning()
            
    #keep running app
    def keeprunning(self):
        keep = input('Do you want to perform another action? (y/n): ')
        if keep == 'y' or keep == 'yes':
            return True
        else:
            return False
        
    #app menu
    def MENU(self):
        print('----------'+'\n')
        print('--- Menu ---')
        print('1. GENERATE REPORT')
        print('2. ADD LOG')
        print('3. Financial Tickers')
        print('\n'+'----------')
        request = input('Option number to perform: ')
        print('\n')
        self.handleMenuRequest(request)
        
    #handle menu request
    def handleMenuRequest(self,request):
        if request == '1':
            self.report()
        elif request == '2':
            self.addlog()
        elif request == '3':
            self.getTickers()
        else:
            print('Entry not valid D:')
        
    #generate financial report
    def report(self):
        self.balance()
        self.graphlogs()
        
    #calculate current balance
    def balance(self):
        b = self.data['AMOUNT'].sum()
        print(f'Current Balance: ${b}')
        
    #graph historical logs
    def graphlogs(self):
        plt.figure(figsize = (10,6))
        plt.title('Historical Development of Logs')
        
        #simple log 
        plt.plot(self.data['AMOUNT'],'o',label='Individual Log')
        #cummulative
        plt.plot(np.cumsum(self.data['AMOUNT']),'--',label='Cummulative')
        
        plt.legend()
        plt.show()
        
    #read database
    def readdb(self):
        self.data = pd.read_csv(self.inputs['data_route'])
        
    #save database
    def savedb(self):
        self.data.to_csv(self.inputs['data_route'],index=False)
        
    #get log
    def getlog(self):
        print('----------'+'\n')
        day = input('Day number: ')
        month = input('Month number: ')
        year = input('Year number: ')
        amount = float(input('Amount: '))
        category = input('Category: ')
        subcategory = input('Subcategory: ')
        comment = input('Comment: ')
        print('\n'+'----------')
        date = day+'/'+month+'/'+year
        log = [date,amount,category,subcategory,comment]
        return log
        
    #add log
    def addlog(self):
        log = self.getlog()
        self.data.loc[len(self.data)] = log
        self.savedb()
        
    #calculates compound interest
    def compound(self,initial,rate,time):
        return initial*(1+rate/100)**time
    
    def getTickers(self):
        self.downloadTickers(self.selectTickers())
        self.graphTickers()
        self.tickersReport()
        
    def graphTickers(self):
        plt.figure(figsize = (10,6)); self.tickers['Close'].plot(); plt.title('Tickers Time Series'); plt.show()
    
    def selectTickers(self):
        tickers = []
        add = True
        while add:
            t = input('Ticker: ')
            tickers.append(t)
            s = input('add another ticker? (y/n): ')
            if s == 'y':
                add = True
            else:
                add = False
        return tickers
    
    #download ticker information:
    def downloadTickers(self,tickers):
        ticker_string = ""
        for i in range(len(tickers)-1):
            ticker_string = ticker_string + tickers[i] + " "
        ticker_string = ticker_string + tickers[-1]
        self.tickers = yf.download(tickers = ticker_string,  # list of tickers
            period = "1y",         # time period
            interval = "1d",       # trading interval
            prepost = False,       # download pre/post market hours data?
            repair = True)         # repair obvious price errors e.g. 100x?
        
    #financial report for tickers
    def tickersReport(self):
        pass