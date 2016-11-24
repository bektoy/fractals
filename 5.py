import turtle
def draw(n,l):
    turtle.shape('turtle')
    if n==0:
        turtle.forward(l)
    else:
        turtle.left(45)
        draw(n - 1, l / 2)
        turtle.right(90)
        draw(n - 1, l / 2)
        turtle.left(45)
draw(5,1000)