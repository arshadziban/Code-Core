# Write a Python program to count the frequency of each character in a string and display them in descending order.

def character_frequency(text):
  
    freq = {}
    for char in text.lower():
        if char.isalnum():
            freq[char] = freq.get(char, 0) + 1
    
    # Sort by frequency in descending order
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


# Test cases
if __name__ == "__main__":
    text = input("Enter a string: ")
    
    result = character_frequency(text)
    
    if result:
        print("Character frequencies (descending):")
        for char, count in result.items():
            print(f"  '{char}': {count}")
    else:
        print("No alphanumeric characters found.")
