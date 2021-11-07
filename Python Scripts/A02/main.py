from twelvedata import TDClient
import json
import pprint 
import sys

# Initialize client - apikey parameter is requiered
td = TDClient(apikey="2733f8250e3741eda43d25df9cbe0943")


def getStocks(year,month,day):
  # Construct the necessary time series
  #print(f"{year}-{month}-{day}")
  ts = td.time_series(
      symbol="GOOG",
      interval="1h",
      outputsize=1000,
      timezone="America/New_York",
      start_date=f"{year}-{month}-{day}",
  )
  return ts.as_json()


def usage():
  print("Usage:")
  print("\tpython main.py YYYY MM DD")
  print("\tpython main.py 2021 08 03")
  sys.exit()

if __name__=='__main__':

  print(sys.argv)
  if len(sys.argv) < 4:
    usage()

  y = sys.argv[1]
  m = sys.argv[2]
  d = sys.argv[3]


  data = getStocks(y,m,d)

  print(type(data))

  print(len(data))

  print(data[0])

  dayDict = {}

  for row in data:
    y = row['datetime'][:4]
    m = row['datetime'][5:7]
    d = row['datetime'][8:10]
    print(y,m,d)
    print(row)
    if not d in dayDict:
      dayDict[d] = []
    
    dayDict[d].append(row)


  pprint.pprint(dayDict[sys.argv[3]])

# tuples () immutable 
# lists [] mutable
# dictionaries {} mutable

# Returns pandas.DataFrame
#print(ts.as_pandas())

# pip install pandas
# pip3 install websocket
# python -m pip install twelvedata
# python3 -m pip install package name