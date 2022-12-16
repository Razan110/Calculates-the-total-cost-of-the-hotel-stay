
"""Calculates the total cost of the hotel stay"""

def hotel_cost (): 

    print('*** \n \nWelcome to our hotel please fill the room type and the lenth of your stay. ')
    print('\n The room type is:\n Stander room that cost 150$ per night. \n Deluxe room that cost 180$ per night.')
    print('\n Suit room that cost 220$ per night.\n\n***\n ')
    roomType = input('Enter The Room Type: \n')
    
    if roomType.lower() == 'stander':
        cost = 150    
    if roomType.lower() == 'deluxe':
        cost =  180  
    if roomType.lower() == 'suit':
        cost =  220  
        
    print('\n*** The',roomType,'cost is',cost,'$ per night *** \n')
    
    totalStayDaysAtTheHotel = input('Enter number of nights: \n')
    totalStayDaysAtTheHotel=int(totalStayDaysAtTheHotel)
    totalCost = cost * totalStayDaysAtTheHotel
    
    return totalCost



"""Calculates the total cost of the rental car"""

def rental_car_cost (): 

    answer=input ('\nDo you want to rent a car? Yes or No. \n')

    if answer.lower()=='yes':
        print('\n*** Rental car charge 100$ for one day (+60$ for each additional day) ***\n')

        rentalCarDays = input ('\nHow many days do you want to rent car?: \n')
        rentalCarDays=int(rentalCarDays)
        totalDailyCost = 100
        day=1
        for day in range(1,rentalCarDays):
                totalDailyCost=totalDailyCost+60
    else:
        totalDailyCost=0
        print('\nOk! answer the next qustions.\n')
    return totalDailyCost




"""Calculates the total cost of the parking """

def parking_cost (): 

    parkingCostAnswer=input ('Do you want to park your car in the theme park? Yes or No. \n')

    if parkingCostAnswer.lower()=='yes':
        print('\n*** Parking charge 175$ for one day (+50$ for each additional day) ***\n')

        parkingCost = input ('\nHow many days are you going to park your car in the parking?: \n')
        parkingCost=int(parkingCost)
        totalParkingCost = 175

        for i in range(1,parkingCost):
                totalParkingCost=totalParkingCost+50
    else:
        totalParkingCost=0
        print('\nOk!\n')
    return totalParkingCost



"""Calculates the total cost of the trip """
def trip_cost():
    
    Hotel=hotel_cost()
    print('\n*** The Hotel total cost is',Hotel,'$ ***')
    Car=rental_car_cost()
    print('\n*** The total cost of the rental car is',Car,'$ ***\n')
    Parking=parking_cost()
    print('\n*** The total parking cost is ',Parking,'***')
    total=Hotel+Car+Parking
    print('\n*** The total cost of the trip is:',total,'$, Thank you and injoy your stay :) ***')
    return

trip_cost()

