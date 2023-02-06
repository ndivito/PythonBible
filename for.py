



for x in range(1,11,2):
    print(x)

for letter in "buccki":
    print(letter)


vowels = 0
consonants = 0
word = "Hello you son of a gun"
print(word)
for letter in word:
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter.lower() in "qwrtypsdfghjklzxcvbnm":
        consonants += 1
    else:
        pass

print('the number of vowels is {}'.format(vowels))
print('the number of consonants is {}'.format(consonants))

students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print('the name {} has an "a" in it'.format(name))
