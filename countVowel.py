def countVowels(str):
    count = 0
    for char in str:
        if char in 'aeiouAEIOU':
            count += 1
    return count


userStr = input("Enter a string: ")
vowelCount = countVowels(userStr)
print("Number of vowels in the string:", vowelCount)