# Creating a To-do List Application for an IOS
from pathlib import Path

file = Path("reminder_files")
file.mkdir(exist_ok=True)
filepath = file / "reminders.txt"
filepath

# list to store all daily or scheduled task
reminders = []

# Function to add a task to the list
def add_activity(activity):
    try:
        if activity == "":
            print("You have to enter an activity")
        elif (activity.isdigit()): 
            raise ValueError("Invalid input!")
        else:
            reminders.append(f"{activity}\n")
            return f"Activity '{activity}' added to your schedule."
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)


# Function to delete a task from the list
def delete_activity(activity):
    if activity in reminders:
        reminders.remove(activity)
        print(f'Activity "{activity}" removed')
    else:
        print('Activity not found!')

# Function to display all added tasks
def view_schedule():
    if reminders:
        print("Your Reminders:")
        for idx, activity in enumerate(reminders, 1):
            print(f"({idx}) {activity}")
    else:
        print("No activity added to your schedule!")

# Function to display saved activity # Still working on it
def save_activity(filepath,reminders):
    if filepath.exists():
        with open(filepath, "a", newline="", encoding="utf-8") as f:
            for activity in reminders:
                print(activity + "\n")
                f.write(activity)
                print ("Saved reminders")
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            print("Lets create it first!")
            for activity in reminders:
                print(activity + "\n")
                f.write(f"My Reminders\n {reminders}\n")


# Function to display commpleted activity
def completed_schedule(activity):
    if activity == 'yes':
        print("Completed")
    else:
        print("Activities yet to be completed!")

# Function to display all added tasks
def edit_schedule(reminders):
    if type(reminders) == list:
        reminders = set(reminders)
        activity = input("Enter an activity to edit: ")
        new_activity = input("Enter new activity: ")
        reminders == (set(reminders))
    reminders.replace(activity, new_activity)
    print(f"Activity replaced in your schedule.")

# Function to flag priority activity
def flagged_activity(activity):
    if reminders[0] == True:
        print("Activity pinned")
        for idx, activity in enumerate(reminders, 1):
            print(f"({idx}) {activity} is pinned")
    else:
        print("No activity pinned!")




# Loop to keep he progrm running untitl user exits the program

def main():
    while True:
        print("\n****Options****")
        print("1. Add new activity")
        print("2. Remove activity")
        print("3. View Schedule")
        print("4. Saved Activity")
        print("5. Completed Activity")
        print("6. Edit Activity")
        print("7. Flagged Activity")
        print("8. Exit")
        
        # Ask user to enter an option
        option = input("Enter an option: ")
        if option == '1':
            activity = input("Enter an activity: ").strip()
            add_activity(activity)
            save_activity(filepath, reminders)
        elif option == '2':
            activity = input("Enter an activity to delete: ").strip()
            delete_activity(activity)
        elif option == '3':
            view_schedule()
        # elif option == '4':
        #     activity = input("Enter an activity to save: ")
        #     save_activity(activity)
        elif option == '5':
            activity = input("Have you completed your activities? Yes or No: ")
            completed_schedule(activity)
        elif option == '6':
            if reminders:
                activity = input("Enter an activity to edit: ")
                new_activity = input("Enter new activity: ")
                print(reminders.replace(activity, new_activity))
            edit_schedule(reminders)
        elif option == '7':
            print("Enter an activity to flag: ")
            flagged_activity(activity)
        elif option == '8':
            print("Exiting program. Have a productive day!")
            break
        else:
            print("Invalid option!, Please enter a valid option.")

if __name__ == "__main__":
     main()
