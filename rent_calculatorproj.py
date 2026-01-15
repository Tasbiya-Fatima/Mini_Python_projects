rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of foof ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit =  "))
persons = int(input("Enter the number of persons = "))

total_bill = electricity_spend * charge_per_unit

output = int( (food + rent + total_bill)/persons)
print("Each person will pay = ",output)