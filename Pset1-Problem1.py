s = 'azcbobobegghakl'   #won't exist in the final problem solution
vowelsCounter = 0;
for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        vowelsCounter = vowelsCounter+1
print('Number of vowels: ' + str(vowelsCounter))
