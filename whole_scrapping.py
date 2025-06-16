import requests
from bs4 import BeautifulSoup
import csv
import time

filename = "beup_full_results_combined.csv"

with open(filename, mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for i in range(1, 63):  # 001 to 062
        reg_no = f"22155135{str(i).zfill(3)}"
        url = f"https://results.beup.ac.in/ResultsBTech4thSem2024_B2022Pub.aspx?Sem=IV&RegNo={reg_no}"

        print(f"Fetching Result for RegNo: {reg_no}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # ----------- THEORY TABLE (GridView1) -------------
        table_theory = soup.find("table", id = "ContentPlaceHolder1_GridView1")

        if table_theory:
            #  header
            writer.writerow([f"Result for RegNo: {reg_no}"])
            writer.writerow(["Subject_Code", "Subject_Name", "External", "Internal", "Total", "Grade", "Credit"])
            
            rows = table_theory.find_all("tr")[1:]  # skip header
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
        else:
            print(f"No THEORY result found for RegNo: {reg_no}")

        #PRACTICAL TABLE
        table_practical = soup.find("table", id = "ContentPlaceHolder1_GridView2")

        if table_practical:
            # Writing PRACTICAL section header
            writer.writerow(["PRACTICAL Results"])
            writer.writerow(["Subject_Code", "Subject_Name", "External", "Internal", "Total", "Grade", "Credit"])
            
            rows = table_practical.find_all("tr")[1:]  # skip header
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
        else:
            print(f"No PRACTICAL result found for RegNo: {reg_no}")

        # Adding blank line section between studnets 
        writer.writerow([])
        writer.writerow([])

        print(f"Saved combined result for RegNo: {reg_no}")
        time.sleep(1)  # polite delay

print(f"\nAll results saved to {filename}")
