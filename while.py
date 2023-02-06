number = 1

while number <= 50:
    if number % 7 == 0:
        print(number)
    number += 1

L = []

while len(L) <4 :
    new_name = input('Please add a new name: ').strip().capitalize()
    L.append(new_name)
    print(L)

print('List is full')
print(L)