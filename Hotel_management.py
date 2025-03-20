

class hotelmanagement:
    def __init__(self):
        self.rooms=["Available"]*10
        self.count_rooms=10
        self.booked_rooms={}


    def rooms_availabilty(self):
        # Total_Available_rooms=[]
        # for i in self.rooms:
        #     if i == "Available":
        #         Total_Available_rooms.append(i)
           
        #     print(Total_Available_rooms)
        
        # if "Available" not  in  Total_Available_rooms:
        #     print("Rooms is not available")
        
        # else:
        print(f"Rooms Availability  {self.rooms}")
            


    def book_the_room(self):
    
        name=input("Enter your name: ")
        phone_number=int(input("Enter your mobile number: "))
        Select_room=int(input(f"Select_room rooms from 1 to  {len(self.rooms)}: " ))
        
        if Select_room !='' and  self.rooms[Select_room]=="Available":
            self.rooms[Select_room]="Booked"
            self.count_rooms-=1
            print(f"\nRoom is booked with Room no: {Select_room +100} is confirmed \n" )
            
            self.booked_rooms[Select_room + 100]="Booked"
            print(f"Hello {name} your room is successfully booked , THANK YOU .")
        elif self.rooms[Select_room]!="Available":
            print("\nSELECTED ROOM IS  ALREADY BOOKED! PLEASE Select_room ANOTHER ROOM ")

        elif Select_room=='':
            for i in range(len(self.rooms)):
                if self.rooms[i]=="Available":
                    self.rooms[i]="booked"
                    self.count_rooms -=1
                
                    print(f"\nRooms is booked with room number {i+100} is confirmed \n" )
                    print(f"Hello {name} your room is successfully booked , THANK YOU .")

                    break
                elif "Available" not in self.rooms:
                    print("Rooms are sold out please visit again after 24hr")

        

    
    def Rooms_availability_check(self):

        print(f"Available rooms counts is {self.count_rooms}")

    
    def check_booked_rooms(self):
        print(f"Booked rooms are {self.booked_rooms}")


    def payment(self,hours):
        room_no = int(input("enter room number starts from 100 to 110:"))
        check_out_room=False
        change_status_for_rooms= room_no -100
        if room_no in self.booked_rooms:
            self.rooms[change_status_for_rooms]="Available"
            self.booked_rooms[room_no]="Available"

            check_out_room=True
        
        if check_out_room and hours>=12:
            pay=hours * 100
            print(f"Your payment is generated Rs.Total: {pay}")

            


            



    

        


            
    



