print('Witam w prostym kalkulatorze')
wynik=0
x = int(input('Podaj dwie liczby:\n'))
y = int(input())
def suma(x,y):
    wynik=x+y
    return wynik
def odejmowanie(x,y):
    minus=x-y
    return minus
print('Suma tych liczb to: ', suma(x,y))
print('Różnica tych liczb to: ', odejmowanie(x,y))