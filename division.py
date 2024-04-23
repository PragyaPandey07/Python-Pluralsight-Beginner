def division(a,b):
    if b == 0 :
        raise ZeroDivisionError #Directly raise the exception
            #or
        raise Exception('Divisor cannot be 0') #Raise exception with custom message
    
    quotient = a//b
    remainder = a%b
    print(a,'/',b,'=', quotient, 'with remainder', remainder)

division(10,0) 