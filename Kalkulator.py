import logging
logging.basicConfig(level = logging.DEBUG)
from enum import IntEnum

def check_if_float(number):
    try:
        number = float(number)
        return True
    except ValueError:
        return False

def get_numbers():
    array_of_numbers = []
    i = 0
    while True:
        if i ==0:
            text = "Wprowadź pierwszą liczbę: "
        else:
            text = "Wprowadź kolejną liczbę lub 'stop' aby uzyskać wynik działania: "
        i += 1
        number = input(text)
        if number == "stop":
            return array_of_numbers
        if not check_if_float(number):
            print("Wprowadzona wartość nie jest liczbą") 
            continue
        array_of_numbers.append(float(number))

Operation = IntEnum('Operation','adding subtraction multiplication dividing')
operation_type = int(input("""Podaj działanie, wprowadzająć odpowiednią liczbę: 
1 - dodawanie 
2 - odejmowanie 
3 - mnożenie
4 - dzielenie
"""))

if operation_type == Operation.adding:
    array_of_numbers = get_numbers()
    numbers_string = ', '.join([str(number) for number in array_of_numbers])
    logging.info(f'Dodaję liczby: {str(numbers_string)}')
    result = sum(array_of_numbers)
    print(f'Wynik to: {result}')

if operation_type == Operation.subtraction:
    array_of_numbers = get_numbers()
    numbers_string = ', '.join([str(number) for number in array_of_numbers[1:]])
    logging.info (f'Od liczby {str(array_of_numbers[0])} odejmuję liczby {numbers_string}')
    print (f'Wynik to: {array_of_numbers[0] - sum(array_of_numbers[1:])}')

if operation_type == Operation.multiplication:
    array_of_numbers = get_numbers()
    numbers_string = ', '.join([str(number) for number in array_of_numbers])
    logging.info(f'Mnożę liczby: {str(numbers_string)}')
    product = 1
    for number in array_of_numbers:
        product *= number
    print(f'Wynik to: {product}')

if operation_type == Operation.dividing:
    array_of_numbers = get_numbers()
    for number in array_of_numbers[1:]:
        if number == 0.0:
            logging.info('Nie można dzielić przez zero, wprowadź inną wartość')
            array_of_numbers[array_of_numbers.index(0)] = float(input("Wprowadź nową wartość:"))
    numbers_string = ', '.join([str(number) for number in array_of_numbers[1:]])
    logging.info (f'Dzielę liczbę {str(array_of_numbers[0])} przez liczby {numbers_string}')
    result = array_of_numbers[0]
    for number in array_of_numbers[1:]:
        result = result/number
    print (f'Wynik to: {round(result,3)}')

if operation_type > 4:
    print("Wprowadzono nieprawidłową wartość")