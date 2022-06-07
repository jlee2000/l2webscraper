import requests
import pandas as pd
from io import BytesIO
urls = ['https://optimistic.etherscan.io/chart/verified-contracts?output=csv', 'https://arbiscan.io/chart/verified-contracts?output=csv', 'https://polygonscan.com/chart/verified-contracts?output=csv']
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

dfs = {}
for url in urls:
    r = requests.get(url, headers=header)
    # print(r.content)
    dfs[url] = pd.read_csv(BytesIO(r.content))
    # print(dfs)
for df in dfs:
    print(df, dfs[df])
