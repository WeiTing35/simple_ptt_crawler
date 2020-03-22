
import requests
import datetime
import pandas as pd
# 使用jupyter notebook 要加：
# %matplotlib inline

url = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&crumb=hP2rOschxO0"

response = requests.get(url)
print(response.text)
with open('file.csv', 'w') as f:
    f.writelines(response.text)

