#graphics
import matplotlib.pyplot as plt
#data management
import pandas as pd
#numerical operations
import numpy as np
#api yahoo finance
import yfinance as yf
#import FM
from scripts.manager import FinanceManager

inputs = {
    'username': 'BlankHall',
    'data_route': './data/finance.csv'
}

if __name__ == '__main__':
    fm = FinanceManager(inputs)

