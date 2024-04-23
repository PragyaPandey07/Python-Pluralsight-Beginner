numbers = [1,2,3,4,5,6,7,8,9,10] #list is like array
print(numbers)
mid = int(len(numbers)/2) #len(listName) is the method used to find length of the list
print(mid)
if mid in numbers : # to find the element in the list
    numbers.remove(mid) #.remove method is used to remove a list item
else :
    numbers.append(mid) #.append method is used to add a list item

for number in numbers : # for loop
    print(number)

total = sum(numbers) #sum(listName) is inbuilt function to calculate the sum of a list
print(total) 