from turtle import Turtle,onscreenclick, onkey, listen, Screen
turtle = Turtle ()
tela = Screen()
turtle.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2

def jogar(x, y):
    turtle.penup()
    turtle.goto(x, y)
    if resultado == 0:
       circulo()


def circulo():
    turtle.color('blue')
    r = 50
    turtle.pendown()
    turtle.circle(r)

tela.onscreenclick(jogar)

listen()
tela.mainloop()

