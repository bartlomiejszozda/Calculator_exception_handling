from Calculator import Calculator
calc=Calculator()

print ("dodawanie - wpisz add, dzielenie - wpisz div, logarytm - wpisz log, pochodna - wpisz der")
operation = input()

if operation == "add":
    print("wpisz dwie liczby do dodawania")
    a = float(input())
    b = float(input())
    print( calc.add(a,b))
if operation == "div":
    print("wpisz licznik i mianownik")
    a = float(input())
    b = float(input())
    print( calc.division(a,b))
if operation == "log":
    print("wpisz podstawe i liczbe logarytmowana")
    a = float(input())
    b = float(input())
    print( calc.logarithm(a,b))

if  operation == "der":
    print("podaj rownanie i zmienna po ktorej jest pochodna")
    a = str(input())
    b = str(input())
    print( calc.derivative(a,b))



