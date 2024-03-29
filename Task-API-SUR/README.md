# REST API implementation with three HTTP-methods (Backend development) #

:ru: [Русская версия здесь](README_RU.md)

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
**`Bottle`**
**`SQLAlchemy`**

----

## Contents ##

[1. Conditions](#conditions)    
[2. Solution](#solution)    
[3. Results](#results)    
[4. Demo instructions](#demo-instructions)    

## Conditions ##

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

    Minors (<16 y.o.) are not allowed to register with the service.

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

## Solution ##

- To meet the deadlines, it was decided to use a simple **Bottle** web server and
**SQLite3** DBMS instead of **Django** and **PostgreSQL**.

- For simplicity, the age of majority check assumes that the date of birth has
already been pre-formatted and that the `birth` field contains a string of
numbers in the format `YYYY-MM-DD`.

- The **SQLite3** database contains two tables. The **`Users`** table stores all
user data. The **`Errors`** table has a minimal set of error variants, that can
be extended for future needs.

- Since clear criteria for uniqueness have yet to be defined, the first API
method does not check for uniqueness when registering a user (whether such a
user already exists in the database).

- The third API method returns a **json** with all fields except `uid` and
`password`. If the user has `NULL` in the optional `email` and/or `tg` columns,
then the corresponding **json** fields will contain `null`. If desired, we can
exclude the output of such fields.

[:arrow_up: Contents](#contents)

----

## Results ##

[**`api_module.py`**](api_module.py)&nbsp;&mdash; main module with API methods.

[**`api_validations.py`**](api_validations.py)&nbsp;&mdash; additional module
for incoming data validation checks. It contains functional blanks for input
data validation, which can be modified as additional requirements arise.

[**`api_demo.py`**](api_demo.py)&nbsp;&mdash; script to run application and
demonstrate API on port 8080 in virtual environment.

[**`sqlite/db.sql`**](sqlite/db.sql)&nbsp;&mdash; SQL-script to create database
file **`sqlite/db.sqlite3`**.

[:arrow_up: Contents](#contents)

----

## Demo instructions ##

1. Required **Python** version 3.8 or later, with actual **pip** manager.
2. Install **SQLite3** using the [Linux](https://linoxide.com/install-use-sqlite-linux)
or [Windows](https://www.sqlitetutorial.net/download-install-sqlite/) manuals.
3. Download the project files from the current repository directory to the local
directory of the computer.
4. To create the `sqlite/db.sqlite3` database file, enter the `sqlite`
subdirectory, run **SQLite3**, and then enter the following meta-commands:

    ```bash
    # Start sqlite3
    sqlite3 db.sqlite3

    # Meta-commands
    .read db.sql
    .exit
    ```

5. An example sequence of commands in the terminal console to run the project in
the `virtualenv` virtual environment in the local directory:

    ```bash
    python -m venv VENV

    # For Linux:
    source VENV/bin/activate
    # For Windows:
    VENV\Scripts\activate

    pip install -r requirements.txt

    python api_demo.py
    # Exit on Ctrl+C

    # Exit from virtual environment
    # For Linux:
    deactivate
    # For Windows:
    VENV\Scripts\deactivate.bat
    ```

6. You can use the [**`HTTPie`**](https://httpie.io/) package (or anything else
you like) as a PoC. If it is not included in your operating system, you can also
install it in a separate console with the same virtual environment:

    ```bash
    pip install httpie
    ```

    and make requests to check the first method:

    ```bash
    http POST http://127.0.0.1:8080/v1/auth/register phone="+79167003020" login="rubella19" password="1Qwerty!" name="Анастасия" birth="2000-07-28" tg="\@Rubella19" email="anastasia.a.krasnova@gmail.com"
    ```

    to check the second method:

    ```bash
    http POST http://127.0.0.1:8080/v1/auth/login login="rubella19" password="1Qwerty!"
    ```

    to check the third method:

    ```bash
    http GET http://127.0.0.1:8080/v1/user?id=00000000-2222-2222-2222-000000000000
    ```

[:arrow_up: Contents](#contents)

----
