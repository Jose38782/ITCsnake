"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
#Bibliotecas
import random
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#coloca colores random del 0 al 4
colorSnake=random.randint(0,4)
colorFood=random.randint(0,4)

#condiones en caso de el color sea el mismo
if(colorSnake==colorFood):
    if(colorSnake==4):
        colorSnake-=1
    else:
        colorSnake+=1

#lista de los colores
colors = {
    0: "black",
    1: "purple",
    2: "green",
    3: "blue",
    4: "brown",
}

colorSnake = colors[colorSnake]
colorFood = colors[colorFood]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    # Ajuste para que la comida avance hacia una sola direccion
    if head == food:
        print('Snake:', len(snake))
        direcciones = [vector(0, 10), vector(0, -10), vector(10, 0), vector(-10, 0)]

        while True:
            direccion = random.choice(direcciones)
            nueva_pos = food + direccion
            if inside(nueva_pos):
                food.move(direccion)
                break

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
