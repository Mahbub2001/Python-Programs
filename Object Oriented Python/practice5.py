'''
write a class Train which has methods to book a ticket,get status(no of seats)
and get fare information of trains running under Bangladesh Railway

'''
import bisect

class Train:
    
    def __init__(self,train_name,fare,seats,seatsTable):
        self.name = train_name
        self.fare = fare
        self.seats = seats
        self.seatsTable = seatsTable

    def getStatus(self):
        print(f"\t\tThe name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    
    def fareInfo(self):
        print(f"The price of the ticket is TK.{self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            choose = int(input("What seat do you want : "))
            seatsTable.remove(choose)
            print(f"Your ticket has been booked! Your seat number is {choose}")
            self.seats = self.seats - 1# seat booked hle kome jbe ejnno protiber evabe komano hoise
        else:
            print("Sorry the train is full!")

        print(f"Now seats available in the train are {self.seats}")
        print(f"Now available seats are : {self.seatsTable}")

    def cancelTicket(self):
        add_seat = int(input("Enter the seat number that you want to cancel : "))
        bisect.insort(self.seatsTable,add_seat)
        print(f"Now seats are : {self.seatsTable}")

ticket_cost = 90
seats = 10
seatsTable =[1,2,3,4,5,6,7,8,9,10]

intercity = Train("Entercity Express : 14015",ticket_cost,seats,seatsTable)

intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.cancelTicket()


