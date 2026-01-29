import csv
import file_ops
from pathlib import Path


workspace = Path("participant_pkg")
csv_file = workspace / "contacts.csv"
csv_file



def get_name():

    while True:
        print("\nWelcome to NCC workshop") # Press 1
        print("1. Registration")
        print("2. Enquiries")

        choice = input("please enter your selection: ")

        if choice == "1":
            try:
                name = str(input("Please enter your name: ").strip())
                if (len(name) == 0) or (name.isdigit()== True):
                    raise ValueError("Invalid input!\n Enter a name")
                else:
                    return (name)  
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error:", e)
                



def get_age():

    while True:
        try:
            age= int(input("Please enter your age: "))
            if age <= 12:
                print("Too young to register")
            else:
                return (age)
        except ValueError:
            print("Invalid input, input a number")
        except Exception as e:
            print("Unexpected error:", e)
          
def get_phone():

    while True:
        try: 
            phone = input("Please enter your Phone: ")
            if (len(phone) != 11) or (phone.isdigit() == False):
                raise ValueError("Invalid input! please enter 11 digits")  
            else:
                    return (phone) 
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error:", e)
        
def get_track():

    while True:
        try:
            track = str(input("Please enter your track: "))
            if (len(track) == 0) or (track.isdigit()== True):
                raise ValueError("Invalid input!\n Enter a track")
            else:
                return (track)  
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error:", e)


# 

def main():
    while True:
        try:
            name = get_name()
            age = get_age()
            phone = get_phone()
            track = get_track()

            particicant = {"Name": name, "Age": age, "Phone": phone, "Track": track}

            try:
                file_ops.save_participant(csv_file, particicant)
                print("Data written to csv file!")

                update_participant = input("Do you want to add another contact? Yes or No: ")
                if update_participant == "no":
                    print("Saved contact")
                    file_ops.load_participant(csv_file)
            except Exception:
                print("Unexpected error encountered while loading the contact")
        except Exception as e:
            print("Unexpected error:", e) 


if __name__ == "__main__":
     main()





