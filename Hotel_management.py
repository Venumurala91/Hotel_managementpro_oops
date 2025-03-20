

class hotelmanagement:
    def __init__(self):
        self.rooms=["Available"]*10
        self.count_rooms=10
        self.booked_rooms=[]


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
        choose=input(f"choose rooms from 1 to  {len(self.rooms)}: " )
        
        if choose !='' and  self.rooms[int(choose)]=="Available":
            self.rooms[int(choose)]="Booked"
            self.count_rooms-=1
            print(f"\nRoom is booked with Room no: {int(choose) +100} is confirmed \n" )

            print(f"Hello {name} your room is successfully booked , THANK YOU .")
        elif self.rooms[int(choose)]!="Available":
            print("\nSELECTED ROOM IS  ALREADY BOOKED! PLEASE CHOOSE ANOTHER ROOM ")

        elif choose=='':
            for i in range(len(self.rooms)):
                if self.rooms[i]=="Available":
                    self.rooms[i]="booked"
                    self.count_rooms -=1
                
                    print(f"\nRooms is booked with room number {i+100} is confirmed \n" )
                    print(f"Hello {name} your room is successfully booked , THANK YOU .")

                    break
                elif "Available" not in self.rooms:
                    print("Rooms are sold out please visit again after 24hr")

        
        self.booked_rooms.append(name)

    
    def Rooms_availability_check(self):

        print(f"Available rooms counts is {self.count_rooms}")

    
    def check_booked_rooms(self):
        print(f"Booked rooms are {self.booked_rooms}")

    

        


            
    



