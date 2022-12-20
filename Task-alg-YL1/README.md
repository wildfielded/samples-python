# Calculating the shortest path for a drone #

:ru: [Русская версия здесь](README_RU.md)

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)

----

## Contents ##

[1. Task conditions](#task-conditions)    
[2. Task solution](#task-solution)    
[3. Results](#results)    
[4. Demo instructions](#demo-instructions)    

## Task conditions ##

- Develop a program to calculate the shortest path for a mail drone to fly. The
drone starts from the post office, flies around all the recipients once to
deliver the parcels and returns to the post office. Destination map with points
and its coordinates set. Ones need to find the shortest route to fly around.

- Destination map:    
![Destination map](ADDS/addresses_map.png)

- Point coordinates:

    ```text
    1. Post office – (0, 2)
    2. Griboedov Str., 104/25 – (2, 5)
    3. Baker Str., 221b – (5, 2)
    4. Bolshaya Sadovaya Str., 302-bis – (6, 6)
    5. Vechnozelyonaya alley, 742 – (8, 3)
    ```

- The result must contain a sequence of points, which make up the shortest of
the routes with the output of intermediate distances for each point (from the
start to the current point) and the total length of the route.

- The point coordinates following each other must show the shortest path found,
indicating the intermediate path length for each next point. The total length of
the entire route is indicated after the equal sign.

- That is, the result of the program must be formatted as follows:

    ```text
    (0, 1) -> (1, 4)[3.1622776601683795] -> (4, 1)[7.404918347287664] -> (5, 5)[11.528023972905324] -> (7, 2)[15.133575248369313] -> (0, 1)[22.204643060234787] = 22.204643060234787
    ```

[:arrow_up: Contents](#contents)

----

## Task solution ##

The total number of all possible routes **$N$** is calculated by the formula
**$N=(n-1)!$**, where **$n$** is number of all destination points.

The number of possible routes to fly around destinations for a given map:
**$(5-1)! = 4! = 24$** routes. Then, the program finds the shortest route and
outputs the sequence of points that make it up.

To search for such a route, program will calculate the distances between the
points that make up the route, and will find total lengths of each route. Then,
it is necessary to find the shortest length by iterating over all possible
routes.

The formula for the distance between two points on a plane is derived from the
Pythagorean theorem: $$L=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2},$$ where **$x_1$**,
**$y_1$**, **$x_2$** and **$y_2$** are coordinates of the first and
second points respectively.

[:arrow_up: Contents](#contents)

----

## Results ##

[**`main.py`**](main.py)&nbsp;&mdash; main program for calculating the shortest
path.

[:arrow_up: Contents](#contents)

----

## Demo instructions ##

1. Required **Python** version **3.8** or later, with actual **pip** manager.
2. Download project files from the current directory of the repository to a
local directory of the computer.
3. An example command sequence in the terminal console to run the project in the
`virtualenv` virtual environment in local directory:

    ```bash
    python -m venv VENV

    # For Linux:
    source VENV/bin/activate
    # For Windows:
    VENV\Scripts\activate

    python main.py

    # Exit from virtual environment
    # For Linux:
    deactivate
    # For Windows:
    VENV\Scripts\deactivate.bat
    ```

[:arrow_up: Contents](#contents)

----
