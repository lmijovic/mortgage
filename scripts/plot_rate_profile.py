from utils import sort_and_filter

import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os 

plt.rcParams.update({'font.size': 16})

# some currently hard-coded values 
# horizontal and vertical grid lines
hlines = (0,2,3,4,5,6,7,10)
vlines = ("01-01-2000","01-01-2005","01-01-2010","01-01-2015","01-01-2020")
copyright="Data source: https://www.ons.gov.uk, (c) OGL3.0"
#copyright="https://www.bankofengland.co.uk & https://www.ons.gov.uk, (c) OGL3.0"
#copyright+="\nhttps://fred.stlouisfed.org" 
yaxis_label="Rate"

date_format = '%d-%m-%Y'
default_start = "01-01-1000"
default_end = "31-01-3000"

parser = argparse.ArgumentParser()
parser.add_argument('--infile', default="", help="date,value csv", dest="infile")
parser.add_argument('--infile2', default="", help="[ optional, second date,value csv ]", dest="infile2")
parser.add_argument('--infile3', default="", help="[ optional, third date,value csv ]", dest="infile3")
parser.add_argument('--infile4', default="", help="[ optional, fourth date,value csv ]", dest="infile4")
parser.add_argument('--start', default=default_start, help="start date d-m-Y", dest="start")
parser.add_argument('--end', default=default_end, help="end date d-m-Y", dest="end")
# plot cosmetics:
parser.add_argument('--label', default="data1", help="legend label", dest="label")
parser.add_argument('--label2', default="data2", help="[ optional, second legend label ]", dest="label2")
parser.add_argument('--label3', default="data3", help="[ optional, third legend label ]", dest="label3")
parser.add_argument('--label4', default="data4", help="[ optional, fourth legend label ]", dest="label4")

args = parser.parse_args()

## here arg name is identical to destination 
print("\nExample command:\n")
command = "python " + os.path.basename(__file__)
for var in vars(args):
    command += " --"+var
    command += "="+str(vars(args)[var])
print(command)
print("\n")

infile = vars(args)["infile"]
infile2 = vars(args)["infile2"]
infile3 = vars(args)["infile3"]
infile4 = vars(args)["infile4"]
date_start =datetime.strptime(vars(args)["start"],date_format)
date_end =datetime.strptime(vars(args)["end"],date_format)
label = vars(args)["label"]
label2 = vars(args)["label2"]
label3 = vars(args)["label3"]
label4 = vars(args)["label4"]

if (infile==""):
    print("\n please provide --infile \n")
    exit(0)


date_col = 'Date'
val_col = 'Value'
headers = [date_col,val_col]


# process and plot first file:
df = pd.read_csv(infile,names=headers, comment='#')
df[date_col]= pd.to_datetime(df[date_col],format='mixed',dayfirst=True)
df = sort_and_filter(df,date_col,date_start,date_end)

ax = df.plot(x=date_col,y=val_col,color='blue',legend=True,label=label, figsize=(12.5, 5))


# plot cosmetics
for line in hlines:
    ax.axhline(y=line,color='lightgray',linestyle='--')

for line in vlines:
    line_date = x=datetime.strptime(line,date_format)
    if (line_date > date_start and line_date < date_end):
        ax.axvline(x=datetime.strptime(line,date_format),
                   color='lightgray',linestyle='--')

plt.xlabel('',horizontalalignment='right', x=1.0)
plt.ylabel(yaxis_label,horizontalalignment='right', y=1.0)
plt.text( 1.01, 0.0, copyright, fontsize=7, color='gray',
          verticalalignment="bottom",rotation="vertical", transform=plt.gca().transAxes)

if (infile2 != ""):
    df = pd.read_csv(infile2,names=headers, comment='#')
    df[date_col]= pd.to_datetime(df[date_col],format='mixed',dayfirst=True)
    df = sort_and_filter(df,date_col,date_start,date_end)
    df.plot(ax=ax, x=date_col,y=val_col,color='orange',label=label2) 
    #df.plot(ax=ax, x=date_col,y=val_col,color='blue',style='--',label=label2) 

if (infile3 != ""):
    df = pd.read_csv(infile3,names=headers, comment='#')
    df[date_col]= pd.to_datetime(df[date_col],format='mixed',dayfirst=True)
    df = sort_and_filter(df,date_col,date_start,date_end)
    df.plot(ax=ax, x=date_col,y=val_col,color='red',label=label3)

if (infile4 != ""):
    df = pd.read_csv(infile4,names=headers, comment='#')
    df[date_col]= pd.to_datetime(df[date_col],format='mixed',dayfirst=True)
    df = sort_and_filter(df,date_col,date_start,date_end)
    df.plot(ax=ax, x=date_col,y=val_col,color='purple',label=label4) 
    #df.plot(ax=ax, x=date_col,y=val_col,color='red',style='--',label=label4) 

plt.xlim(date_start,date_end)
plt.legend(frameon=False)
plt.tight_layout()
plt.savefig("fig.pdf")
plt.savefig("fig.png", dpi=900)
plt.show()

