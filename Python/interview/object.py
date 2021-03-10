"""
Напишите программу для того, чтобы узнать имя объекта в Python.
Объекты не имеют имен, поэтому нет способа узнать имя объекта.
Операция присвоения используется для связывания имени и значения,
 которое включает в себя имя объекта, к которому должно быть
 привязано значение. Если к этому значению можно обратиться,
 то результатом присвоения будет true, то следующая программа
  может использоваться для поиска ссылочного имени объекта.
"""
class A:
    pass
B = A
a = B()
b = a
print(b)
#<__main__.A instance at 0x16D07CC>
print(a)
#<__main__.A instance at 0x16D07CC>
"""
Класс состоит из имени, а имена вызываются с помощью переменной B,
это создает экземпляр класса try. Суть метода заключается в том,
чтобы среди всех областей видимости определить, что объект 
существует, и уже после этого вывести его имя.
"""