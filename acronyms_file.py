search = input('Enter acronym you want to look up \n')

found = False
with open('Ahold_Acronyms.txt') as file :
    for line in file :
        if search in line :
            print(line)
            found = True
            break
    
    if not found :
        print("Not found !!") 