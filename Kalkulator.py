import logging
logging.basicConfig(level = logging.DEBUG)

action_type = input("Podaj działanie, wprowadzająć odpowiednią liczbę: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie\n4 - dzielenie\n")
if action_type == "1":
    numbers = []
    numbers.append(input("Wprowadź pierwszą liczbę:"))
    numbers.append(input("Wprowadź drugą lczbę:"))
    i = 1
    while i > 0:
        numbers.append(input('Wprowadź kolejną liczbę lub wpisz "end" aby uzyskać sumę wprowadzonych liczb:'))
        if numbers[-1] == "end":
            numbers.pop()
            i -= 1
    numbers_string = ', '.join(numbers)
    logging.info(f'Dodaję liczby: {numbers_string}')
    result = 0
    for number in numbers:
        result += int(number)
    print(result)
