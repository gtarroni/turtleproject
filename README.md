# turtleproject

This project implements the `simpleturtle` Python package, a simple version of the Turtle Graphics Language.

#### Minimum requirements:
```
python==2.7.10
numpy==1.16.2
graphics.py==5.0.1.post1 
```

#### Install the package:

- Clone this repository
- In the downloaded directory, create a virtual environment and activate it:
```
virtualenv new_env
source new_env/bin/activate
```
- Install the required packages (numpy and graphics.py) using the provided setup.py file:
```
python setup.py install
```

`simpleturtle` is now ready to be used.

#### Usage:

Start a Python shell within the virtual environment. 

To initialise a graphic window and create a Turtle:
```
from simpleturtle import Turtle
turtle = Turtle("TurtleName")
```

To move the Turtle forward by d pixels:
```
turtle.move_forward(d)
```

To rotate the Turtle anticlockwise by d degrees:
```
turtle.rotate_left(d)
```

To rotate the Turtle clockwise by d degrees:
```
turtle.rotate_right(d)
```

To change the colour (using strings of common colours) of both the Turtle and its future drawings:
```
turtle.set_colour("colour")
```

To disable the Turtle's drawing function:
```
turtle.set_pen_up()
```

To re-enable the Turtle's drawing function:
```
turtle.set_pen_down()
```

#### Minimal working example: 

Create a Turtle instance named Tom and use it to draw a red square:
```
from simpleturtle import Turtle
tom = Turtle("Tom")
tom.set_colour("red")
tom.move_forward(50)
tom.rotate_left(90)
tom.move_forward(50)
tom.rotate_left(90)
tom.move_forward(50)
tom.rotate_left(90)
tom.move_forward(50)
```
