import requests
url = "https://results.beup.ac.in/ResultsBTech4thSem2024_B2022Pub.aspx?Sem=IV&RegNo=22155135044"
response = requests.get(url)
html = response.text
# print(html)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,"html.parser")

table = soup.find("table",id = "ContentPlaceHolder1_GridView1")

if table: 
    print("table found")
else: 
    print("table not found")


# extracting data from the table 

if table:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all(["td", "th"])  # headers or data cells
        cols_text = [col.get_text(strip=True) for col in cols]
        print(cols_text)
else:
    print("No table to scrape.")

