print('============================Task 1====================================================================')

a = ["Question", "Answer", "Blue", "Red", "Green", "White"]
b = ["Vopros", "Otvet", "Sinii", "Krasni"]

for index in range(len(a)):
        word = a[index]
        if index < len(b):
            print("{}-{}".format(word, b[index]))
        else:
            print("{}-{}".format(word, None))


print('============================Task 2====================================================================')

str1 = input("Please enter the word: ")
str2 = ''
for i in reversed(str1):
    str2 += i
#    print(str2)
if str1 == str2:
    print("Everything is OK. The word is palindrom.")
else:
    print("Something is wrong.")


print('============================Task 3====================================================================')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("List with all non-repeating numbers")
print(list(set(a+b)))
print("List with all numbers in both lists (a,b)")
d = []
for index in range(len(a)):
    if (a[index] in b) & (a[index] not in d):
      d += [a[index]]
print(d)


print('============================Task 4====================================================================')

import re
from collections import Counter

with open('access.log') as log:
    list = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
    log.read())
    log.close()
    for ip in Counter(list).most_common(10):
        print(ip[0])
