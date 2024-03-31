from person import Person # Importing necessary classes from their respective modules.
from visitor import Visitor, VisitorType
from employee import Employee
from ticket import Ticket
from event import Event, EventType
from exhibition import Exhibition
from artwork import Artwork
from location import Location, LocationType
from datetime import date,timedelta
import random


# Main function that starts the interactive system.
def main():
    print("Welcome to the Museum Interactive System")
    # let  user to pick whether to identify as a visitor or an employee.
    user_type = input("Are you a visitor or an employee? (1) visitor / (2) employee): ").lower()
    # Handling user input
    if user_type in ["visitor", "1"]:
        handle_visitor_scenario()
    elif user_type in ["employee", "2"]:
        handle_employee_scenario()
    else:
        print("Invalid option selected. Exiting.")

# Function to handle the visitor scenario.
def handle_visitor_scenario():
    try:  # Collect visitor information.
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        national_id = input("Please enter your national ID: ")
        email_id = input("Please enter your email ID: ")
        # Instantiate a Visitor object.
        visitor = Visitor(name, age, national_id, email_id, VisitorType.ADULT)
        # Ask if the visitor wants to purchase a ticket.
        purchase_ticket = input("Do you want to purchase a ticket? (yes/no): ").lower()
        if purchase_ticket == "yes": # Determine how many tickets the visitor wants to purchase.
            num_tickets = int(input("How many tickets do you want to purchase? "))
            # Present the available events to the visitor.
            print("Please select the event:")
            for event_type in EventType:
                print(f"{event_type.name[0]}: {event_type.value}")
            event_letter = input().upper()
            # Retrieve the selected event type based on user input from event class enum
            event = {'A': EventType.ART_EXHIBITION, 'M': EventType.MUSIC_FESTIVAL, 'S': EventType.SCIENCE_CONFERENCE,
                     'F': EventType.FOOD_FAIR}.get(event_letter)

            if event is None:
                raise ValueError("Invalid event selected.")
            # Iterate over the number of tickets to set details for each.
            total_price = 0
            for i in range(num_tickets):
                print(f"Ticket {i + 1}: Please select the type of visitor:")
                for visitor_type in VisitorType:
                    print(f"{visitor_type.value[0]}: {visitor_type.value[1]}")
                type_of_visitor_input = int(input())
                if type_of_visitor_input not in range(1, 6): # Validate and assign the visitor type.
                    raise ValueError("Invalid visitor type selected.")
                type_of_visitor = \
                {1: VisitorType.ADULT, 2: VisitorType.CHILD, 3: VisitorType.SENIOR, 4: VisitorType.TEACHER_STUDENT,
                 5: VisitorType.GROUP}[type_of_visitor_input]
                # Randomly assign a location to the ticket.
                location = Location(
                    random.choice(list(LocationType)))  # Assuming location is selected randomly
                # Randomly determine the duration for the ticket.
                duration = random.randint(1, 5)  # Assuming duration is selected randomly

                # Instantiate a Ticket object.
                ticket = Ticket(type_of_visitor, event, location.get_name(), duration)
                # Assign the ticket to the visitor.
                visitor.assign_ticket(ticket)
                # Calculate the total price for all tickets from ticket class function
                total_price += ticket.get_price()

                event_object = Event(event)
                start_date = event_object.get_start_date()
                end_date = event_object.get_end_date()

            # Display the total price and details of the event.
            print(f"The total price for {num_tickets} tickets is {total_price} AED.")
            print(f"The event {event.value} will be held at {location.get_name()} from {event_object.start_date} to {event_object.end_date} for {duration} hours.")
            # Ticket Purchase Summary
            print("--- Ticket Purchase Summary ---")
            print(f"Name: {name}")
            print(f"Email: {email_id}")
            print(f"Number of Tickets: {num_tickets}")
            print(f"Event: {event.value}")
            print(f"Location: {location.get_name()}")
            print(f"Total Price: {total_price} AED")
        else:
            print("Thank you for visiting!")
    except ValueError as ve:
        print(f"Error: {ve}") # Handle any value errors that arise from invalid input.
    except KeyError:
        print("Invalid option selected. Exiting.") # Handle any key errors from invalid dictionary lookups.



added_artworks = []  # Initialize an empty list to store added artworks
# Function to add an artwork to an exhibition.
def add_artwork_to_exhibition():
    try:
        global added_artworks  # Access the global list of added artworks
