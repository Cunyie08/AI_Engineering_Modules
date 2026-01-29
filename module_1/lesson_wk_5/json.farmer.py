from  pathlib import Path
import json
from user import User


workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
json_file = workspace / "users.json"
json_file


fieldnames = ["Name", "Age", "Gender", "Farm Location", "farm Size",]

# class ProfileMgt(User):

def save_profile(json_file):
            json_file = workspace / "users.json"
            with open(json_file, "w", newline="", encoding="utf-8") as f:
                json.dump(fieldnames,f, indent=2)
                json.dump()
            print ("profile added to JSON file successfully")

            # Now read it back
            with open(json_file, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
save_profile(json_file)


