def romanToInt(s: str) -> int:
   
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    length = len(s)
    
    for i in range(length):
        value = roman_map[s[i]]
        
        if i + 1 < length and roman_map[s[i + 1]] > value:
            total -= value 
        else:
            total += value  
    
    return total

# Example usage:
print(romanToInt("III"))
print(romanToInt("LVIII"))    
print(romanToInt("MCMXCIV"))  




