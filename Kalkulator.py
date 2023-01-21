import logging
logging.basicConfig(level = logging.DEBUG)
from enum import IntEnum

def check_if_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def check_if_number1():
    j = 1
    while j > 0:
        number = input("Wprowadź liczbę:")
        if check_if_float(number) == True:
            j -= 1
        else:
            print("Wprowadzona wartość nie jest liczbą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
    return float(number)

def check_if_number2():
    j = 1
    while j > 0:
        number = input('Wprowadź kolejną liczbę lub wpisz "stop" aby uzyskać rezultat działania:')
        if check_if_float(number) == True or number == "stop" or number == "Stop":
            j -= 1
        else:
            print("Wprowadzona wartość nie jest liczbą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
    return number

def check_if_number3():
    i = 1
    while i > 0:
        number = (input("Wprowadź liczbę: "))
        if check_if_float(number) == True:
            pass
        else:
            print("Wprowadzona wartość nie jest liczbą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
        i -=1
    i = 1
    return float(number)


Operation = IntEnum('Operation','adding subtraction multiplication dividing')
operation_type = int(input("""Podaj działanie, wprowadzająć odpowiednią liczbę: 
1 - dodawanie 
2 - odejmowanie 
3 - mnożenie
4 - dzielenie
"""))

if operation_type == Operation.adding:
    numbers = []
    i = 1
    while i > 0:
        if i < 3:
            x = check_if_number1()
            numbers.append(x)
            i += 1
        else:
            x = check_if_number2()
            if x == "stop" or x == "Stop":
                i -= i
            else:
                numbers.append(float(x))
    numbers_string = ', '.join([str(number) for number in numbers])
    logging.info(f'Dodaję liczby: {str(numbers_string)}')
    result = 0
    for number in numbers:
        result += number
    print(f'Wynik to: {result}')

if operation_type == Operation.subtraction:
    x = check_if_number3()
    y = check_if_number3()
    logging.info (f'Odejmuję liczbę {y} od liczby {x}')
    print (f'Wynik to: {x-y}')

if operation_type == Operation.multiplication:
    numbers = []
    i = 1
    while i > 0:
        if i < 3:
            x = check_if_number1()
            numbers.append(x)
            i += 1
        else:
            x = check_if_number2()
            if x == "stop" or x == "Stop":
                i -= i
            else:
                numbers.append(float(x))
    numbers_string = ', '.join([str(number) for number in numbers])
    logging.info(f'Mnożę liczby: {str(numbers_string)}')
    product = 1
    for number in numbers:
        product *= number
    print(f'Wynik to: {product}')

if operation_type == Operation.dividing:
    x = check_if_number3()
    y = check_if_number3()
    i = 1
    while i > 0:
        if y == 0.0:
            logging.info('Nie można dzielić przez zero, wprowadź inną wartość')
            y = check_if_number3()
            continue
        else:
            i -= 1
    logging.info (f'Dzielę liczbę {x} przez liczbę {y}')
    print (f'Wynik to: {x/y}')

if operation_type > 4:
    print("Wprowadzono nieprawidłową wartość")