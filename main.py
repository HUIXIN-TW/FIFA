import generateFile as gFile
import monitorChange as mChange
import sys
import json

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 
         1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

if len(sys.argv) == 2 and int(sys.argv[1]) in years:
        years=[sys.argv[1]]
elif len(sys.argv) == 1:
    years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 
             1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
else:
    print("Try: python3 main.py {year} to get the date in a specific year. Or python3 main.py to get all data.")
    sys.exit(1)

gFile.historical_data(years)

# test
# print(gFile.historical_data(years))

# with open("email.json") as f:
#     data = json.load(f)
#     print(mChange.send_email(data))