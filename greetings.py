name = input('Please enter your name\n')
print('Hello' + " " + name) 

#greetings using function in python
def greeting(person_name, word='Hey') :
    print(word, person_name, 'from greeting function !!')

greeting(name, 'Hello') 