import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id':str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        '''book a hotel by changing it availability to no'''
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)
    
    def available(self):
        '''Checks if hotel is available'''
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name , hotel_object):
        pass

    def generate(self):
        content = f"Name of the customer hotel: "
        return content


print(df)
hotel_ID = input('enter id of hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("enter name: ")
    reservation = ReservationTicket(name, hotel)
    print(reservation.generate())
else:
    print("hotel not available")