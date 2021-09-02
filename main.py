#EasyBill 
print("Welcome to the EasyBill!")
print("EasyBill calculates the total of the bill with the tip amount and splits the bill for per person.")

#mainmenu
def mainmenu():
  choice=input("""1.Calculate Bill 
2.Exit
""")

  if choice == "1":
    easybill()

  elif choice == "2":
    print("EasyBill is closing..")
    quit()

  else:
    print("You can only pick 1 or 2. Closing the application.")

def easybill():
  bill = float(input("Total Bill: $"))
  tip = float(input("Tip: "))
  people = int(input("Number of People: "))
  bill_with_tip = tip + bill
  float(bill_with_tip)
  round(bill_with_tip,2)
  print(f"Your updated bill with tip: ${bill_with_tip}")

  result=bill_with_tip / float(people)
  print(f"Each person should pay: ${result:.2f}")
  print("Thank you for using EasyBill.")
  print("Have a good day!")
  
mainmenu()
