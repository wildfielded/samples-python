# REST API implementation with three HTTP-methods (Backend development) #

:ru: [Русская версия здесь](README_RU.md)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
**`Bottle`**

----

## Contents ##

[1. Task conditions](#task-conditions)    
[2. Task solution](#task-solution)    
[3. Results](#results)    
[4. Demo instructions](#demo-instructions)    

## Task conditions ##

Implement REST API with three http-methods:

1. **`POST /v1/auth/register`**    
    Accepts json:

    ```text
    {
        "phone": "+79167003020",
        "login": "rubella19",
        "password": "1Qwerty!",
        "name": "Анастасия",
        "birth": "2000-07-28",
        "tg": "@Rubella19",
        "email": "anastasia.a.krasnova@gmail.com"
    }
    ```

    Wherein **`phone`**, **`name`**, **`birth`**, **`login`**,
    **`password`**&nbsp;&mdash; required fields, **`tg`**,
    **`email`**&nbsp;&mdash; optional.

    It is required to implement data validation checks.

    Minors (<16 y.o.) must not be registered with the service.

    Returns **json** with user ID on success, or **json** with two fields
    **`code`** and **`text`** on error.

2. **`POST /v1/auth/login`**    
    Accepts **json** with two fields **`login`** and **`password`** and returns
    **json** with user ID on success, or **json** with two fields **`code`** and
    **`text`** on error.

3. **`GET /v1/user`**    
    Accepts query-parameter **`id`** and returns **json** with all user fields
    except **`password`** on success, or **json** with two fields **`code`** and
    **`text`** on error.

All data must be stored in a database.

Provide as a result:

- repository with code
- SQL-script to create database schema
- application configuration, database configuration
- which database type was used (write in the **README**)
- how to start the application (write in the **README**)

**Advanced**: Add scripts to run the application. For example, add `Makefile`
with `run` target to run the made API on port 8080.

[:arrow_up: Contents](#contents)

----

## Task solution ##

- To fit the deadlines, it was decided to use a simple **Bottle** web server and
SQLite DBMS instead of **Django** and **PostgreSQL**.

- For simplicity, the age of majority check assumes that the birth date has
already been pre-formatted and that the `birth` field contains a string of
numbers in the format `YYYY-MM-DD`.

- The **SQLite3** database contains two tables. The **`Users`** table stores all
user data. The **`Errors`** table has a minimal pre-set of error variants, which
can be expanded for future requirements.

- Due to clear criteria for uniqueness still need to be defined, the first API
method does not check for uniqueness when registering a user (wether such a user
already exists in the database).

- The third API method returns a **json** with all fields except `uid` and
`password`. If the user has `NULL` in the optional `email` and/or `tg` table
columns, then the corresponding **json** fields contain `null`. If desired, we
can exclude the output of such fields.

[:arrow_up: Contents](#contents)

----

## Results ##

[**`api_module.py`**](api_module.py)&nbsp;&mdash; main module with API methods.

[**`api_validations.py`**](api_validations.py)&nbsp;&mdash; additional module
for incoming data validation checks. It contains functional blanks for
validating input data, which can be modified when additional requirements appear.

[**`api_demo.py`**](api_demo.py)&nbsp;&mdash; script to run application and
demonstrate API on port 8080 in virtual environment.

[**`sqlite/db.sql`**](sqlite/db.sql)&nbsp;&mdash; SQL-script to create database
file **`sqlite/db.sqlite3`**.

[:arrow_up: Contents](#contents)

----

## Demo instructions ##

[:arrow_up: Contents](#contents)

----
