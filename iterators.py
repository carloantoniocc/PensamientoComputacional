frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
print(next(iterador))
#manzana
print(next(iterador))
#pera
print(next(iterador))
#mango
print(next(iterador))
Traceback (most recent call last):
  File "c:/Users/carlos/Desktop/Introducción al pensamiento computacional/code/i
terators.py", line 9, in <module>
    print(next(iterador))
StopIteration