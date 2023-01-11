import logging
logging.basicConfig(level = logging.DEBUG)

action_type = input("Podaj działanie, wprowadzająć odpowiednią liczbę: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie\n4 - dzielenie\n")

if action_type == "1":
    numbers = []
    numbers.append(input("Wprowadź pierwszy składnik:"))
    numbers.append(input("Wprowadź drugi składnik:"))
    i = 1
    while i > 0:
        numbers.append(input('Wprowadź kolejny składnik lub wpisz "end" aby uzyskać sumę wprowadzonych liczb:'))
        if numbers[-1] == "end":
            numbers.pop()
            i -= 1
    numbers_string = ', '.join(numbers)
    logging.info(f'Dodaję liczby: {numbers_string}')
    result = 0
    for number in numbers:
        result += int(number)
    print(f'Wynik to: {result}')

if action_type == "2":
    x = int(input("Wprowadź odjemną: "))
    y = int(input("Wprowadź odjemnik: "))
    difference = x - y
    logging.info (f'Odejmuję liczbę {y} od liczby {x}')
    print (f'Wynik to: {difference}')

if action_type == "3":
    numbers = []
    numbers.append(input("Wprowadź pierwszy czynnik:"))
    numbers.append(input("Wprowadź drugi czynnik:"))
    i = 1
    while i > 0:
        numbers.append(input('Wprowadź kolejny czynnik lub wpisz "end" aby uzyskać iloczyn wprowadzonych liczb:'))
        if numbers[-1] == "end":
            numbers.pop()
            i -= 1
    numbers_string = ', '.join(numbers)
    logging.info(f'Mnożę liczby: {numbers_string}')
    product = 1
    for number in numbers:
        product *= int(number)
    print(f'Wynik to: {product}')

if action_type == "4":
    x = int(input("Wprowadź dzielną: "))
    y = int(input("Wprowadź dzielnik: "))
    quotient = x/y
    logging.info (f'Dzielę liczbę {x} przez liczbę {y}')
    print (f'Wynik to: {quotient}')