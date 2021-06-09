import random

while True: 
    random_number_1 = random.randint(1, 99)
    random_number_2 = random.randint(1, 99)
    random_number_3 = random.randint(1, 99)

    with open("fastmathsign.txt") as file:
	    allText = file.read()
	    sign1 = list(map(str, allText.split()))
    sign1_random = random.choice(sign1)

    with open("fastmathsign.txt") as file:
	    allText = file.read()
	    sign2 = list(map(str, allText.split()))
    sign2_random = random.choice(sign2)

    print(f"\n {random_number_1}")
    print(f"{sign1_random}{random_number_2}")
    print(f"{sign2_random}{random_number_3}")

    answer = int(input('Answer: '))

    if sign1_random == '+':
        Math1 = random_number_1 + random_number_2
    elif sign1_random == '-':
        Math1 = random_number_1 - random_number_2

    if sign2_random == '+':
        Math2 = Math1 + random_number_3
    elif sign2_random == '-':
        Math2 = Math1 - random_number_3
    if answer == Math2:
        print('Correct! \n')
    else:
        print('Wrong :( \n')