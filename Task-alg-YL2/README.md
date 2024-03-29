# Тестовое задание «Обратные крестики-нолики» #

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
**`PyQt5`**

----

## Содержание ##

[1. Условия задания](#условия-задания)    
[2. Решение](#решение)    
[3. Краткое описание алгоритма](#краткое-описание-алгоритма)    
[4. Рефакторинг](#рефакторинг)    
[5. Инструкция по запуску проекта](#инструкция-по-запуску-проекта)    

## Условия задания ##

Разработать игру &laquo;Обратные крестики-нолики&raquo; на поле 10 x 10 с
правилом &laquo;Пять в ряд&raquo;&nbsp;&mdash; проигрывает тот, у кого получился
вертикальный, горизонтальный или диагональный ряд из пяти своих фигур
(крестиков/ноликов).

Игра должна работать в режиме &laquo;человек против компьютера&raquo;.

Игра может быть консольной или поддерживать графический интерфейс (будет плюсом,
но не требуется).

При разработке игры учесть принцип DRY (don’t repeat yourself)&nbsp;&mdash;
&laquo;не повторяйся&raquo;. То есть минимизировать повторяемость кода и
повысить его переиспользуемость за счёт использования функций. Функции должны
иметь свою зону ответственности.

Критерии оценки:

1. Качество алгоритмов.
2. Принцип DRY.
3. Качество оформления кода (наименования переменных, форматирование, документация).

[:arrow_up: Содержание](#содержание)

----

## Решение ##

[**`cli_mode.py`**](cli_mode.py)&nbsp;&mdash; Игра в командной строке (CLI).

Игрок ходит крестиками, компьютер&nbsp;&mdash; ноликами. Пустые клетки игрового
поля обозначены точками. Для удобства справа приведены номера строк,
сверху&nbsp;&mdash; номера колонок. Отсчёт слева направо и сверху вниз.

Вначале предлагается выбрать, кто делает первый ход&nbsp;&mdash; игрок (**1**)
или компьютер (**2**).

Ход игрока вводится в формате **`номер_строки / номер_колонки`** цифрами через
дробь (все пробелы устраняются). Если координаты клетки выходят за допустимый
диапазон, строку ввода нельзя интерпретировать, или клетка уже
занята&nbsp;&mdash; ход не производится, надо вводить заново.

Игра заканчивается, если по любому направлению образуется ряд из пяти крестиков
(`"Вы проиграли"`), ноликов (`"Вы выиграли"`), или если не остаётся свободных
клеток (`"Ничья"`).

На любом ходу можно выйти из игры, если вместо координат ввести **`q`** или
**`Q`**.

[**`win_mode.py`**](win_mode.py)&nbsp;&mdash; Графический вариант игры. Требует
установки:

```bash
pip install PyQt5
```

Использованы функции из CLI-варианта игры, адаптированные под графику (для
переиспользования при прямом импорте модуля требуется рефакторинг).

Игрок ходит крестиками, компьютер&nbsp;&mdash; ноликами. Клетки игрового поля
представлены кнопками, на которые нужно нажать, чтобы сделать ход. По умолчанию
первый ход за игроком. В любой момент можно выйти из игры по кнопке
**`"Выход"`** или начать новую игру по соответсвующим кнопкам. Интерфейс
минималистичен, &laquo;интуитивно понятен&raquo; и готов к любым
&laquo;раскраскам&raquo;.

![Снимок окна](screen.png)

**TODO:** Можно попытаться в PyQt5 полностью избавиться от **lambda** через
функции высшего порядка.

[:arrow_up: Содержание](#содержание)

----

## Краткое описание алгоритма ##

После каждого хода, как игрока, так и компьютера, клеткам ***прибавляются***
весовые коэффициенты из соответстующих наборов (кортежей) для игрока
(`DUDE_WEIGHTS`) и компьютера (`COMP_WEIGHTS`). То есть &laquo;интеллект&raquo;
игры за компьютер можно отрегулировать, играясь с весовыми значениями в
кортежах.

Изначально вес каждой клетки нулевой. Как только сделан ход, клетке с
поставленным символом к имеющемуся весу ***прибавляется*** первый весовой
коэффициент из кортежа. Следующие 4 &laquo;веса&raquo; в кортеже прибавляются
последовательно по мере удаления четырём клеткам в линии по каждому направлению
(вверх, вниз, влево, вправо и по четырём диагоналям).

Чтобы сделать ход, компьютер из свободных клеток выбирает список клеток с
минимальным на текущий момент весом, и уже из этого списка делает случайный
выбор с помощью `random.choice()`.

[:arrow_up: Содержание](#содержание)

----

## Рефакторинг ##

Попытка спокойного рефакторинга кода с учётом принципов **`ООП`** (абстракция,
инкапсуляция, наследование, полиморфизм) и **`SOLID`** (single responsibility,
open-closed, liskov substitution, interface segregation, dependency inversion).

[**`play_con.py`**](play_con.py)&nbsp;&mdash; CLI-вариант игры.

[**`play_win.py`**](play_win.py)&nbsp;&mdash; GUI-вариант игры.

[**`game_stuff.py`**](game_stuff.py)&nbsp;&mdash; Модуль, общий для CLI и GUI игр.

[:arrow_up: Содержание](#содержание)

----

## Инструкция по запуску проекта ##

[:arrow_up: Содержание](#содержание)

----
