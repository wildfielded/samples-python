## &laquo;Задачки для раскачки&raquo; перед стажировкой YL ##

### Домашка №1 ###

**Требования к задачам:**

- Должны проходить все тесты;
- Написаны без использования сторонних библиотек (можно внутренние, к примеру
itertools);
- Код соответствует PEP8.


#### Задача 1.1 ####

Написать метод `domain_name`, который вернет домен из url адреса:

```text
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
```

Основа:

```text
def domain_name(url):
    return
```

Для проверки:

```text
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
```

----

#### Задача 1.2 ####

Написать метод `int32_to_ip`, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:

```text
2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"
```

Основа:

```text
def int32_to_ip(int32):
    return
```

Для проверки:

```text
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
```

----

#### Задача 1.3 ####

Написать метод `zeros`, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале ($N!=1*2*3*...*N$) заданного числа:

Осторожно&nbsp;&mdash; 1000! имеет 2568 цифр.

Дополнительная информация: [http://mathworld.wolfram.com/Factorial.html](http://mathworld.wolfram.com/Factorial.html)

```text
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```

Основа:

```text
def zeros(n):
    return 0
```

Для проверки:

```text
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
```

----

#### Задача 1.4 ####

Написать метод `bananas`, который принимает на вход строку и возвращает
количество слов &laquo;banana&raquo; в строке.

(Использовать **`-`** для обозначения зачеркнутой буквы)

**Input:** `bbananana`

**Output:**

```text
b-anana--
b-anan--a
b-ana--na
b-an--ana
b-a--nana
b---anana
-banana--
-banan--a
-bana--na
-ban--ana
-ba--nana
-b--anana
```

Основа:

```text
def bananas(s) -> set:
    result = set()
    # Your code here!
    return result
```

Для проверки:

```text
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                "b-a--nana", "-banan--a", "b-ana--na",
                                "b---anana", "-bana--na", "-ba--nana",
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
```

----

#### Задача 1.5 ####

Основа:

```text
```

Для проверки:

```text
```

----
