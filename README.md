# python-start-course

## Урок 1. Установка Python и Pycharm
### Для установки Python на Windows вам понадобятся следующие шаги:
- Загрузка установщика Python Перейдите на официальный сайт Python и скачайте установщик Python для Windows. Официальный сайт Python: https://www.python.org/downloads/

- Запуск установщика. Запустите загруженный установщик Python и следуйте инструкциям на экране. Убедитесь, что вы выбрали опцию "Add Python to PATH" во время установки, чтобы Python был доступен из командной строки.

- Проверка установки. После завершения установки откройте командную строку и введите команду python --version, чтобы убедиться, что Python успешно установлен.

### Для установки PyCharm на Windows на вашем компьютере, выполните следующие шаги:
- Перейдите на **официальный сайт** PyCharm от JetBrains. Официальный сайт PyCharm от JetBrains: https://www.jetbrains.com/ru-ru/pycharm/download/?section=windows
- Скачайте последнюю версию **PyCharm Community Edition для Windows**.
- Запустите загруженный установщик PyCharm.
- Следуйте инструкциям на экране, чтобы завершить установку. Убедитесь, что вы выбрали правильную версию PyCharm (Community Edition или Professional) в соответствии с вашими потребностями.
- После завершения установки, запустите PyCharm.

### Для создания первого проекта в PyCharm вам потребуется выполнить следующие шаги:
- В меню выберите **"File"** (Файл) и затем **"New Project"** (Новый проект).
- В появившемся окне выберите **местоположение для вашего проекта** и **введите его название**.
- Нажмите кнопку **"Create"** (Создать) для создания проекта.

## Урок 2. Переменные, оператор присваивания, функции type и id
### Типизация
**Типизация** - это концепция, связанная с определением **типов данных в программировании**. Она определяет, **какие типы данных могут быть использованы в языке программирования** и **как эти типы взаимодействуют друг с другом**.

В языках программирования **типизация** может быть **динамической** или **статической**.
- **Динамическая типизация** означает, что **тип** переменной определяется **автоматически** на основе значения, которое ей присваивается.
- **Статическая типизация**, напротив, требует **явного объявления типов переменных** и **проверки их соответствия во время компиляции**.

### Типизация в Python.
В Python используется **динамическая типизация**, что означает, что **тип переменной определяется автоматически** на основе значения, которое ей присваивается. В отличие от языков с явной типизацией, в Python вам не нужно объявлять тип переменной явно.

### Основные компоненты и действия, которые присутствуют в программировании:
- Данные
- Вычисления
- Проверка условий
- Циклы

### Переменные
**Переменная** - это имя, которое используется для хранения значения. Она представляет собой **ссылку на объект в памяти компьютера**. Переменные в Python могут содержать различные типы данных.  
В Python **имена переменных** могут состоять из **букв (как строчных, так и заглавных)**, **цифр** и **символа подчеркивания**.  
**Имя переменной не может начинаться с цифры**.  
Python также является **регистрозависимым языком**, поэтому переменные **myVar**, **myvar** и **MYVAR** будут **считаться разными переменными**.
```python
a = 7
```
- **a** - это имя переменной. 
- **=** - это оператор присваивания. Он позволяет присвоить переменной определенное значение или ссылку на объект.
- **7** - это объект на который ссылается **а**. 

В языке **Python** переменные **не хранят сами объекты**, а лишь **ссылаются** на них с определенными значениями. Это означает, что **одной переменной можно присваивать объекты разных типов данных**. Например, вы можете создать переменную x и присвоить ей значение числа, а затем изменить ее значение, присвоив ей строку или другой объект. В Python переменные являются **ссылками на объекты**, и их значения могут изменяться в процессе выполнения программы.

Например:
```python
x = 10
print(x)  # Вывод: 10

x = "Hello, world!"
print(x)  # Вывод: Hello, world!

x = [1, 2, 3]
print(x)  # Вывод: [1, 2, 3]
```
### Функция id
Каждый объект в Python имеет свой **уникальный идентификатор**, который можно получить с помощью функции **id()**. Идентификатор представляет собой **целое число, которое гарантированно уникально для каждого объекта во время его существования**.

Например:
```python
a = 2
b = a 
c = b
print(id(a)) # Вывод: 140719720362824
print(id(b)) # Вывод: 140719720362824
print(id(c)) # Вывод: 140719720362824
```
**Идентификаторы** у всех трех переменных будут **одинаковы**. Это говорит о том, что эти **три переменные** ссылаються на **один объект**.

### Функция type
Функция **type()** в языке Python используется для получения **типа объекта**. Она возвращает информацию о **типе данных**, к которому принадлежит **объект**.

