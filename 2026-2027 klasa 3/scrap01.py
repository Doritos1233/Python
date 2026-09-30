# %%
!pip install beautifulsoup4 requests json

# %%
from bs4 import BeautifulSoup
import requests
import json

# %%
url = "https://egzamin-informatyk.pl/testy-inf03-ee09-programowanie-bazy-danych/"
response = requests.get(url)
bs = BeautifulSoup(response.content, "html.parser")

# %%
pytania = bs.find_all("div", class_="trescE")
odpowiedzA = bs.find_all("div", class_="odpowiedzE")
odpowiedzB = bs.find_all("div", class_="odpowiedzE")
odpowiedzC = bs.find_all("div", class_="odpowiedzE")
odpowiedzD = bs.find_all("div", class_="odpowiedzE")

questions = []
for i in range(0,40):
    odpowiedzA = bs.select(f"div#odpa{i+1}")[0].text
    odpowiedzB = bs.select(f"div#odpb{i+1}")[0].text
    odpowiedzC = bs.select(f"div#odpc{i+1}")[0].text
    odpowiedzD = bs.select(f"div#odpd{i+1}")[0].text

    q = {
            "content": f"{pytania[i].text}",
            "odpA": f"{odpowiedzA}",
            "odpB": f"{odpowiedzB}",
            "odpC": f"{odpowiedzC}",
            "odpD": f"{odpowiedzD}"
    }

    questions.append(q)

questions
with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump(questions, plik, ensure_ascii=False, indent=4)


