from atendee import *
from conference import *

if __name__ == '__main__':

    print("Welcome to the conference interface!")

    conference_name = None
    while conference_name is None:
        conference_name = input("Which conference are you attending?: ")

    new_conference = Conference(conference_name + ".txt")

    statement = "What do you want to do?\n" \
                "Add new attendee [add]: \n"\
                "Delete an attendee [delete]: \n"\
                "Show attendees in a given state [state]: \n"\
                "Display general attendee info [general]: \n"\
                "Display attendee contacts [contacts]: \n"\
                "End program [end]: \n"

    control = input(statement)

    while control.lower() != "end":
        if control.lower() == "add":
            while input("add new attendee? [y/n]: ").lower() != "n":
                name = input("name: ")
                email = input("email: ")
                company = input("company: ")
                state = input("state: ")
                attendee = Attendee(name, company, state, email)
                new_conference.add_attendee(attendee)
                print("Attendee has been added")

        elif control.lower() == "delete":
            while input("delete? [y/n]: ").lower() != "n":
                name = input("name of attendee to be deleted: ")
                new_conference.delete_attendee(name)
                print(name + " " + "has been deleted")

        elif control.lower() == "state":
            while input("Indicate state for data retrieval? [y/n]? ").lower() != "n":
                state = input("state: ")
                new_conference.attendee_location(state)

        elif control.lower() == "general":
            while input("Display attendee info? [y/n]? ").lower() != "n":
                name = input("name: ")
                new_conference.display_attendee(name)

        elif control.lower() == "contacts":
            while input("Display attendee contact? [y/n]? ").lower() != "n":
                new_conference.attendee_contact()

        control = input(statement)

