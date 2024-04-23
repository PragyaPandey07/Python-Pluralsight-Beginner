acronyms = {
    'LOL': 'Laugh Out Loud',
    'BTW': 'By The Way',
    'EOD': 'End Of Day',
    'ASAP': 'As Soon As Possible'
}

search_word = input('Enter the acronym you wanna look up ')

try :       #contains the code which might throw an errror is not successful
    definition = acronyms[search_word]
    print('Acronym', search_word, 'stands for', definition)
except :    #contains code which needs to be executed in case of errors. this block runs only when there is an error
    print("The acronym', search_word, 'doesn't exist !!")
finally:    #contains code which always runs irresprctive of whether try succeeds or fails 
    print("Acronyms in the list are: ")
    for acronym in acronyms :
        print(acronym, ':', acronyms[acronym])


print("The program keeps going...") 
