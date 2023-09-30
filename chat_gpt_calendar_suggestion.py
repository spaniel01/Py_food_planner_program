import datetime

# Calendar dictionary to store events
calendar = {}

def display_events(date):
    if date in calendar:
        events = calendar[date]
        print(f"Events on {date}:")
        for i, event in enumerate(events, 1):
            print(f"{i}. {event}")
    else:
        print(f"No events found on {date}")

def add_event(date, event):
    if date not in calendar:
        calendar[date] = []
    calendar[date].append(event)
    print(f"Event added to {date}: {event}")

def edit_event(date, event_index, new_event):
    if date in calendar and 0 < event_index <= len(calendar[date]):
        calendar[date][event_index - 1] = new_event
        print(f"Event updated on {date}: {new_event}")
    else:
        print(f"Event not found on {date} at index {event_index}")

def delete_event(date, event_index):
    if date in calendar and 0 < event_index <= len(calendar[date]):
        deleted_event = calendar[date].pop(event_index - 1)
        print(f"Event deleted from {date}: {deleted_event}")
    else:
        print(f"Event not found on {date} at index {event_index}")

def food_planner(food_calendar, recipes):
    while True:
        choice = user_input_validation_int("\nFood planner menu:\n1. View most recent food plan\n2. Create new food plan\n3. Edit previous food plan\n4. Delete food plan\n5. Return to main menu", 5)
        if choice == 1:
            date = input("Enter date (YYYY-MM-DD): ")
            display_events(date)
        elif choice == 2:
            date = input("Enter date (YYYY-MM-DD): ")
            event = input("Enter event description: ")
            add_event(date, event)
        elif choice == 3:
            date = input("Enter date (YYYY-MM-DD): ")
            event_index = int(input("Enter the index of the event to edit: "))
            new_event = input("Enter new event description: ")
            edit_event(date, event_index, new_event)
        elif choice == 4:
            date = input("Enter date (YYYY-MM-DD): ")
            event_index = int(input("Enter the index of the event to delete: "))
            delete_event(date, event_index)
        elif choice == 5:
            return food_calendar
        else:
            print("Invalid choice. Please choose a valid option.")