import turtle
import time

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=700, height=700)
screen.title("Analog Clock")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):

    pen.up()
    pen.goto(0, 210)
    pen.seth(180)
    pen.color('white')
    pen.pd()
    pen.circle(210)

    pen.pu()
    pen.goto(0, 0)
    pen.seth(90)
    pen.lt(30)

    for i in range(1, 13):
        pen.fd(190)
        pen.pd()
        pen.fd(20)
        pen.pu()
        pen.fd(30)
        pen.pd()
        pen.write(i, font=('Arial', 16, 'bold'), align='center')
        pen.pu()
        pen.goto(0, 0)
        pen.lt(30)

    
    angle = (h/12)*360
    angle = angle + (m*0.5)
    pen.pu()
    pen.goto(0, 0)
    pen.color('white')
    pen.seth(90)
    pen.lt(angle)
    pen.pd()
    pen.fd(80)
    
    hands = [('white', 150, 60), ('red', 110, 60)]
    time_set = (m, s)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.pu()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.seth(90)
        pen.lt(angle)
        pen.pd()
        pen.fd(hand[1])

    pen.pu()
    pen.color('white')
    pen.goto(0, -280)
    pen.pd()
    pen.write(str(h)+":"+str(m)+":"+str(s)+" "+time.strftime('%p'), font=('Arial', 22, 'bold'), align='center')

    pen.pu()
    pen.color('white')
    pen.goto(0, -310)
    pen.pd()
    pen.write(time.strftime('%d')+" "+time.strftime('%B')+" "+time.strftime('%Y')+", "+time.strftime('%A'), font=('Arial', 22, 'bold'), align='center')
    

while True:
    h = int(time.strftime('%I'))
    m = int(time.strftime('%M'))
    s = int(time.strftime('%S'))

    draw_clock(h, m, s, pen)
    screen.update()
    time.sleep(1)
    pen.clear()

screen.mainloop()
