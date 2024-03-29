## &laquo;Задачки для раскачки&raquo; перед стажировкой YL ##

### Домашка №2 ###

**Требования к задачам:**

- Соответствует ожидаемому результату;
- Написаны без использования сторонних библиотек (можно внутренние, к примеру
`itertools`);
- Код соответствует **PEP8**.


#### Задача 2.1 на циклический итератор ####

Надо написать класс `CyclicIterator`. Итератор должен итерироваться по
итерируемому объекту (`list`, `tuple`, `set`, `range`, `Range2`, и т. д.), и
когда достигнет последнего элемента, начинать сначала.

```text
cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
```

Основа:

```text
class CyclicIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass
```

Для проверки. Ожидаемый вывод программы:

```text
0
1
2
0
1
2
0
1
2
....
```

----

#### Задача 2.2 на разжатие массива ####

У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для
эффективности дни проката хранятся периодами дат. Например, прокат фильма
проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля:

```text
[
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
]
```

Дан class `Movie`. Реализовать у него метод `schedule`. Он будет генерировать
дни, в которые показывают фильм.

Основа:

```text
from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple

@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return []

m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
```

Для проверки. Ожидаемый вывод программы:

```text
2020-01-01 00:00:00
2020-01-02 00:00:00
2020-01-03 00:00:00
2020-01-04 00:00:00
2020-01-05 00:00:00
2020-01-06 00:00:00
2020-01-07 00:00:00
2020-01-15 00:00:00
2020-01-16 00:00:00
2020-01-17 00:00:00
2020-01-18 00:00:00
2020-01-19 00:00:00
2020-01-20 00:00:00
2020-01-21 00:00:00
2020-01-22 00:00:00
2020-01-23 00:00:00
2020-01-24 00:00:00
2020-01-25 00:00:00
2020-01-26 00:00:00
2020-01-27 00:00:00
2020-01-28 00:00:00
2020-01-29 00:00:00
2020-01-30 00:00:00
2020-01-31 00:00:00
2020-02-01 00:00:00
2020-02-02 00:00:00
2020-02-03 00:00:00
2020-02-04 00:00:00
2020-02-05 00:00:00
2020-02-06 00:00:00
2020-02-07 00:00:00
```

----
