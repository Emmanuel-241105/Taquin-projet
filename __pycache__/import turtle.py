import turtle
import random
import time

def firework():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    
    # Fonction pour dessiner un feu d'artifice
    def draw_firework(x, y, colors):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(colors))
        for _ in range(20):
            angle = random.randint(0, 360)
            distance = random.randint(50, 150)
            turtle.left(angle)
            turtle.forward(distance)
            turtle.backward(distance)
            turtle.right(angle)

    turtle.speed(0)
    turtle.hideturtle()
    colors = ["red", "blue", "yellow", "green", "purple", "white", "orange"]

    # Affiche plusieurs feux d'artifice
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        draw_firework(x, y, colors)
        time.sleep(0.5)
    
    turtle.done()

# Exemple de condition
condition = True

# Si la condition est remplie, affiche les feux d'artifice
if condition:
    firework()