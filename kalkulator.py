print('Witam w prostym kalkulatorze')
wynik=0
x = int(input('Podaj dwie liczby:\n'))
y = int(input())
def odejmowanie(x,y):
    wynik=x-y
    return wynik
print('Suma tych liczb to: ', odejmowanie(x,y))