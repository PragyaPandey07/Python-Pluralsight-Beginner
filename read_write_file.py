def add_acronym() :
    acronym = input("Enter acronym ")
    definition = input("Enter definition ")

    with open('acronym_list.txt', 'a') as file :
        file.write(acronym + ' - ' + definition + "\n")

def find_acronym() :
    acronym = input("Enter acronym to find ")

    try:
        found = False
        with open('acronym_list.txt') as file :
            for line in file :
                if acronym in line :
                    print(line)
                    found = True
                    break
            
            if not found :
                print("Acronym not found !!") 
    
    except:
        print("File does not exist !!") 


def main() :
    user_choice = input("Add or Find your acronym. Press \n (F) - To find acronym \n (A) - To add acronym \n")
    if user_choice == 'F' or user_choice == 'f' :
        find_acronym()
    elif user_choice == 'A' or user_choice == 'a' :
        add_acronym()

main()