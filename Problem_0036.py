# Write a Python program to find all pairs of numbers in a list that sum to a target value.

def find_pairs(numbers, target):
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted([num, complement]))
            if pair not in pairs:
                pairs.append(pair)
        seen.add(num)
    
    return sorted(pairs)


# Test cases
if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    
    result = find_pairs(numbers, target)
    
    if result:
        print(f"Pairs that sum to {target}:")
        for pair in result:
            print(f"  {pair[0]} + {pair[1]} = {target}")
    else:
        print(f"No pairs found that sum to {target}")
