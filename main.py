import pandas as pd

df = pd.read_csv('hotels.csv')

class Hotel:
    def __init__(self, id) -> None:
        pass

    def book(self):
        pass
    
    def available(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name , hotel_object):
        pass

    def generate(self):
        content = f"Name of the customer hotel: "
        return content


print(df)
id = input('enter id of hotel: ')
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("enter name: ")
    reservation = ReservationTicket(name, hotel)
    print(reservation.generate())
else:
    print("hotel not available")