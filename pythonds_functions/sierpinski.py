from turtle import Turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

def get_mid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points, degree, t):
    colormap = ["#EBF5F7", "#D7E5EB", "#D1D7EC", "#BED4E5", "#F6E2E2", "#EBD7DD"]
    draw_triangle(points, colormap[degree], t)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1, t)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree-1, t)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree-1, t)

my_turtle = Turtle()
my_win = my_turtle.getscreen()
my_points = [(-500, -250), (0, 500), (500, -250)]
sierpinski(my_points, 5, my_turtle)
my_win.exitonclick()