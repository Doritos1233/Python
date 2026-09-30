# %% [markdown]
# # import bibliotek
# %%
# !pip install requests
# !pip install beautifulsoup4

# %% [markdown]
# # import

# %%
import requests
from bs4 import BeautifulSoup


# %%
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# %% [markdown]
# # zadanie

# %%
counter = 0
lista = []

div_tag = soup.find("div", class_="side_categories")
ul_tag = div_tag.find("ul")
li_tag = ul_tag.find("li")

for kat in li_tag.find_all("li"):
    counter += 1
    text = kat.text.strip()
    lista.append(text)
    print(f"{counter}. {text}")


