from collections import deque

class TicketBooker:
    availableLowerBerths = 1
    availableMiddleBerths = 1
    availableUpperBerths = 1
    availableRacTickets = 1
    availableWaitingList = 1

    def __init__(self):
        self.waitingList = deque()
        self.racList = deque()
        self.bookedTicketList = []
        self.lowerBerthsPositions = [1]
        self.middleBerthsPositions = [1]
        self.upperBerthsPositions = [1]
        self.racPositions = [1]
        self.waitingListPositions = [1]
        self.passengers = {}

    def bookTicket(self, passenger, berth_info, alloted_berth):
        passenger.number = berth_info
        passenger.alloted = alloted_berth
        self.passengers[passenger.passenger_id] = passenger
        self.bookedTicketList.append(passenger.passenger_id)
        print("-------------------------- Booked Successfully")

    def add_to_rac(self, passenger, rac_info, alloted_rac):
        passenger.number = rac_info
        passenger.alloted = alloted_rac
        self.passengers[passenger.passenger_id] = passenger
        self.racList.append(passenger.passenger_id)
        TicketBooker.availableRacTickets -= 1
        self.racPositions.pop(0)
        print("-------------------------- Added to RAC Successfully")

    def add_to_waiting_list(self, passenger, waiting_list_info, alloted_wl):
        passenger.number = waiting_list_info
        passenger.alloted = alloted_wl
        self.passengers[passenger.passenger_id] = passenger
        self.waitingList.append(passenger.passenger_id)
        TicketBooker.availableWaitingList -= 1
        self.waitingListPositions.pop(0)
        print("-------------------------- Added to Waiting List Successfully")

    def cancel_ticket(self, passenger_id):
        if passenger_id not in self.passengers:
            print("Passenger detail Unknown")
            return

        passenger = self.passengers[passenger_id]
        self.passengers.pop(passenger_id)
        self.bookedTicketList.remove(passenger_id)
        position_booked = passenger.number
        print("--------------- Cancelled Successfully")

        if passenger.alloted == "L":
            TicketBooker.availableLowerBerths += 1
            self.lowerBerthsPositions.append(position_booked)
        elif passenger.alloted == "M":
            TicketBooker.availableMiddleBerths += 1
            self.middleBerthsPositions.append(position_booked)
        elif passenger.alloted == "U":
            TicketBooker.availableUpperBerths += 1
            self.upperBerthsPositions.append(position_booked)

        if self.racList:
            passenger_from_rac = self.passengers[self.racList.popleft()]
            position_rac = passenger_from_rac.number
            self.racPositions.append(position_rac)
            TicketBooker.availableRacTickets += 1

            if self.waitingList:
                passenger_from_waiting_list = self.passengers[self.waitingList.popleft()]
                position_wl = passenger_from_waiting_list.number
                self.waitingListPositions.append(position_wl)
                passenger_from_waiting_list.number = self.racPositions[0]
                passenger_from_waiting_list.alloted = "RAC"
                self.racPositions.pop(0)
                self.racList.append(passenger_from_waiting_list.passenger_id)
                TicketBooker.availableWaitingList += 1
                TicketBooker.availableRacTickets -= 1
            self.book_ticket(passenger_from_rac)

    def print_available(self):
        print("Available Lower Berths", TicketBooker.availableLowerBerths)
        print("Available Middle Berths", TicketBooker.availableMiddleBerths)
        print("Available Upper Berths", TicketBooker.availableUpperBerths)
        print("Available RACs", TicketBooker.availableRacTickets)
        print("Available Waiting List", TicketBooker.availableWaitingList)
        print("--------------------------")

    def print_passengers(self):
        if not self.passengers:
            print("No details of passengers")
            return

        for passenger in self.passengers.values():
            print("PASSENGER ID", passenger.passenger_id)
            print("Name", passenger.name)
            print("Age", passenger.age)
            print("Status", f"{passenger.number}{passenger.alloted}")
            print("--------------------------")