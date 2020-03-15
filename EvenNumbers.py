#program to print the even numbers from a given list.

#list
numbers = [12, 21, 5, 45, 7, 9,18,20,44,2,6,] 
  
# iterating each number in list 
for num in numbers: 
      
    # checking condition 
    if num % 2 == 0: 
       print(num, end = " ")
    else:
        print("no even number found on the list")

#end of program