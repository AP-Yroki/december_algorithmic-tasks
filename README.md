# december_algorithmic-tasks


2. Дан массив целых чисел. Необходимо найти индекс в этом массиве, такой что сумма элементов слева от индекса равна сумме элементов справа от индекса. Если такого индекса не существует, вернуть -1. Если существует более одного такого индекса, вернуть индекс, который находится ближе всего к началу массива.

Примеры:

Для массива [1, 7, 3, 6, 2, 9], ответ будет 3. При индексе 3 элементы слева (1, 7, 3) в сумме дают 11, так же как и элементы справа (2, 9).

Для массива [1, 2, 3, 4, 5, 6], ответ будет -1, так как нет такого индекса, при котором суммы элементов с обеих сторон были бы равны.

Требования к решению:

Написать функцию, принимающую массив целых чисел.
Функция должна возвращать целое число - индекс, удовлетворяющий условиям задачи, или -1, если такого индекса не существует.
Постарайтесь достичь эффективности по времени и памяти. Решение должно иметь линейную временную сложность (O(n)).

3. Шахматный конь обладает уникальным движением: он может перемещаться на два поля по вертикали и одно поле по горизонтали или на два поля по горизонтали и одно поле по вертикали (причем оба образуют форму буквы L). Возможные движения шахматного коня показаны на этой диаграмме:

Шахматный конь может двигаться так, как показано на шахматной диаграмме ниже:

У нас есть шахматный конь и телефонная панель, как показано ниже. Конь может стоять только на числовой ячейке (т. е. синей ячейке).

Учитывая целое число n, выведите количество различных телефонных номеров длины n, которые мы можем набрать.

Вам разрешено изначально разместить коня на любой числовой ячейке, а затем вам необходимо совершить n - 1 прыжков, чтобы набрать число длиной n. Все прыжки должны быть действительными прыжками коня.

Поскольку ответ может быть очень большим, верните ответ по модулю 109+ 7.
Пример1:
Input: n = 1
Output: 10
	
4. Вам дана двумерная матрица размера n x n, представляющая изображение. Поверните изображение на 90 градусов (по часовой стрелке).

Вам необходимо повернуть изображение на месте, а это значит, что вам придется напрямую изменить входную 2D-матрицу. НЕ выделяйте еще одну 2D-матрицу и не выполняйте вращение.
Пример 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

5. Учитывая числа целочисленного массива, отсортированные в неубывающем порядке, удалите несколько дубликатов на месте так, чтобы каждый уникальный элемент появлялся не более двух раз. Относительный порядок элементов должен оставаться неизменным.

Поскольку в некоторых языках изменить длину массива невозможно, вместо этого необходимо поместить результат в первую часть массива nums. Более формально, если после удаления дубликатов осталось k элементов, то первые k элементов nums должны содержать окончательный результат. Не имеет значения, что вы оставите после первых k элементов.

Возвращает k после размещения окончательного результата в первых k слотах чисел.

Не выделяйте дополнительное пространство для другого массива. Вы должны сделать это, изменив входной массив на месте с дополнительной памятью O (1).

Пример 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

6. Даны две строки s и t. Определите, изоморфны ли они.

Две строки s и t изоморфны, если символы в s можно заменить, чтобы получить t.

Все вхождения символа должны быть заменены другим символом с сохранением порядка символов. Никакие два символа не могут сопоставляться одному и тому же символу, но символ может сопоставляться сам с собой.




Пример 1:
Input: s = "egg", t = "add"
Output: true

Пример 2:
Input: s = "foo", t = "bar"
Output: false

Пример 3:
Input: s = "paper", t = "title"
Output: true

7. Вы играете со своим другом в следующую игру Ним:

Изначально на столе лежит куча камней.
Вы и ваш друг будете по очереди ходить, и вы пойдете первым.
На каждом ходу тот, чья очередь, убирает из кучки от 1 до 3 камней.
Победителем становится тот, кто уберет последний камень.

Учитывая n, количество камней в куче, верните true, если вы можете выиграть игру, предполагая, что вы и ваш друг играете оптимально, в противном случае верните false.

Пример1:
Input: n = 4
Output: false

Пример 2:
Input: n = 1
Output: true

 Учитывая строку s в сбалансированных круглых скобках, верните оценку строки.

8. Оценка строки со сбалансированными круглыми скобками основана на следующем правиле:

    «()» имеет оценку 1.
    AB имеет оценку A + B, где A и B — строки со сбалансированными круглыми скобками.
    (A) имеет оценку 2 * A, где A — строка в круглых скобках.







Пример 1:
Input: s = "()"
Output: 1

Пример 2:
Input: s = "(())"
Output: 2

9. Нам дан массив астероидов целых чисел, представляющих астероиды подряд.

Для каждого астероида абсолютное значение представляет его размер, а знак представляет его направление (положительное значение означает право, отрицательное значение означает лево). Каждый астероид движется с одинаковой скоростью.

Узнайте состояние астероидов после всех столкновений. Если два астероида встретятся, взорвется меньший из них. Если оба имеют одинаковый размер, оба взорвутся. Два астероида, движущиеся в одном направлении, никогда не встретятся.
Пример 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Пример 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.





10. Имеется N кг металлического сплава. Из него изготавливают заготовки массой K кг каждая. После этого из каждой заготовки вытачиваются детали массой M кг каждая (из каждой заготовки вытачивают максимально возможное количество деталей). Если от заготовок после этого что-то остается, то этот материал возвращают к началу производственного цикла и сплавляют с тем, что осталось при изготовлении заготовок. Если того сплава, который получился, достаточно для изготовления хотя бы одной заготовки, то из него снова изготавливают заготовки, из них – детали и т.д. Напишите программу, которая вычислит, какое количество деталей может быть получено по этой технологии из имеющихся исходно N кг сплава.
	




	Пример 1: 
Input: Вводятся N, K, M. Все числа натуральные и не превосходят 200.

Output: Выведите одно число — количество деталей, которое может получиться по такой технологии.

11. Шифр состоит в модификации шифра Цезаря числовым ключом. Для этого
под сообщением необходимо написать ключ. Если ключ короче сообщения, то
его повторить циклически. Шифровка получается аналогично шифру Цезаря, но
отсчитывать необязательно только четвертую букву по алфавиту, а ту, которая
сдвинута на соответствующую цифру ключа.
Например:
Сообщение С О В Е Р Ш Е Н Н О С Е К Р Е Т Н О
Ключ 3 1 4 3 1 4 3 1 4 3 1 4 3 1 4 3 1 4
Шифровка Ф П ЖИС Ь И О С С АХИ ЛФ И У Т
Шифр Гронсфельда имеет массу модификаций: вроде записи текста
шифровки буквами другого алфавита, двойное шифрование разными ключами.

