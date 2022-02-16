#!/usr/bin/python3

HEADER = '''<!DOCTYPE html>
<HTML LANG="ru">
<HEAD>
    <TITLE>B6.13 Домашнее задание</TITLE>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8"/>
</HEAD>
<BODY>
    <H1>Расчёт параметров геометрических фигур</H1>
    <P>На данный момент подразумеваются не произвольные типы фигур, а симметричные. То есть равнобедренные треугольники, правильные пирамиды, конусы и некоторые другие</P>
    <P></P>
    <HR>
'''

FORM_INI = '''    <FORM ID="iniform" STYLE="background: #ddddff; padding: 10px" ACTION="/figure" METHOD="post">
        <P>
            <LABEL>Выбор фигуры:&nbsp;&nbsp;
            <SELECT FORM="iniform" NAME="figtype" SIZE="1">
                <OPTION VALUE="Quadro" SELECTED>Квадрат</OPTION>
                <OPTION VALUE="Cone">Конус</OPTION>
                <OPTION VALUE="Circle">Круг</OPTION>
                <OPTION VALUE="Cube">Куб</OPTION>
                <OPTION VALUE="Parallelepiped">Параллелепипед</OPTION>
                <OPTION VALUE="Pyramid3F">Пирамида трёхгранная</OPTION>
                <OPTION VALUE="Pyramid4F">Пирамида четырёхгранная</OPTION>
                <OPTION VALUE="Rectangle">Прямоугольник</OPTION>
                <OPTION VALUE="Rhombus">Ромб</OPTION>
                <OPTION VALUE="Sphere">Сфера</OPTION>
                <OPTION VALUE="Trapezoid">Трапеция</OPTION>
                <OPTION VALUE="Triangle">Треугольник равнобедренный</OPTION>
                <OPTION VALUE="Cylinder">Цилиндр</OPTION>
            </SELECT>
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Далее">
        </P>
    </FORM>
'''

FORM_QUADRO = '''    <FORM ID="form_quadro" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Сторона квадрата:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_quadro" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины стороны квадрата">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_CONE = '''    <FORM ID="form_cone" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Радиус основания:&nbsp;&nbsp;
                <INPUT NAME="r_" FORM="form_cone" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение радиуса основания конуса">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_cone" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты конуса">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_CIRCLE = '''    <FORM ID="form_circle" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Радиус круга:&nbsp;&nbsp;
                <INPUT NAME="r_" FORM="form_circle" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение радиуса круга">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_CUBE = '''    <FORM ID="form_cube" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Грань куба:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_cube" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины грани куба">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_PARALLELEPIPED = '''    <FORM ID="form_parallelepiped" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Длина основания:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_parallelepiped" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины основания параллелепипеда">
            </LABEL>
        </P>
        <P>
            <LABEL>Ширина основания:&nbsp;&nbsp;
                <INPUT NAME="b_" FORM="form_parallelepiped" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение ширины основания параллелепипеда">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_parallelepiped" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты параллелепипеда">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_PYRAMID3F = '''    <FORM ID="form_pyramid3f" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Длина основания:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_pyramid3f" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины основания тетраэдра">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота основания:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_pyramid3f" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты основания тетраэдра">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота тетраэдра:&nbsp;&nbsp;
                <INPUT NAME="height_" FORM="form_pyramid3f" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты тетраэдра">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_PYRAMID4F = '''    <FORM ID="form_pyramid4f" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Длина основания пирамиды:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_pyramid4f" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины основания пирамиды">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота пирамиды:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_pyramid4f" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты пирамиды">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_RECTANGLE = '''    <FORM ID="form_rectangle" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Основание прямоугольника:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_rectangle" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины основания прямоугольника">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота прямоугольника:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_rectangle" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты прямоугольника">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_RHOMBUS = '''    <FORM ID="form_rhombus" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Первая диагональ ромба:&nbsp;&nbsp;
                <INPUT NAME="d1_" FORM="form_rhombus" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины первой диагонали ромба">
            </LABEL>
        </P>
        <P>
            <LABEL>Вторая диагональ ромба:&nbsp;&nbsp;
                <INPUT NAME="d2_" FORM="form_rhombus" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длинв второй диагонали ромба">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_SPHERE = '''    <FORM ID="form_sphere" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Радиус сферы:&nbsp;&nbsp;
                <INPUT NAME="r_" FORM="form_sphere" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение радиуса сферы">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_TRAPEZOID = '''    <FORM ID="form_trapezoid" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Первое основание трапеции:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_trapezoid" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины первого основания трапеции">
            </LABEL>
        </P>
        <P>
            <LABEL>Второе основание трапеции:&nbsp;&nbsp;
                <INPUT NAME="b_" FORM="form_trapezoid" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины второго основания трапеции">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота трапеции:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_trapezoid" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты трапеции">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_TRIANGLE = '''    <FORM ID="form_triangle" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Основание треугольника:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_triangle" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины основания треугольника">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота треугольника:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_triangle" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты треугольника">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FORM_CYLINDER = '''    <FORM ID="form_cylinder" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Радиус основания цилиндра:&nbsp;&nbsp;
                <INPUT NAME="r_" FORM="form_cylinder" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение радиуса основания цилиндра">
            </LABEL>
        </P>
        <P>
            <LABEL>Высота цилиндра:&nbsp;&nbsp;
                <INPUT NAME="h_" FORM="form_cylinder" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение высоты цилиндра">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FOOTER = '''    <HR>
    <H2><A HREF="/">Начальная страница</A></H2>
    <P></P>
</BODY>
</HTML>'''

#####=====----- THE END -----=====########################################