Например:
```python
x = 5
print(type(x))  # Вывод: <class 'int'>

y = "Hello"
print(type(y))  # Вывод: <class 'str'>

z = [1, 2, 3]
print(type(z))  # Вывод: <class 'list'>
```
## Вопросы:
1. Что представляет собой переменная в Python?
2. Что делает оператор присваивания (=)?
3. Какая типизация реализована в Python?
4. Что происходит при присваивании одной переменной другой (a = b)?
5. Для чего используется функция type?
6. Различаются ли имена переменных arg, Arg, ARG интерпретатором языка Python?
7. Можно ли функции id присвоить число 7 (id = 7)?

## Урок 3. Числа и операции над ними
### Числовые типы данных
В **Python** существуют **различные типы чисел**.  
Вот некоторые из них:
- **Целые числа (int)**: представляют целочисленные значения, например, 0, -1, 100 и т.д.
- **Вещественные числа (float)**: представляют числа с плавающей точкой, такие как 0.5, -3.14, 2.71828 и т.д.
- **Комплексные числа (complex)**: представляются в виде **x + yj**, где **x** и **y** - это **вещественные числа**, а **j** - мнимая единица. Например, **3 + 2j**, **-1.5 + 0.5j** и т.д.

Например:
```python
x = 10  # Целое число
y = 3.14  # Вещественное число
z = 2 + 3j  # Комплексное число

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```
### Операции над типами данных
1. **Сложение (+)**: оператор сложения используется для сложения двух чисел. Например:
```python
x = 5 + 3
print(x)  # Выводит: 8
y = 2
z = 5
res = y + z
print(res) # Выводит: 7
```
2. **Вычитание (-)**: оператор вычитания используется для вычитания одного числа из другого. Например:

```python
y = 10 - 4
print(y)  # Выводит: 6
y = 2
z = 5
res = y - z
print(res) # Выводит -3
```

