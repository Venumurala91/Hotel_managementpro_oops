
from utility import *
from Hotel_management import hotelmanagement

class Hotelmanager:
    def __init__(self):
        self.hotel=hotelmanagement()
   
        
    def print_menu(self):

        Msg=f"======>    Hello Welcome to Taj hotel  <======= "
        options_to_choose=[
                           '1.Rooms_availability',
                           '2.book_the_room',
                           '3.Avail_rooms_count',
                           '4.Booked_rooms',
                           '5.select_billing']

        message="Choose_options_from_above_Menu from 1 to 10:"

        print("\n",Msg,"\n")
        
        print("\n".join(options_to_choose))
        
        return input_validity_check(message,end=len(options_to_choose))

    

    def run(self):
        choose= self.print_menu()

        if choose ==1:
            self.hotel.rooms_availabilty()
        
        elif choose ==2:
            self.hotel.book_the_room()

        elif choose==3:
            
            self.hotel.Rooms_availability_check()

        
        elif choose==4:
            self.hotel.check_booked_rooms()
        
        elif choose==5:
            hours=int(input("Enter the hours u had stayed :"))
            self.hotel.payment(hours)
            
        
        print("\n")
        app.run()




if __name__== "__main__":
    app= Hotelmanager()
    app.run()
