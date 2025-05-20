from turtle import *
import random

colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'pink', 'cyan']

def малюй_коло(радіус, x, y):
    up()
    goto(x, y)
    down()
    color(random.choice(colors))
    circle(радіус)
    up()

малюй_коло(30, 0, 0)
малюй_коло(60, 70, 50)
малюй_коло(90, 200, 120)

done()