# let user select the type of event.
        print("Please select the event type:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None
        # Determine the event type based on user input.
        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return
        # Get artwork details from the user.
        title = input("Please enter the artwork title: ")
        artist = input("Please enter the artist: ")
        year_of_creation = input("Please enter the year of creation: ")

        # Randomly select a location type for the artwork.
        location_type = random.choice(list(LocationType))
        location = Location(location_type)

        historical_significance = input("Please enter the historical significance: ")

        # Instantiate an Artwork object.
        artwork = Artwork(title, artist, year_of_creation, location, historical_significance)

        exhibition = Exhibition(event, location, date.today(), date.today())
        exhibition.add_artwork(artwork)
        added_artworks.append(artwork)  # Add the artwork to the list of added artworks
        print(f"Artwork {title} by {artist} created in {year_of_creation} added to {event.value} exhibition.")

    except Exception as e:
        print(f"An error occurred: {e}") # Handle any general errors that occur.



# Function to remove an artwork from an exhibition.
def remove_artwork_from_exhibition():
    try:
        global added_artworks  # Access the global list of added artworks

        print("Please select the event:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None
        # Determine the event based on user input.
        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return

        # Get the title of the artwork to be removed.
        title = input("Please enter the artwork title: ")

        # Randomly select a location type.
        location_type = random.choice(list(LocationType))
        location = Location(location_type)

        # Create an Exhibition object for the removal operation.
        exhibition = Exhibition(event, location, date.today(), date.today())

        # Find and remove the artwork by title from the list of added artworks
        removed = False
        for artwork in added_artworks:
            if artwork.title == title:
                exhibition.remove_artwork(artwork)
                added_artworks.remove(artwork)
                removed = True
                break

        if removed:
            print(f"Artwork {title} removed from {event.value} exhibition.")
        else:
            print(f"No such artwork with title '{title}' found in the {event.value} exhibition.")

    except Exception as e:
        print(f"An error occurred: {e}") # Handle any general errors.




# Function to create a new exhibition.
def create_new_exhibition():
    try:
        # Prompt the user to select the type of event for the new exhibition.
        print("Please select the event type:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None

        # Determine the event type based on the user's choice.
        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return

        # Randomly select a location type for the new exhibition.
        location_type = random.choice(list(LocationType))
        location = Location(location_type)
        # Set the start and end dates for the exhibition.
        start_date = date.today()
        end_date = date.today() + timedelta(days=30)

        # Instantiate the Exhibition object with the event type, location, and dates.
        exhibition = Exhibition(event, location, start_date, end_date)
        print(f"New {event.value} exhibition opened at {location.get_name()} from {start_date} to {end_date}.")

    except Exception as e:
        print(f"An error occurred: {e}") # Handle any general errors.


# Function to display all added artworks.
def display_added_artworks():
    if added_artworks:  # Check if there are any artworks added
        print("List of added artworks:")
        for artwork in added_artworks: #if there is art by using for loop it prints them
            print(f"Title: {artwork.title}, Artist: {artwork.artist}, Year: {artwork.year_of_creation}, Historical Significance: {artwork.historical_significance}")
    else: #no artwork it prints this
        print("No artworks have been added yet.")



# Function to handle the employee scenario.
def handle_employee_scenario():
    try:  # Collect employee information.
        employee_id = input("Please enter your Employee ID: ")
        employee_name = input("Please enter your name: ")
        # Set a flag to continue the working session.
        continue_working = True
        # Loop for the employee interaction with the system.
        while continue_working:
            print(f"\nEmployee ID: {employee_id}, Employee Name: {employee_name}")
            print("What would you like to do?")
            # Display options for the employee to choose from.
            print("(1) Add artwork to an exhibition")
            print("(2) Remove artwork from an exhibition")
            print("(3) Open a new exhibition or event at the museum")
            print("(4) Display added artworks")
            action = input()

            # Handle the chosen action.
            if action == "1":
                add_artwork_to_exhibition()
            elif action == "2":
                remove_artwork_from_exhibition()
            elif action == "3":
                create_new_exhibition()
            elif action == "4":
                display_added_artworks()  # Display artworks that have been added.
            else:
                print("Invalid option selected. Exiting.")
                break  # Exit the loop if the option is invalid.

            # Ask the employee if they want to continue
            continue_choice = input("Do you want to continue? (yes/no): ").lower()
            continue_working = continue_choice == "yes"

        print("Thank you for your work today!") # Thank the employee after the session is over.

    except Exception as e:
        print(f"An error occurred: {e}") # Handle any general errors.


# Check if this script is the main program and execute it.
if __name__ == "__main__":
    main()