import random
import time

#BOOKING FUNC
def destination():
    print('\t \t PLEASE SELECT DESTINATION')
    print()
    print("\t \t 1. SHIMLA\n")
    print("\t \t 2. MANALI\n")
    print('\t \t 3. OOTY\n')
    print('\t \t 4. DARJEELING\n')
    print("\t \t 5. JAIPUR\n")
    ch_dest=int(input("--->>"))

def package():
    print("_"*107)
    print('\t \t PLEASE SELECT DESIRED PACKAGE')
    print("_"*107)
    print()
    print("\t \t Please note the following packages\n"
          "\t \t are in accordance to per person per night")
    time.sleep(2)
    print()
    print('\t \t 1. Rs3,500 per person, 3 activites,CP')
    print("\t \t  It includes breakfast along with room")
    time.sleep(2)
    print()
    print("\t \t 2. Rs5,000 per person, 3 activities, MAP")
    print("\t \t  Room with Breakfast and One Major Meal")
    time.sleep(2)
    print()
    print("\t \t 3. Rs6,000 per person, 5 activites, MAP")
    print("\t \t  Room with Breakfast and One Major Meal")
    time.sleep(2)
    print()
    print('\t \t 4. Rs7,000 per person, 8 activities, EP')
    print ("\t \t It is room only,with no meals")
    time.sleep(2)
    print()
    ch_pack=int(input("--->>"))
    global pack_cost
    if ch_pack==1:
        pack_cost= 3500
    elif ch_pack==2:
        pack_cost= 5000
    elif ch_pack==3:
        pack_cost=6000
    elif ch_pack==4:
        pack_cost=7000
    global nights
    nights=int(input('ENTER NO. OF NIGHTS YOU WANT TO STAY:'))

def passengers():
    global num
    num=int(input("ENTER NO. OF PASSENGERS:"))
    i=1
    while i<=num:
        name=input("ENTER NAME OF PASSENGER:")
        age=int(input("ENTER AGE OF PASSENGER:"))
        gender=input('ENTER GENDER OF PASSENGER:')
        DOB=input("ENTER DOB OF PASSENGER(DD-MM-YYYY):"))
        i+=1
        
def route():
    print("\t \t START JOURNEY FROM:")
    print("\t \t 1. DELHI")
    print("\t \t 2. BENGALURU")
    print("\t \t 3. MUMBAI")
    print("\t \t 4. HYDERABAD")
    print("\t \t 5. CHENNAI")
    ch_route=int(input("--->>"))
    global route_cost
    if ch_route==1:
        route_cost=1000
    elif ch_route==2:
        route_cost=1500
    elif ch_route==3:
        route_cost=2000
    elif ch_route==4:
        route_cost=1200
    elif ch_route==5:
        route_cost=1300

def invoice():
    print("\t     PAYMENT       ")
    print("-----------------------")
    print("     MODE OF PAYMENT   ")
    print("  1- Credit/Debit Card")
    print("  2- Paytm/PhonePe")
    print("  3- Using UPI")
    print("  4- Cash")
    pay=int(input("--->>"))
    print("PROCEED(Y/N)")
    dec=input("--->>")
    if dec in "Yy":
        name=input("ENTER NAME OF PAYEE:")
        nom=input("ENTER PHONE NO.:")
        print("-----------------------")
        print("     EASE MY TRIP      ")
        print('-----------------------')
        print("          BILL         ")
        print('NAME:',name, "\t\n Phone number:",nom)
        print("HOTEL AMOUNT= Rs",pack_cost*num*nights)
        print("TRANSPORT AMOUNT= Rs",route_cost)
        print("TOTAL AMOUNT= Rs",pack_cost*num*nights+route_cost)
        print("-----------------------")
        print("-----------------------")
        print("      THANK YOU :)      ")
        print("------------------------")
        print("BOOKING DONE SUCCESSFULLY")
        print("HAPPY JOURNEY!")



#MAIN MENU
import time
print("_"*107)
a="EASE MY TRIP"
b=a.center(107)
print(b)
print("_"*107)
print()
time.sleep(1)
print("_"*107)
c="Welcome to Ease My Trip!"
d=c.center(107)
print(d)
print()
time.sleep(1)
e="Where the journey begins"
f=e.center(107)
print(f)
print("_"*107)
print()

while True:
    print("\t \t 1. HOTEL BOOKING\n")
    time.sleep(1)
    print("\t \t 2. BOOK FLIGHT TICKECTS\n")
    time.sleep(1)
    print('\t \t 3. BOOK TRAIN TICKETS\n')
    time.sleep(1)
    print("\t \t 4. INVOICE\n")
    time.sleep(1)
    print("\t \t 5. EXIT\n")
    

    ch=int(input("ENTER CHOICE-->"))
    if ch==1:
        destination()
        package()
        passengers()
        time.sleep(2)
        print("Please Wait.....")
        time.sleep(1)
        print("Loading....")
        time.sleep(2)
        print("_"*107)
        hb= "HOTEL BOOKED"
        hc=hb.center(107)
        print(hc)
        print("_"*107)
        print()
    elif ch==2:
        route()
        passengers()    
    elif ch==3:
        route()
        passengers() 
    elif ch==4:
        invoice()
    elif ch==5:
        print('EXITING')
    else:
        print('PLEASE ENTER VALID OPTION')



              
