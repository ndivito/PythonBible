films = {
    'Finding Dory': [3,5],
    'Bourne': [18,5],
    'Tarzan': [15,5],
    'Ghost Busters': [12,5],
    'B': [12,2]
}

while True:
    print(films.keys())
    choice = input('Which movie do you want to watch?: ').strip().title()

    if choice in films:
        age = int(input('How old are you?: ').strip())



        if age >= films[choice][0]: #check user age
            # check enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print('Enjoy the film!')
                films[choice][1] = films[choice][1] - 1
            else:
                print('sorry, we are out of seats')


        else:
            print('You are too young!')

    else:
        print('We dont have that film...')