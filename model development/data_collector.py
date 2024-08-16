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

URL_list = df['url'].to_list()

print(len(URL_list))

col = URL_list[:]

tag = "http://"
collection_list = [tag + url for url in col]

re.packages.urllib3.disable_warnings(re.packages.urllib3.exceptions.InsecureRequestWarning)

def create_structured_data(url_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    data_list = []
    for i, url in enumerate(url_list):

        # Ensure the URL is properly formatted
        if not url.startswith(("http://", "https://")) or url.startswith("."):
            print(i, ". Skipping malformed URL: ", url)
            continue

        try:
            response = re.get(url, headers=headers, verify=False, timeout=4)
            if response.status_code != 200:
                print(i, ". HTTP connection was not successful for the URL: ", url)
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                vector = fe.create_vector(soup)
                vector.append(str(url))
                data_list.append(vector)

        # Handle specific exceptions
        except (LocationParseError, NameResolutionError) as e:
            print(i, f" --> Skipping due to {type(e).__name__}: {e}")
            continue
        except re.exceptions.RequestException as e:
            print(i, " --> ", e)
            continue

    return data_list