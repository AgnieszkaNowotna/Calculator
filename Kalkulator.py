import logging
logging.basicConfig(level = logging.DEBUG)

action_type = input("Podaj działanie, wprowadzająć odpowiednią liczbę: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie\n4 - dzielenie\n")

if action_type == "1":
    numbers = []
    i = 1
    while i > 0:
        if i < 3:
            x = input("Wprowadź składnik:")
            if bool(x.isdigit()) == True:
                pass
            else:
                print("Wprowadzona wartość nie jest liczbą całkowitą")
                print("Proszę o ponowne wprowadzenie wartości")
                continue
            numbers.append(x)
            i += 1
        else:
            x = input('Wprowadź składnik lub wpisz "end" aby uzyskać sumę wprowadzonych liczb:')
            if bool(x.isdigit()) == True or x == "end":
                pass
            else:
                print("Wprowadzona wartość nie jest liczbą całkowitą")
                print("Proszę o ponowne wprowadzenie wartości")
                continue
            numbers.append(x)
            i += 1
            if numbers[-1] == "end":
                numbers.pop()
                i -= i
    numbers_string = ', '.join(numbers)
    logging.info(f'Dodaję liczby: {numbers_string}')
    result = 0
    for number in numbers:
        result += int(number)
    print(f'Wynik to: {result}')

if action_type == "2":
    i = 1
    while i > 0:
        x = (input("Wprowadź odjemną: "))
        if bool(x.isdigit()) == True:
            pass
        else:
            print("Wprowadzona wartość nie jest liczbą całkowitą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
        i -=1
    i = 1
    while i > 0:
        y = (input("Wprowadź odjemnik: "))
        if bool(y.isdigit()) == True:
            pass
        else:
            print("Wprowadzona wartość nie jest liczbą całkowitą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
        i -=1
    difference = int(x) - int(y)
    logging.info (f'Odejmuję liczbę {y} od liczby {x}')
    print (f'Wynik to: {difference}')

if action_type == "3":
    numbers = []
    i = 1
    while i > 0:
        if i < 3:
            x = input("Wprowadź czynnik:")
            if bool(x.isdigit()) == True:
                pass
            else:
                print("Wprowadzona wartość nie jest liczbą całkowitą")
                print("Proszę o ponowne wprowadzenie wartości")
                continue
            numbers.append(x)
            i += 1
        else:
            x = input('Wprowadź czynnik lub wpisz "end" aby uzyskać sumę wprowadzonych liczb:')
            if bool(x.isdigit()) == True or x == "end":
                pass
            else:
                print("Wprowadzona wartość nie jest liczbą całkowitą")
                print("Proszę o ponowne wprowadzenie wartości")
                continue
            numbers.append(x)
            i += 1
            if numbers[-1] == "end":
                numbers.pop()
                i -= i
    numbers_string = ', '.join(numbers)
    logging.info(f'Mnożę liczby: {numbers_string}')
    product = 1
    for number in numbers:
        product *= int(number)
    print(f'Wynik to: {product}')

if action_type == "4":
    i = 1
    while i > 0:
        x = (input("Wprowadź dzielną: "))
        if bool(x.isdigit()) == True:
            pass
        else:
            print("Wprowadzona wartość nie jest liczbą całkowitą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
        i -=1
    i = 1
    while i > 0:
        y = (input("Wprowadź dzielną: "))
        if bool(y.isdigit()) == True:
            pass
        else:
            print("Wprowadzona wartość nie jest liczbą całkowitą")
            print("Proszę o ponowne wprowadzenie wartości")
            continue
        i -=1
    quotient = int(x)/int(y)
    logging.info (f'Dzielę liczbę {x} przez liczbę {y}')
    print (f'Wynik to: {quotient}')