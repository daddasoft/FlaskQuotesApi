import requests
from bs4 import BeautifulSoup

URL = "https://www.goalzz.com/?region=-1&area=0&dd=18&mm=9&yy=2021"
session = requests.Session()
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
r = session.get(URL, headers=headers)

print(r.content)
