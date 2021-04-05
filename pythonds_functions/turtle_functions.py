from turtle import Turtle

my_turtle = Turtle()
my_win = my_turtle.getscreen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

# draw_spiral(my_turtle, 250)
# my_win.exitonclick()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15, t)
        t.left(40)
        tree(branch_len-10, t)
        t.right(20)
        t.backward(branch_len)

my_turtle.penup()
my_turtle.right(90)
my_turtle.forward(250)
my_turtle.left(180)
my_turtle.pendown()
tree(110, my_turtle)
my_win.exitonclick()