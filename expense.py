expenses = []

for i in range(5) :
    expense = float(input("Enter expense " + str(i+1) + " "))
    expenses.append(expense)

print(sum(expenses)) 
