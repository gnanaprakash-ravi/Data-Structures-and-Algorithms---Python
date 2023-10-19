from Passenger import Passenger
from TicketBooker import TicketBooker

def bookTicket(p):
    booker = TicketBooker()
    if booker.availableWaitingList == 0:
        print("No Tickets Available")
        return

    if (p.berth_preference == "L" and booker.availableLowerBerths > 0) \
            or (p.berth_preference == "M" and booker.availableMiddleBerths > 0) \
            or (p.berth_preference == "U" and booker.availableUpperBerths > 0):
        print("Preferred Berth Available")

        if p.berth_preference == "L":
            print("Lower Berth Given")
            booker.bookTicket(p, booker.lowerBerthsPositions[0], "L")
            booker.lowerBerthsPositions.pop(0)
            booker.availableLowerBerths -= 1

        elif p.berth_preference == "M":
            print("Middle Berth Given")
            booker.bookTicket(p, booker.middleBerthsPositions[0], "M")
            booker.middleBerthsPositions.pop(0)
            booker.availableMiddleBerths -= 1

        elif p.berth_preference == "U":
            print("Upper Berth Given")
            booker.bookTicket(p, booker.upperBerthsPositions[0], "U")
            booker.upperBerthsPositions.pop(0)
            booker.availableUpperBerths -= 1

    elif booker.availableLowerBerths > 0:
        print("Lower Berth Given")
        booker.bookTicket(p, booker.lowerBerthsPositions[0], "L")
        booker.lowerBerthsPositions.pop(0)
        booker.availableLowerBerths -= 1

    elif booker.availableMiddleBerths > 0:
        print("Middle Berth Given")
        booker.bookTicket(p, booker.middleBerthsPositions[0], "M")
        booker.middleBerthsPositions.pop(0)
        booker.availableMiddleBerths -= 1

    elif booker.availableUpperBerths > 0:
        print("Upper Berth Given")
        booker.bookTicket(p, booker.upperBerthsPositions[0], "U")
        booker.upperBerthsPositions.pop(0)
        booker.availableUpperBerths -= 1

    elif booker.availableRacTickets > 0:
        print("RAC available")
        booker.add_to_rac(p, booker.racPositions[0], "RAC")

    elif booker.availableWaitingList > 0:
        print("Added to Waiting List")
        booker.add_to_waiting_list(p, booker.waitingListPositions[0], "WL")

def cancel_ticket(passenger_id):
    booker = TicketBooker()
    if passenger_id not in booker.passengers:
        print("Passenger detail Unknown")
    else:
        booker.cancel_ticket(passenger_id)

def main():
    loop = True

    while loop:
        print(" 1. Book Ticket \n 2. Cancel Ticket \n 3. Available Tickets \n 4. Booked Tickets \n 5. Exit")
        choice = int(input())
        booker = TicketBooker()

        if choice == 1:
            name = input("Enter Passenger name: ")
            age = int(input("Enter age: "))
            berth_preference = input("Enter berth preference (L,M or U): ")
            p = Passenger(name, age, berth_preference)
            bookTicket(p)

        elif choice == 2:
            passenger_id = int(input("Enter passenger Id to cancel: "))
            cancel_ticket(passenger_id)

        elif choice == 3:
            booker.print_available()

        elif choice == 4:
            booker.print_passengers()

        elif choice == 5:
            loop = False

if __name__ == "__main__":
    main()