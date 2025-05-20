import turtle
import random

# Список можливих кольорів
colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

def малюй_квадрат(сторона):
    # Встановлення випадкового кольору пера
    turtle.color(random.choice(colors))
    
    turtle.pendown()  # Опускаємо перо

    for _ in range(4):
        turtle.forward(сторона)
        turtle.left(90)
    
    turtle.penup()  # Піднімаємо перо

# Виклик функції з довжиною сторони 100
малюй_квадрат(100)

turtle.done()