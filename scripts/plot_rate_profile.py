import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import argparse
import os 

date_format = '%d-%m-%Y'
default_start = "01-01-1000"
default_end = "31-01-3000"
default_inflation = True

parser = argparse.ArgumentParser()
parser.add_argument('--start', default=default_start, help="start date d-m-Y", dest="start")
parser.add_argument('--end', default=default_end, help="end date d-m-Y", dest="end")
parser.add_argument('--inflation', default=default_inflation, help="plot inflation ", dest="inflation")
args = parser.parse_args()

## here arg name is identical to destination 
print("\nExample command:\n")
command = "python " + os.path.basename(__file__)
for var in vars(args):
    command += " --"+var
    command += "="+str(vars(args)[var])
print(command)
print("\n")

date_start =datetime.strptime(vars(args)["start"],date_format)
date_end =datetime.strptime(vars(args)["end"],date_format)
inflation = vars(args)["inflation"]
print("plotting data for:", date_start, date_end)

plt.rcParams.update({'font.size': 16})

headers = ['Date','Value']
df = pd.read_csv('../data/BOE_interest_rate_Aug23.csv',names=headers, comment='#')
df['Date']= pd.to_datetime(df['Date'])

print('----- Working with rates file ----- ')
print(df.tail(5))


df = df.sort_values(by=['Date'])

# filter acc to range
df = df[(df['Date'] > date_start)]
df = df[(df['Date'] <= date_end)]

ax = df.plot(x='Date',y='Value',legend=True,label="BoE rate")

hlines = (0,2,3,4,5,6,7,10)
for line in hlines:
    ax.axhline(y=line,color='lightgray',linestyle='--')

vlines = ("01-01-2000","01-01-2005","01-01-2010","01-01-2015","01-01-2020")
for line in vlines:
    line_date = x=datetime.strptime(line,date_format)
    if (line_date > date_start and line_date < date_end):
        ax.axvline(x=datetime.strptime(line,date_format),
                   color='lightgray',linestyle='--')

plt.xlabel('',horizontalalignment='right', x=1.0)
plt.ylabel('Rate',horizontalalignment='right', y=1.0)


if (inflation):
    df = pd.read_csv('../data/inflation/cpi_aug23.csv',names=headers, comment='#')
    df['Date']= pd.to_datetime(df['Date'], yearfirst=True)

    print('----- Working with inflation file ----- ')
    print(df.tail(5))

    df = df.sort_values(by=['Date'])
    
    # filter acc to range
    df = df[(df['Date'] > date_start)]
    df = df[(df['Date'] <= date_end)]
    df.plot(ax=ax, x='Date',y='Value',color='orange',label="CPI inflation") 
    #ax = df.plot(x='Date',y='Value',color='orange',legend=None)

plt.legend(frameon=False)
plt.tight_layout()
plt.savefig("uk_monetary.pdf")
plt.savefig("uk_monetary.png", dpi=900)
plt.show()

