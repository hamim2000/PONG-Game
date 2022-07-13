
import turtle
x = turtle.Screen()
x.title("Pong by @hamim_nasim_")
x.bgcolor("black")
x.setup(width=800, height=600)
x.tracer(0)
#score
score_a=0
score_b=0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #animation speed 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) #animation speed 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0) #animation speed 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#pen 
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center" ,font=("Courier",24,"normal"))


#function
def paddle_a_up():
    y=paddle_a.ycor() #return y coordinate
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor() #return y coordinate
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor() #return y coordinate
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor() #return y coordinate
    y-=20
    paddle_b.sety(y)


#keyboard
x.listen()
x.onkeypress(paddle_a_up,"w") 
x.onkeypress(paddle_a_down,"s")
x.onkeypress(paddle_b_up,"Up") #user w press the function will be called
x.onkeypress(paddle_b_down,"Down")

#main program
while True:
    x.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(- 290)
        ball.dy*=-1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center" ,font=("Courier",24,"normal"))
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center" ,font=("Courier",24,"normal"))

    #paddle and ball collisions
    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor()+40 and  ball.ycor()>paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()< -340 and ball.xcor() > -350 and ball.ycor()<paddle_a.ycor()+40 and  ball.ycor()>paddle_a.ycor()-40:
        ball.setx(-340)
        ball.dx*=-1