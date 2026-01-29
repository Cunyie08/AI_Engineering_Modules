import csv
from pathlib import Path

workspace = Path("participant_pkg")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contacts.csv"
csv_file


header_row = ["Name", "Age", "Phone", "Track"]

