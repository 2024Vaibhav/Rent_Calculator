# inputs we need from the user
# # total rent
# Total food ordered for snacking
# Electricity units spends
# charge per unit
# Output
# Number of person living in room/flat
# Total amount you have to pay is 

rent = int(input("Enter your hostel/flat rent="))
food = int(input("Enter the amount of food ordered="))
electricity_spend = int(input("Enter the total of elecricity spend =")) 
charge_per_unit = int(input("Enter the electricity charge per unit ="))
no_of_person = int(input("Enter the  number of person living together = "))
total_bill = electricity_spend*charge_per_unit
output = (rent+food+total_bill)//no_of_person
print("Each person will pay =",output)