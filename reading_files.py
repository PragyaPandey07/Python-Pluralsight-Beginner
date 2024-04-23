#open the file. If using this syntax, close the file after completing all operations using file.close(). Give absolute or relative path of the file to be opened
file = open("/Users/prapande12/Desktop/test.html") 
# or 
#open the file with 'with' syntax. This closes the file on it's own after all the operations are complete. Give absolute or relative path of the file to be opened
with open("/Users/prapande12/Desktop/test.html") as file :  
    
    result1 = file.readline()   #readline reads the curent line
    result2 = file.readline()
    result3 = file.readlines()  #reads all the line from current position and returns a list of all the lines
    result4 = file.read()   #reads the entire file at once from current position
    print(result1)
    print(result2)
    print(result3)
    print(result4) 