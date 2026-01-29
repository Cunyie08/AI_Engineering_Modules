
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
            reminders.append(activity)
            return f"Activity '{activity}' added to your schedule."
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)
print(add_activity("Enter"))

