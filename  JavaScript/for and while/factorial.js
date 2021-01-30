/*
В этом задании вам нужно вычислить факториал для числа,
передаваемого в нашу функцию и вывести его с помощью команды return.
На всякий случай напоминаем, что факториал числа a это произведение
всех целых чисел от 1 до a, например, если а = 5, то факториал a будет равен
1 * 2 * 3 * 4 * 5

Sample Input 1:

7
Sample Output 1:

5040
Sample Input 2:

9
Sample Output 2:

362880
*/
// -------------------------------------------------------------------------------------------------

// 1)вариант
function testFactorial(a) {
    var x = 1;
   while(a) {
       x *= a--;
   }
    return x;
}