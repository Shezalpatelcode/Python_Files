
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]

# print("Orginal list of strings:")
# print(texts)  


# result = list(filter(lambda x: (x == "".join(reversed(x))), texts))

# # Display the list of palindromes obtained from the original list of strings
# print("\nList of palindromes:")
# print(result)  # Print the filtered 'result' list 
#----------------------------------------------------------------------------
#          Q)Palindrome of a number using the lambda function 

# Palindrome check using lambda function


# Example usage
string = input("Enter a string or number: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")
