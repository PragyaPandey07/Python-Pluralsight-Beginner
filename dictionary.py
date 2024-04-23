# Dictionary is a key-value pair of data type
acronyms = {
    'LOL': 'laugh out loud',
    'IDK': "I don't know",
    'TBH': 'to be honest'
}

acronyms['ASAP'] = "as soon as possible" #adding values to the dictionary

print(acronyms)

print(acronyms['LOL']) #reading from the dictionary 

del acronyms['LOL'] #deletes the key-value pair from teh dictionary
print(acronyms)

# acronyms['BTW'] 
#reading a value which is not available throws an error
# use .get method instead 
print(acronyms.get('BTW')) #this returns None instead of crashing the program which shows the absence of a value 
