'''

convert in.csv of Date,Value from yearfirst to dayfirst
write result to out.csv

'''


import pandas as pd
from datetime import datetime
import csv
import argparse
import os 

headers=['Date','Value']
df = pd.read_csv("in.csv",names=headers, comment='#')
df['Date']= pd.to_datetime(df['Date'], yearfirst=True)
df['Date']=df['Date'].dt.strftime('%d-%m-%Y')
df.to_csv("out.csv",header=False, index=False)
