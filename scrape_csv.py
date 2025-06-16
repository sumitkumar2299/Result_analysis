import requests
from bs4 import BeautifulSoup
import csv
import time

filename = "beup_results_clean.csv"

with open(filename, mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for i in range(1, 63):  # 001 to 062
        reg_no = f"22155135{str(i).zfill(3)}"
        url = f"https://results.beup.ac.in/ResultsBTech4thSem2024_B2022Pub.aspx?Sem=IV&RegNo={reg_no}"

        print(f"Fetching Result for RegNo: {reg_no}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", id = "ContentPlaceHolder1_GridView1")
        if not table:
            print(f"No result found for RegNo: {reg_no}")
            continue

        # header row 
        writer.writerow([f"Result for RegNo: {reg_no}"])
        writer.writerow(["Subject_Code", "Subject_Name", "External", "Internal", "Total", "Grade", "Credit"])

        rows = table.find_all("tr")[1:]  # skip header

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 7:
                subject_code = cols[0].text.strip()
                subject_name = cols[1].text.strip()
                external = cols[2].text.strip()
                internal = cols[3].text.strip()
                total = cols[4].text.strip()
                grade = cols[5].text.strip()
                credit = cols[6].text.strip()

                writer.writerow([subject_code, subject_name, external, internal, total, grade, credit])

        # Adding blank line between students. 
        writer.writerow([])

        time.sleep(1)
