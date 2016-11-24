import turtle
def draw(n,l):
    turtle.shape('turtle')
    if n==0:
        turtle.forward(l)

    else:
        draw(n - 1, l / 3)
        turtle.left(60)
        draw(n - 1, l / 3)
        turtle.right(120)
        draw(n - 1, l / 3)
        turtle.left(60)
        draw(n - 1, l / 3)

draw(2,100)