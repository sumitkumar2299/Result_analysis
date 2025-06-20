import requests
from bs4 import BeautifulSoup
import time

# Looping registration number 1 to 62
for i in range(1, 63):  
    reg_no = f"22155135{str(i).zfill(3)}"
    url = f"https://results.beup.ac.in/ResultsBTech4thSem2024_B2022Pub.aspx?Sem=IV&RegNo={reg_no}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", id = "ContentPlaceHolder1_GridView1")
    if not table:
        print(f"No result found for RegNo: {reg_no}")
        continue

    print(f"Result for RegNo: {reg_no}")
    
    for row in table.find_all("tr"):
        columns = row.find_all("td")
        if columns:
            data = [col.text.strip() for col in columns]
            print(" | ".join(data))
    
    print("-" * 50)
    time.sleep(1)  # delay for 1 second on server so that i can't get blocked my ip. 
