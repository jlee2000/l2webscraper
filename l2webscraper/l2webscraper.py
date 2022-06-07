import requests
import pandas as pd
import sys
from io import BytesIO

urls = ['https://optimistic.etherscan.io/chart/verified-contracts?output=csv', 'https://arbiscan.io/chart/verified-contracts?output=csv', 'https://polygonscan.com/chart/verified-contracts?output=csv']

# to use command-line arguments, use the following format:
#   python3 l2webscraper.py "URL_1.xyz" "URL_2.com" "URL_3.org" ...
for i in range(1, len(sys.argv)):
    urls.append(sys.argv[i])

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

dfs = {}
for url in urls:
    r = requests.get(url, headers=header)
    dfs[url] = pd.read_csv(BytesIO(r.content))
for df in dfs:
    print(df, dfs[df])
