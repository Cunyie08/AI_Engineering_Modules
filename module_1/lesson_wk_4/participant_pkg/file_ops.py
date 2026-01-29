import csv
from pathlib import Path

workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contacts.csv"
csv_file


fieldnames = ["Name", "Age", "Phone", "Track"]


# Define a csv_file that collects details of the participant
def save_participant(csv_file,participant):
    if type(participant) == dict:
        participant = [participant]
    if csv_file.exists():
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writerows(participant)
        print ("Contact file successfully created")

    else:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(participant)
    print ("Contact file successfully created")
        


def load_participant():

    with open(csv_file, "r", encoding="utf-8") as f:
        load_participant = csv.reader(f)

        for row_number, row in enumerate(load_participant):
            if row_number == 0:
                print(f"Headers: {"|".join(row)}")
                print("-" * 40)
            else:
                name, age, phone, track = row
                print(f"{name}\t{age}\t{phone}\t{track}") 

