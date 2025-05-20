import turtle
import random

# Список кольорів
colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

def малюй_шестикутник(сторона):
    turtle.pendown()  # Опускаємо перо

    for _ in range(6):
        turtle.color(random.choice(colors))  # Випадковий колір
        turtle.forward(сторона)
        turtle.left(60)

    turtle.penup()  # Піднімаємо перо

# Виклик функції з параметром 100
малюй_шестикутник(100)

turtle.done()