import requests
from bs4 import BeautifulSoup
import csv
import time

# Open file as simple text file so you can print custom header lines:
filename = "beup_practical_results_all_students_custom_format.csv"

with open(filename, mode="w", encoding='utf-8') as file:

    # Looping registration number 1 to 62
    for i in range(1, 63):
        reg_no = f"22155135{str(i).zfill(3)}"

        url = f"https://results.beup.ac.in/ResultsBTech4thSem2024_B2022Pub.aspx?Sem=IV&RegNo={reg_no}"

        print(f"Fetching result for RegNo: {reg_no} ...")

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find Practical Table
            table = soup.find("table", id="ContentPlaceHolder1_GridView2")

            if not table:
                print(f"No Practical result found for RegNo: {reg_no}")
                continue

            # Write "Result for RegNo: ..." header in the file
            file.write(f"Result for RegNo: {reg_no}\n")
            file.write("Subject_Code,Subject_Name,External,Internal,Total,Grade,Credit\n")

            # Extract rows (skip header row)
            rows = table.find_all("tr")[1:]

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

                    # Write this row in CSV format to the file
                    file.write(f"{subject_code},{subject_name},{external},{internal},{total},{grade},{credit}\n")

            file.write("\n")  # empty line between students

            print(f"Saved Practical result for RegNo: {reg_no}")

            time.sleep(0.5)  # polite delay

        except Exception as e:
            print(f"Error fetching RegNo {reg_no}: {e}")

print(f"\nAll Practical results saved to {filename}")
