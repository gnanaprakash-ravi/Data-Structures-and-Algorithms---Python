class Passenger:
    id = 1  # Class variable to give an ID to each new passenger

    def __init__(self, name, age, berth_preference):
        self.name = name
        self.age = age
        self.berth_preference = berth_preference
        self.passenger_id = Passenger.id
        self.alloted = ""  # Alloted type (L, U, M, RAC, WL)
        self.number = -1  # Seat number
        Passenger.id += 1  # Increment passenger ID for the next passenger

    # def __str__(self):
        # return f"Passenger ID: {self.passenger_id}, Name: {self.name}, Age: {self.age}, Berth Preference: {self.berth_preference}, Alloted: {self.alloted}, Seat Number: {self.number}"