import turtle, random, time, math
from pygame import mixer

# Setup the screen

screen = turtle.Screen()
screen.setup(720, 480)
screen.bgcolor("blue")
screen.title("my little bouncing ball")
screen.tracer(False)

mixer.init()

images = ["ball.gif", "paddle.gif"]
for image in images:
    turtle.register_shape(image)

class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        #self.pencolor("red")
        #self.fillcolor("red")
        self.shape("ball.gif")
        self.shapesize(1)
        self.setpos(0,230)
        self.speed(0)
        self.speed = 0.2
        self.setheading(-90)
        self.direction = "down"
        self.levelup = "on"

    def update(self):
        self.forward(self.speed)
        if self.direction =="down" and self.ycor() <= -250:
            self.direction = "up"
            self.setheading(random.choice((135,90,45)))
        if self.ycor() >= 230:
            self.direction ="down"
            self.setheading(random.choice((-135,-90,-45)))
        if self.xcor() <= -350 or self.xcor() >= 350:
            self.right(45)

    def is_hit(self, other):
        a = (self.xcor() - other.xcor())
        b = (self.ycor() - other.ycor())
        distance = math.sqrt((a**2) + (b**2))
        if distance < 35:
            return True
        else:
            return False 
        
class Player(turtle.Turtle):
    def __init__(self, x, y= -210):
        turtle.Turtle.__init__(self)
        self.penup()
        #self.color("green")
        #self.fillcolor("lightgreen")
        self.shape("paddle.gif")
        self.width = 3
        self.height = 1
        self.shapesize(self.height, self.width)
        self.setpos(x, -220)
        self.speed = 0.4
        self.direction = "stop"

    def update(self):
        if self.xcor() >= 320:
            self.setx(320)
        if self.xcor() <= -320:
            self.setx(-320)
        if self.direction =="left":
            self.goto(self.xcor() - self.speed, self.ycor())
        elif self.direction == "right":
            self.goto(self.xcor() + self.speed, self.ycor())
        elif self.direction == "stop":
            self.goto(self.xcor(), self.ycor())
            
    def left(self):
        self.direction = "left"
    def right(self):
        self.direction = "right"
    def down(self):
        self.direction = "down"

ball = Ball()
player = Player(0)

# key bindings
turtle.listen()
turtle.onkey(player.left,"Left")
turtle.onkey(player.right,"Right")
turtle.onkey(player.down,"Down")

running = True
while running:
    screen.update()
    ball.update()
    player.update()
    if ball.direction == "down" and ball.is_hit(player):
        ball.setheading(random.choice((135,90,45)))
        ball.direction = "up"

    

