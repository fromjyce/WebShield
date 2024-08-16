import requests as re
from urllib3.exceptions import InsecureRequestWarning, LocationParseError, NameResolutionError
import urllib3
from urllib3 import disable_warnings
from bs4 import BeautifulSoup
import pandas as pd
import feature_extraction as fe

disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#phishing sites
#URL_file_name = "verified_online.csv"
#df = pd.read_csv(URL_file_name, header=None, names=['index', 'url'])

#normal sites
URL_file_name = "tranco_list.csv"
df = pd.read_csv(URL_file_name, header=None, names=['index', 'url'])

print(df.columns)
print(df.info())
print(df.shape)