3. **Умножение (*)**: оператор умножения используется для умножения двух чисел. Например:
```python
z = 2 * 6
print(z)  # Выводит: 12
y = 2
z = 5
res = y * z
print(res) # Выводит 10
```
4. **Деление (/)**: оператор деления используется для деления одного числа на другое. В результате получается число с плавающей точкой (float). Например:
```python
a = 10 / 3
print(a)  # Выводит: 3.3333333333333335
y = 2
z = 5
res = y / z
print(res) # Выводит 0.4
```
5. **Целочисленное деление (//)**: оператор целочисленного деления возвращает целую часть от деления одного числа на другое. Например:
```python
x = 10 // 3
print(x)  # Выводит: 3
y = 2
z = 5
res = y // z
print(res) # Выводит 0
```
6. **Остаток от деления (%)**: оператор остатка от деления возвращает остаток от деления одного числа на другое. Например:
```python
y = 10 % 3
print(y)  # Выводит: 1
y = 2
z = 5
res = y % z
print(res) # Выводит 4
```
7. **Возведение в степень (`**`)**: оператор возведения в степень используется для возведения числа в определенную степень. Например:
```python
z = 2 ** 3
print(z)  # Выводит: 8
y = 2
z = 5
res = y % z
print(res) # Выводит 32
```
### Сокращенная запись операторов
**Сокращенная запись оператора** - это специальный синтаксис, который позволяет выполнять операцию и присваивание значения переменной в одной строке кода.
```python
x = 5
x += 3
print(x)  # Выводит: 8
```
Сокращенную запись оператора можно использовать с любым из семи перечисленных выше операторов.
## Вопросы:
1. К какому типу данных относится int?
2. К какому типу данных относится float?
3. Как называется оператор **`+`**
4. Как называется оператор **`-`**
5. Как называется оператор **`*`**
6. Как называется оператор **`/`**
7. Как называется оператор **`//`**
8. Как называется оператор **`%`**
9. Как называется оператор **`**`**
10. Что выведит строка `print(a + b)`, если a = 7.0, b = 2.5
11. Что выведит строка `print(a ** b)`, если a = 2, b = 4
12. Что выведит строка `print(a / b ** c)`, если a = 32, b = 2, c = 4
13. Что выведит строка `print(a % b)`, если  a = 11, b = 3
14. Что выведит строка `print(a // b)`, если a = 21, b = 4
15. Какой тип данных мы увидим, выполнив строчку `print(type(8/2))`
16. Чему будет равно k?
```python
k = 8
k *= 2
print(k)
```
17. Чему будет равно i?
```python
i = 2
i += 3
print(i)
```

## Урок 4. Математические функции. Модуль math. Функции print() и input()
В языке Python есть множество **встроенных математических функций**, которые могут быть использованы для выполнения различных вычислений.  
Вот некоторые из них:
1. **`abs(x)`**: возвращает абсолютное значение числа **x**.
```python
x = abs(-5)
print(x)  # Выводит: 5
```
2. **`round(x)`**: округляет число x до **ближайшего целого значения**.
```python
x = round(3.7)
print(x)  # Выводит: 4
```
3. **`max(x1, x2, ...)`**: возвращает **наибольшее значение** из переданных аргументов.
```python
x = max(5, 3, 8)
print(x)  # Выводит: 8
```
4. **`min(x1, x2, ...)`**: возвращает **наименьшее значение** из переданных аргументов.
```python
x = min(5, 3, 8)
print(x)  # Выводит: 3

```
5. **`pow(x, y)`**: возвращает значение **x в степени y**.
```python
x = pow(2, 3)
print(x)  # Выводит: 8
```
6. **`sum(iterable)`**: возвращает **сумму всех элементов** в итерируемом объекте.
```python
x = sum([1, 2, 3, 4, 5])
print(x)  # Выводит: 15
```
### Молуль math
Модуль **math** в Python предоставляет **функции для выполнения математических операций**. Чтобы импортировать модуль math, вы можете использовать следующую конструкцию:
```python
import math
```
После импорта модуля math вы можете **использовать его функции** для выполнения различных математических операций.  
Некоторые математические операции модуля math:
1. **`math.sqrt(x)`**: возвращает **квадратный корень** числа x.
```python
import math

x = math.sqrt(16)
print(x)  # Выводит: 4.0
```
2. **`math.pow(x, y)`**: возвращает **значение x в степени y**.
```python
import math

x = math.pow(2, 3)
print(x)  # Выводит: 8.0
```
3. **`math.ceil(x)`**: **округляет число** x вверх **до ближайшего целого значения**.
```python
import math

x = math.ceil(3.2)
print(x)  # Выводит: 4
```
4. **`math.floor(x)`**: **округляет число** x **вниз до ближайшего целого значения**.
```python
import math

x = math.floor(3.8)
print(x)  # Выводит: 3
```
5. **`math.radians(x)`**: **преобразует угол из градусов в радианы**.
```python
import math

x = math.radians(90)
print(x)  # Выводит: 1.5707963267948966
```
6. **`math.sin(x)`**, **`math.cos(x)`**, **`math.tan(x)`**: возвращают синус, косинус и тангенс угла x (в радианах).
```python
import math

x = math.sin(math.radians(90))
print(x)  # Выводит: 1.0
```
7. `math.log(x, base)`: возвращает **логарифм числа x по указанному основанию base**.
```python
import math

x = math.log(10, 2)
print(x)  # Выводит: 3.3219280948873626
```
8. `math.log10(x)`: **возвращает десятичный логарифм числа x**.
```python
import math

x = math.log10(100)
print(x)  # Выводит: 2.0
```
9. `math.factorial(x)`: возвращает факториал числа x.
```python
import math

x = math.factorial(5)
print(x)  # Выводит: 120
```
### Функция print()
- Функция **print()** используется для **вывода текста или значений переменных на экран**.
- Она может **принимать один или несколько аргументов**, разделенных запятыми.
- Аргументы могут быть **строками, числами или другими объектами**, которые могут быть преобразованы в строку.
- Функция print() **автоматически добавляет символ новой строки (\n)** в конце вывода, но это поведение можно изменить с помощью аргументов **end** и **sep**.  
**Примеры использования**:
```python
x = 17
print("Привет, мир!")  # Выводит строку "Привет, мир!"
print(42)  # Выводит число 42
print("Значение переменной x:", x)  # Выводит значение переменной x
```

### Функция input():
- Функция input() используется для получения ввода от пользователя.
- Она может принимать необязательный аргумент - строку, которая будет отображаться перед ожиданием ввода.
- Функция input() возвращает введенное пользователем значение в виде строки.
**Пример использования**:
```python
name = input("Введите ваше имя: ")
print("Привет, " + name + "!")  # Выводит приветствие с именем пользователя
```
## Задание:
1. Допишите текст программы. Выведите в консоль все переменные в одну строчку с помощью одной функции print().
```python
x = 2
y = 5
z = 12
# продолжите программу
```
2. Допишите текст программы. Выведите в консоль все переменные в три строчки с помощью одной функции print().
```python
x = 2
y = 5
z = 12
# продолжите программу
```
3. Допишите текст программы. Выведите в консоль все переменные через пробел используя две функции **print()**.
```python
x = "Привет,"
y = "Мир"
# продолжите программу
```
4. Создать три переменные в которые по очереди будут присваиваться разные слова. Вывести эти слова через запятую используя один print(). 

5. Допишите текст программы. Выведите в консоль модуль значения переменной `d` в консоль.
```python
d = int(input())
# продолжите программу
```
6. Допишите текст программы. Выведите в консоль минимальное значение из созданных переменых.
```python
a = 1
b = 3
c = 45
d = 12
e = 0
# продолжите программу
```
7. Допишите текст программы. Выведите в консоль максимальное значение из созданных переменых.
```python
a = 1
b = 3
c = 45
d = 12
e = 0
# продолжите программу
```
8. Выведите в консоль значение гипотенузы треугольника, если катеты равны a = 3, b = 4.  
Формула гипотенузы:
![Формула гипотенузы](img/формула_гипотенузы.jpg)
9. В лагерь нужно отвезти 40 детей и 5 вожатых с помощью автобусов. Максимальная вместимость автобуса 20 человек. Напишите программу для вычисления минимального числа автобусов. Результат (целое число) выведите в консоль.
10. Геливая ручка стоит 20 рублей. Магазин предоставляет скидку в 10% на каждую купленную ручку. Какое количесвто ручек можно будет купить на 500 рублей. Результат (целое число) выведите в консоль.

## Урок 5. Логический тип Bool. Операторы сравнения
**Логический тип bool** в языке программирования Python используется для представления **логических значений** и имеет два возможных значения: **True (истина)** и **False (ложь)**.
### Операторы сравнения
- В Python существуют **операторы сравнения**, которые позволяют **сравнивать значения** и **возвращать логический результат**.
- Операторы сравнения в Python включают:
  - `== (равно)`;
  - `!= (не равно)`; 
  - `> (больше)`; 
  - `< (меньше)`;
  - `>= (больше или равно)`;
  - `<= (меньше или равно)`.
- Результатом оператора сравнения является логическое значение True или False.
```python
a = int(input())
b = int(input())
print(a == b)
print(a > b)
print(a <= b)
```

### Преобразование в логический тип:
- В Python можно преобразовать **другие типы данных** в **логический тип с помощью функции bool()**.
- Значения, которые преобразуются в **False**, включают **пустые строки, числа равные нулю, пустые контейнеры (списки, кортежи, словари) и значение None**.
```python
a = None
b = ""
d = 0

print(bool(a)) # False
print(bool(b)) # False
print(bool(d)) # False
```
- Все остальные значения преобразуются в True.
```python
a = "Строка"
c = 1

print(bool(a)) # True
print(bool(c)) # True
```
### Операторы `and` `or` `not`
Операторы `and`, `or` и `not` в языке программирования Python используются для выполнения логических операций и манипуляций с логическими значениями.
- Оператор `and` выполняет **логическое "и"** между двумя операндами. Он возвращает **True, если оба операнда являются истинными**, и **False в противном случае**.
- Оператор `or` выполняет **логическое "или"** между двумя операндами. Он возвращает **True, если хотя бы один из операндов является истинным**, и **False в противном случае**.
- Оператор `not` выполняет **логическое отрицание операнда**. Он возвращает **True, если операнд является ложным**, и **False, если операнд является истинным**.
```python
x = 5
y = 10

print(x > 0 and y > 20)  # Выводит False
print(x > 0 or y > 20)  # Выводит True
print(not x > 0)  # Выводит False
```
### Приоритет операторов
**Приоритет операторов** определяет порядок выполнения операций в выражениях.
#### Таблица приоритетов операторов:
1. `**` - оператор возведения в степень имеет самый высокий приоритет.
2. `*, /, //, %` - операторы умножения, деления, целочисленного деления и остатка от деления имеют одинаковый приоритет и выполняются слева направо.
3. `+, -` - операторы сложения и вычитания также имеют одинаковый приоритет и выполняются слева направо.
4. `<, >, <=, >=` - операторы сравнения имеют одинаковый приоритет и выполняются слева направо.
5. `==, !=` - операторы равенства и неравенства имеют одинаковый приоритет и выполняются слева направо.
6. `not` - оператор логического отрицания выполняется перед операндом.
7. `and` - оператор логического И выполняется слева направо.
8. `or` - оператор логического ИЛИ выполняется слева направо.

## Задание:
1. Какой результат (True или False) будет получен при выполнении команды `print(10 < 10)`?
2. Какой результат (True или False) будет получен при выполнении команды `print(10 <= 10)`?
3. Допишите текст программы. `a` - это вещественное число (с плавающей точкой). Программа должна выводит True, если целая часть числа `a` кратна трём, и False если не кратна.
```python
a = 78,34
# продолжите программу
```
4. Допишите текст программы. `x` - это стоимость книги. Определите является ли дробное значение (число после запятой) больше 50. В консоль вывести True если больше и False если нет.
```python
x = 435.78
# продолжите программу
```
5. Допишите текст программы. `a, b, c` - предполагаемые длины сторон треугольника. Определите, действительно ли треугольник с такими сторонами может существовать (Сумма длин двух произвольных сторон всегда должна быть больше третьей стороны)? В консоль вывести True, если треугольник формируется и False - в противном случае.
```python
a = 8
b = 11
c = 12
# продолжите программу
```
## Урок 6. Введение в строки. Операции над строками.
### Строка
**Строка** в языке Python представляет собой **последовательность символов, заключенных в одинарные (') или двойные (") кавычки**. Строки могут содержать **любые символы, включая буквы, цифры, специальные символы и пробелы**. Они используются для **хранения и манипуляции текстовой информацией в программе**.
```python
s1 = 'Привет, мир!'
s2 = "Hello, world!"
```
**Многострочные строки** задаются с помощью тройных одинарных (''') или тройных двойных (""") кавычек.  
Например:
```python
s3 = '''
Это строка 1.
Это строка 2.
'''
print(s3)
```
Если мы попробуем отобразить эту строку в консоли Python, то увидим, что наши строки разделены специальным символом:
```
'\nЭто строка 1.\nЭто строка 2.\n'
```
Символ строки `\n` представляет собой **управляющую последовательность, которая обозначает перенос на новую строку**. При выводе строки, если встречается символ \n, текст переносится на новую строку.  
Например:
```python
s4 = "Это строка 1.\nЭто строка 2."
print(s4)
```
Строка так же может вообще не содержать символов - это будет пустая строка.
```python
s = ""
print(s)
```
### Базовые операции над строками
**Базовые операции** над строками включают `конкатенацию (объединение)` строк с помощью оператора `+` и `повторение строки` с помощью оператора `*`.
- `Оператор +` используется для конкатенации (соединения) строк. Он позволяет объединить две строки в одну.  
Например:
```python
s5 = "Привет, " + "мир!"
print(s5)  # Выводит "Привет, мир!"
```
- `Оператор *` в языке Python используется для дублирования строкового фрагмента. Он позволяет повторить строку несколько раз.  
Например:
```python
s6 = "spam" * 3
print(s6)  # Выводит "spamspamspam"
```
### Преобразование в строку
**Функция** `str()` используется для **преобразования аргумента в строковое представление**. Она принимает аргумент **любого типа данных** и **возвращает его строковое представление**.  
Например:
```python
num = 42
s7 = "The answer is: " + str(num)
print(s7)  # Выводит "The answer is: 42"
```
### Вычисление длины строки
**Функция** `len()` используется для **вычисления длины строки**. Она принимает **строку в качестве аргумента** и **возвращает количество символов в строке**.  
Например:
```python
s8 = "Hello, world!"
length = len(s8)
print(length)  # Выводит 13
```
### Оператор для проверки вхождения подстроки в строку
**Оператор** `in` в языке Python используется для **проверки вхождения подстроки в строку**. Он возвращает логическое значение `True`, если **подстрока присутствует в строке**, и `False` в **противном случае**.  
Например:
```python
s9 = "Hello, world!"
print("world" in s9)  # Выводит True
print("foo" in s9)  # Выводит False
```
### Сравнение строк
Операторы сравнения `(==, !=, >, <, >=, <=)` используются для **сравнения строк**. Они сравнивают строки лексикографически (по алфавиту) и возвращают логическое значение True или False.  
При **лексикографическом сравнении строк** происходит сравнение символов в строках **по их порядку в таблице символов**. Сравнение начинается с первого символа каждой строки и продолжается до тех пор, пока не будет найдено отличие или одна из строк не закончится.
**Алгоритм сравнения**:
- Сравниваются первые символы обеих строк. Если они различаются, то строка с меньшим символом считается "меньшей" в лексикографическом порядке. Например, строка "apple" будет меньше строки "banana", потому что символ "a" имеет меньший код ASCII, чем символ "b".
- Если первые символы совпадают, то сравниваются следующие символы в обеих строках. Процесс продолжается до тех пор, пока не будет найдено отличие или одна из строк не закончится.
- Если одна строка заканчивается, а другая продолжает иметь символы, то строка, которая закончилась, считается "меньшей" в лексикографическом порядке. Например, строка "apple" будет меньше строки "applesauce".
- Если обе строки заканчиваются одновременно и не было найдено отличий, то строки считаются равными.
Например:
```python
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # Выводит True

str3 = "apple"
str4 = "applesauce"
print(str3 < str4)  # Выводит True

str5 = "apple"
str6 = "apple"
print(str5 == str6)  # Выводит True
```
### Таблица символов
**Таблица символов** в Python основана на стандарте Unicode, который определяет уникальный числовой код для каждого символа. Коды символов в таблице Unicode могут быть представлены в различных кодировках, таких как ASCII.

В Python для определения кода **ASCII** символа используется функция `ord()`. Она принимает символ в качестве аргумента и возвращает его числовое значение в кодировке ASCII.  
Например:
```python
char = 'A'
ascii_code = ord(char)
print(ascii_code)  # Выводит 65
```
## Задание
1. В каких кавычках можно задать строки?
2. В каких кавычках можно задать многострочные строки?
3. Как обозначается символ переноса на новую строку?
4. Что будет выведено в консоль при выполнении команды: `print( (1+2)*('7'+'8') )`
5. Допишите текст программы. Есть две строки s1 и s2. Необходимо сформировать новую строку, продублировав первое слово дважды, а второе - трижды и вывести результат на экран.
```python
s1 = "hello"
s2 = "python"
# продолжите программу
```
6. Допишите текст программы. Есть две переменные a и b. Необходимо сформировать строку вида: `Переменная a = <значение>, переменная b = <значение>` и вывести на экран.
```python
a = 12
b = 7
# продолжите программу
```
7. Допишите текст программы. Есть переменная s3, которая является строкой. Необходимо сформировать новую строку вида: `Строка: <введенная строка>. Длина: <длина строки>` и вывести ее на экран.
```python
s3 = "Hello, Python!"
# продолжите программу
```
8. Допишите текст программы. Есть две переменные s4 и s5. Необходимо вычислить следующие булевы значения:
- проверка вхождения первого слова во второе
- сравнение двух слов
- сравнение на **больше** первого слова со вторым
- сравнение на меньше первого слова со вторым
Вывести результаты на экран одной строкой.
```python
s4 = "str"
s5 = "fivestr"
# продолжите программу
```
9. Допишите текст программы. Есть две переменные char1 и char2. Необходимо сформировать строку вида: `Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>` и вывести ее на экран.
```python
char1 = "a"
char2 = "z"
# продолжите программу
```

## Урок 7. Индексы и срезы строк.

### Индексы в строке
Строка представляет собой **последовательность символов**, заключенных в одинарные или двойные кавычки.  
Каждый символ строки имеет свой **уникальный, порядковый номер**. Эти номера называются **индексами**.  
**Индексы строки** используются для обращения к **отдельным символам в строке**.  
**Индексы** начинаются с **0** для первого символа, 1 для второго символа и так далее.  
**Отрицательные индексы** могут быть использованы для обращения к символам с конца строки, где -1 обозначает последний символ, -2 обозначает предпоследний символ и так далее.
```python
my_string = "Hello, World!"
first_char = my_string[0]  # Получаем первый символ "H"
last_char = my_string[-1]  # Получаем последний символ "!"
```
Если вы попытаетесь обратиться к **несуществующему индексу** строки в Python, возникнет **ошибка IndexError**.  
Это происходит, когда индекс находится за пределами допустимого диапазона индексов строки.
```python
my_string = "Hello, World!"
invalid_index = my_string[100]  # Попытка получить символ с несуществующим индексом
```
### Подстроки. Срезы.
**Подстрока** - это часть строки, которая состоит из **последовательности символов**.  
**Подстрока** может быть получена путем **выбора определенного диапазона символов из исходной строки**.
Для **выделения подстроки** в Python можно использовать **срезы строк**.  

**Срезы строк** позволяют получать **подстроки из исходной строки**.  
Синтаксис срезов состоит из использования **квадратных скобок** и **двоеточия**.  

**Срезы строк** включают:
- **начальный индекс(start)**,
- **конечный индекс(stop)**,
- **шаг(step)**.  

Синтаксис срезов:
```
string[start:stop:step]

start - индекс, с которого начинается срез (включительно).
stop - индекс, на котором заканчивается срез (не включается).
step - шаг, определяющий, какие символы будут включены в срез.
```

Пример использования **срезов**:
```python
main_string = "Python is fun!"
substring = main_string[0:6]  # Получаем подстроку "Python"
substring2 = main_string[7:]  # Получаем подстроку "is fun!"
substring3 = main_string[:6]  # Получаем подстроку "Python is fun"
substring4 = main_string[::2]  # Получаем подстроку "Pto sfn"
```
### Отрицательный шаг в срезах.
**Отрицательный шаг** в срезах используется для получения подстроки в **обратном порядке**. Отрицательный шаг указывает, **какие символы будут включены в подстроку**.

Например:
```python
main_string = "Привет, мир!"
reversed_string = main_string[::-1]  # Получаем строку в обратном порядке "!рим ,тевирП"
substring1 = main_string[4:1:-1]  # Получаем подстроку "ети"
substring2 = main_string[::-2] # Получаем каждый второй символ в обратном порядке
substring3 = main_string[1:4:-1] # Получаем пустую строку
print("reversed_string: ", reversed_string)
print("substring1: ", substring1)
print("substring2: ", substring2)
print("substring3: ", substring3)
```
### Почему при `main_string[4:1:-1]` получаем подстроку "ети", а при `main_string[1:4:-1]` получаем пустую строку?
Отрицательный шаг в срезах указывает направление обхода символов строки. 
В данном случае, `main_string[4:1:-1]` означает, что мы начинаем с индекса **4 (символ "е")**, заканчиваем на индексе **1 (символ "и")** и двигаемся с **шагом -1 (в обратном направлении)**.  
Мы получаем подстроку "ети".  
Если бы мы использовали `main_string[1:4:-1]`, то **начальный индекс (1)** был бы **меньше конечного индекса (4)**, что **противоречит направлению обхода**. В результате получилась **пустая строка**.

Таким образом, срезы всегда должны образовывать **диапозон значений**.

### Изменение строк.
Cтроки являются **неизменяемым типом данных**, что означает, что непосредственное изменение строки невозможно.  
Попытка **изменить символ** по индексу или **присвоить символ новому индексу** строки приведет к ошибке:
```python
main_string = "Hello World!" # Длина строки - 12 символов, т.е. последний символ имеет индекс "11"
main_string[11] = "?" # Ошибка
main_string[12] = "!" # Ошибка
```
Чтобы изменить строку, нужно **создать новую с другим содержимым**:
```python
main_string = "Hello World!"
second_string = main_string[:-1] + "?"
print(main_string)
print(second_string)
```
## Вопросы:
1. Что такое строка?
2. Как выполняется индексация к отдельным символам строки?
3. Как выделять из строк наборы символов – срезы?
4. Возможно ли изменить строку?
4. Способ модификации (изменения) строк через индексы и срезы.
## Задачи:
1. На вход программе подается строка с помощью input(). Прочитайте эту строку и отобразите на экране ее первый и последний символ подряд в одну строчку.
2. На вход программе подается строка с помощью input(). Прочитайте эту строку и отобразите первые четыре ее символа. Полагается, что строка гарантированно имеет длину не менее четырех символов.
3. На вход программе подается строка с помощью input(). Прочитайте эту строку и отобразите последние три ее символа. Полагается, что строка гарантированно имеет длину не менее трех символов.
4. На вход программе подается строка. Прочитайте ее и отобразите все ее символы с нечетными индексами подряд в одну строчку.
5. На вход программе подаются две строки, каждая с новой строчки. Прочитайте их и из первой строки выделите все символы с четными индексами, а из второй - с нечетными. Объедините полученные строки через пробел и выведите результирующую строку на экран.
6. На вход программе подается строка. Необходимо ее прочитать и отобразить первые пять символов в обратном порядке. Полагается, что введенная строка имеет минимум пять символов.
7. На вход программе подаются две строки, каждая с новой строчки. Длина первого слова меньше второго. Необходимо  обрезать второе слово до длины первого и вывести на экран.


## Урок 8. Основные методы строк.
### Методы строк.
**Методы** - это **функции**, которые применяются к объектам **определенного типа данных**.
**Методы строк** - это специальные **функции**, которые могут быть применены к строковым объектам для выполнения **различных операций**.
Чтобы **вызвать метод** для конкретной строки, необходимо **указать объект**, **поставить точку**, **записать имя метода** и в **круглых скобках список аргументов**, если они необходимы:
```
объект.метод(аргументы)
```
### Основные методы строк:
- `String.upper()` - Возвращает строку с заглавными буквами.
```python
s = 'hello'
uppercase = s.upper()
print(uppercase)  # Вывод: 'HELLO'
```
- `String.lower()` - Возвращает строку с малыми буквами.
```python
s = 'WORLD'
lowercase = s.lower()
print(lowercase)  # Вывод: 'world'
```
- `String.count(sub)` - Определяет число вхождений подстроки в строке.
```python
s = 'hello'
count = s.count('l')
print(count)  # Вывод: 2
```
- `String.find(sub)` - Возвращает индекс первого найденного вхождения. Если подстрока не найдена, метод возвращает значение -1.
```python
s = 'hello'
index = s.find('o')
print(index)  # Вывод: 4
```
- `String.rfind(sub)` - Возвращает индекс первого найденного вхождения при поиске справа.
```python
s = 'hello'
index = s.rfind('l')
print(index)  # Вывод: 3
```
- `String.index(sub)` - Возвращает индекс первого найденного вхождения. Если подстрока не найдена, метод вызывает исключение ValueError.
```python
s = 'hello'
index = s.index('e')
print(index)  # Вывод: 1
```
- `String.replace(old, new)` - Заменяет подстроку old на new.
```python
s = 'hello'
new_string = s.replace('l', 'p')
print(new_string)  # Вывод: 'heppo'
```
- `String.isalpha()` - Определяет, состоит ли строка целиком из буквенных символов.
```python
s = 'hello'
is_alpha = s.isalpha()
print(is_alpha)  # Вывод: True
```
- `String.isdigit()` - Определяет, состоит ли строка целиком из цифр. 
```python
s = '123'
is_digit = s.isdigit()
print(is_digit)  # Вывод: True
```
- `String.rjust(width)` - Расширяет строку, добавляя символы слева. 
```python
s = 'hello'
padded = s.rjust(10)
print(padded)  # Вывод: '     hello'
```
- `String.ljust(width)` - Расширяет строку, добавляя символы справа.
```python
s = 'hello'
padded = s.ljust(10)
print(padded)  # Вывод: 'hello     '
```
- `String.split(sep)` - Разбивает строку на подстроки, используя указанный разделитель. 
```python
s = 'hello,world'
words = s.split(',')
print(words)  # Вывод: ['hello', 'world']
```
- `String.join(список)` - Объединяет коллекцию в строку. 
```python
words = ['hello', 'world']
joined = ' '.join(words)
print(joined)  # Вывод: 'hello world'
```
- `String.strip()` - Удаляет пробелы и переносы строк справа и слева. 
```python
s = '   hello   '
stripped = s.strip()
print(stripped)  # Вывод: 'hello'
```
- `String.rstrip()` - Удаляет пробелы и переносы строк справа.
```python
s = '   hello   '
stripped = s.rstrip()
print(stripped)  # Вывод: '   hello'
```
- `String.lstrip()` - Удаляет пробелы и переносы строк слева.
```python
s = '   hello   '
stripped = s.lstrip()
print(stripped)  # Вывод: 'hello   '
```
## Вопросы:
1. Что возвращает метод **String.upper()**?
2. Что возвращает метод **String.lower()**?
3. Что возвращает метод **String.count()**?
4. Что возвращает метод **String.find()**?
5. Что делает метод **String.replace()**?
6. Что делает метод **String.split()**?
7. Что делает метод **String.join**?
8. Что возвратит метод **String.index()**, если подстрока не будет найдена в строке?
9. Что возвратит метод **String.find()**, если подстрока не будет найдена в строке?

## Задачи:
1. На вход программе подается слово в виде строки. Необходимо прочитать это слово и его первую букву сделать заглавной, а остальные - малыми. Результат отобразить на экране.
2. На вход программе подается строка. Необходимо прочитать эту строку и определить число вхождений дефисов (-) в ней. На экране отобразить полученное число. Пример входящей строки: `osnovnye-metody-strok`.
3. На вход программе подается строка. Прочитайте эту строку и найдите в ней индекс первого вхождения фрагмента "ra". Полученное число (индекс) выведите на экран.
4. На вход программе подается строка. Прочитайте ее и замените в ней все двойные дефисы (--) и тройные (---) на одинарные (-). Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран. Пример входящей строки: `osnovnye-metody---strok--practica`.
5. На вход программе подаются три целых положительных числа (максимум трехзначные), записанные в одну строчку через пробел. Необходимо их прочитать из входного потока. Затем, для двухзначных и однозначных чисел добавить слева незначащие нули так, чтобы все числа содержали по три цифры. Вывести на экран полученные числа в столбик (каждое с новой строки) в порядке их чтения из входного потока.
6. На вход программе подается строка, состоящая из слов, разделенных пробелом. Необходимо прочитать строку и подсчитать число слов в ней. Результат (число слов) отобразить на экране.
7. На вход программе подается строка, состоящая из названий городов, разделенных пробелом. Необходимо прочитать эту строку и преобразовать так, чтобы названия городов шли через точку с запятой (без пробелов). Результат  (строку) отобразите на экране. Пример строки: `Москва Тверь Казань`