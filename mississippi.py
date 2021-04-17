s= input("please enter a string:")
counter = {}
for char in s:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] =1
print(counter)

#after entering Mississippi in input u will get output like {'M': 1, 'i': 4, 's': 4, 'p': 2}
