# daily_reminder.py

# Prompt user for task description
task = input("Enter your task: ")

# Prompt user for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt user to check if task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Customized message based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that is time-sensitive. Plan accordingly.")
        else:
            print(f"Note: '{task}' is a medium priority task. Complete it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority but time-bound task. Don’t forget to do it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use high, medium, or low.")
