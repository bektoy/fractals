import turtle

def draw_dragon(n, l):
    turtle.shape('turtle')
    if n == 0:
        turtle.forward(l)
    else:
        turtle.right(45)
        draw_dragon(n - 1, l / 2)
        turtle.left(90)
        draw2(n - 1, l / 2)
        turtle.left(45)

def draw2(n, l):
    turtle.shape('turtle')
    if n ==0:
        turtle.forward(l)
    else:
        turtle.right(45)
        draw_dragon(n - 1, l / 2)
        turtle.right(90)
        draw2(n - 1, l / 2)
        turtle.left(45)

draw_dragon(5,2000)




