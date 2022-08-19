# new version of pido-weatherstation data visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse
import datetime as dt
from datetime import timedelta

STARTDATE = pd.Timestamp("2022-06-30 00:00:00")

# parse cmdline arguments
parser = argparse.ArgumentParser(description='Weatherstation plotting API')

parser.add_argument('-s', dest='startdate', type=pd.Timestamp,
                    help='starting date, format example: \
                    "2022-06-17 00:00:00"')
parser.add_argument('-t', '--today', action="store_true",
                    help='show graphs for today')
parser.add_argument('-d', '--days', type=int, metavar='N',
                    help='show graphs for last N days')

args = parser.parse_args()

if args.startdate:
    startdate = args.startdate
elif args.today:
    print("showing data for today...")
    startdate = pd.Timestamp(dt.date.today())
elif args.days:
    today = pd.Timestamp(dt.date.today())
    startdate = today - timedelta(days=args.days)
else:
    startdate = STARTDATE

myFmt = mdates.DateFormatter('%d.%m. %H:%M')


headers = ['time', 'temp', 'p']
dtypes = {'time': 'str', 'temp': 'float', 'p': 'float'}
parse_dates = ['time']

data = pd.read_csv('./data.log', sep=',', header=None, names=headers,
                   dtype=dtypes, parse_dates=parse_dates)

plt.xkcd()

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12, 16),
                         tight_layout=True)
data = np.array(data)

# only show the data starting from 'startdate'
dataslice = data[data[:, 0] > startdate]
axes[0].plot(dataslice[:, 0], dataslice[:, 1],
             label="Temperatur [C]", color="red")
axes[0].text(dataslice[-1, 0], dataslice[-1, 1]+0.5,
             s="{}".format(dataslice[-1, 1]),
             bbox=dict(facecolor='red', alpha=0.5))

axes[0].legend(loc=2)

axes[1].plot(dataslice[:, 0], dataslice[:, 2], label="Druck [hPa]")
axes[1].text(dataslice[-1, 0], dataslice[-1, 2]+1,
             s="{}".format(dataslice[-1, 2]),
             bbox=dict(facecolor='cornflowerblue', alpha=0.5))

# set xy-Axis formats
axes[1].xaxis.set_major_formatter(myFmt)
axes[1].yaxis.set_major_formatter('{x:.1f}')
axes[1].legend(loc=0)

plt.show()
