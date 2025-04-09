class Vehicle:
    def __init__(self, vt, stock, rp):
        self.vt = vt 
        self.stock = stock 
        self.rp = rp 

    def va(self):
        print(f"There are {self.stock} {self.vt}s available with rent: Rs.{self.rp}/day")



class RentalAgency(Vehicle):
    def __init__(self, agency, vt, stock, rp):
        self.agency = agency 
        Vehicle.__init__(self,vt, stock, rp)

    def RentalPeriod(self):
        a=int(input("Enter rental period in days: "))
        return a


class RentalTransaction(RentalAgency):
    def __init__(self, agency, vt, stock, rp):
        RentalAgency.__init__(self,agency, vt, stock, rp)

    def bill(self, days, number):
        ta=days*self.rp*number
        return ta



cs = 200
cr = 25
bs = 100
br = 50
customers = [] 

print("                       RENTAL SYSTEM                        ")
print("------------------------------------------------------------")

while True:
    print("\nMENU:")
    print("1.Rent a Car")
    print("2.Rent a Bus")
    print("3.Cancel Order")
    print("4.Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        rental = RentalTransaction("ABC", "Car", cs, cr)
        rental.va()
        
        name = input("Enter your name: ")
        nc = int(input("Enter the number of : "))

        if nc <= cs:
            cs =cs-nc  
            days = rental.RentalPeriod()
            tc = rental.bill(days, nc)
            print(f"{name}, your {nc} car are booked with amount Rs {tc}.")
            customers.append((name, "Car", nc, days, tc)) 
        else:
            print("sorry we can't provide the given amount of vehicles")

    elif choice == 2: 
        rental = RentalTransaction("ABC", "Bus", bs, br)
        rental.va()
        
        name = input("Enter your name: ")
        nb = int(input("Enter the number of buses : "))

        if nb <= bs:
            bs =bs - nb  
            days = rental.RentalPeriod()
            tct = rental.bill(days, nb)
            print(f" {name}, your {nb} bus are booked with amount Rs {tct}.")
            customers.append((name, "Bus", nb, days, tct)) 
        else:
            print("sorry we can't provide the given amount of vehicles")

    elif choice == 3:
        name = input("Enter your name: ")
        for customer in customers:
            if customer[0] == name:
                vt = customer[1]
                q = customer[2]
                
                if vt == "Car":
                    cs =cs + q
                else:
                    bs =bs + q
                
                print(f" {name}, your {q} {vt} have been cancelled.")
                customers.remove(customer) 
                break


    elif choice == 4: 
        print(" Exiting ....")
        break

    else:
        print(" Invalid choice")
        
