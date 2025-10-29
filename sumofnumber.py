# Python 3 program to find  
# factorial of given number 
def sum(n): 
    
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
        return (n + sum(n - 1)) 

# Driver Code 
num = 5; 
print("number : ",num)
print("Factorial : ",sum(num))