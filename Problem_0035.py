# Write a Python program to check if a string is a palindrome, ignoring spaces and punctuation.

def is_palindrome(text):
  
   
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
  
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")
