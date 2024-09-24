#set amount due
amount_due = 50
#create conditional case
while amount_due >= 0:
    #prompt user for initial amount due and show initial amount
    print("Amount Due:", amount_due)
    inserted = int(input("Insert Coin:"))
    #check denomination 25, 10 or 5
    if inserted == 25 or inserted == 10 or inserted == 5:
        #deduct amount inserted from initial amount
        amount_due = amount_due - inserted
        #show change owed
        if amount_due <= 0:
            print("Change Owed:", (amount_due*-1))
            break
