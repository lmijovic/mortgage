import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import argparse


date_format = '%d-%m-%Y'
default_start = "01-01-1000"
default_end = "31-01-3000"



parser = argparse.ArgumentParser(description="",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--start", default=default_start, help="start date "+date_format, dest="start")
parser.add_argument("--end", default=default_end, help="end date "+date_format, dest="end")
args = parser.parse_args()

#print(args)
#config = vars(args)
#print(config)
date_start =datetime.strptime(vars(args)["start"],date_format)
date_end =datetime.strptime(vars(args)["end"],date_format)
print("plotting data for:", date_start, date_end)

plt.rcParams.update({'font.size': 16})

headers = ['Date','Value']
#df = pd.read_csv('virusi.txt',names=headers)
df = pd.read_csv('../data/BOE_interest_rate.csv',names=headers, comment='#')
df['Date']= pd.to_datetime(df['Date'])

print('----- Working with rates file ----- ')
print(df.tail(5))


df = df.sort_values(by=['Date'])

# filter acc to range
df = df[(df['Date'] > date_start)]
df = df[(df['Date'] <= date_end)]

df.plot(x='Date',y='Value',legend=None)

plt.xlabel('',horizontalalignment='right', x=1.0)
plt.ylabel('Rate',horizontalalignment='right', y=1.0)

plt.tight_layout()
plt.savefig("plot.pdf")
plt.savefig("plot.png", dpi=900)
plt.show()
