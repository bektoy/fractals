import turtle
def draw(n,l):
    turtle.shape('turtle')
    if n==0:
        turtle.forward(l)

    else:
        draw(n - 1, l / 4)
        turtle.left(90)
        draw(n - 1, l / 4)
        turtle.right(90)
        draw(n - 1, l / 4)
        turtle.right(90)
        draw(n - 1, l / 4)
        draw(n-1,l/4)
        turtle.left(90)
        draw(n - 1, l / 4)
        turtle.left(90)
        draw(n - 1, l / 4)
        turtle.right(90)
        draw(n - 1, l / 4)


draw(4,2000)