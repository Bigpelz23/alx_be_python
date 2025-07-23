def main():
    # EXACT input prompts as required
    task = input("Enter your task:")
    priority = input("Priority (high/medium/low):")
    time_bound = input("Is it time-bound? (yes/no):")

    # Normalize input
    priority = priority.strip().lower()
    time_bound = time_bound.strip().lower()

    # Loop until valid priority is given
    while priority not in {"high", "medium", "low"}:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low):").strip().lower()

    # Loop until valid time_bound is given
    while time_bound not in {"yes", "no"}:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-bound? (yes/no):").strip().lower()

    # Use match-case for priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

    # Add urgency if time-bound and not low
    if time_bound == "yes" and priority in {"high", "medium"}:
        reminder += " that requires immediate attention today!"

    print(reminder)

if __name__ == "__main__":
    main()
