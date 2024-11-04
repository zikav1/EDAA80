import random
import turtle

def random_step(t):
    
    # Random step between 5 and 15 pixels
    step = random.randint(5,15)
    t.forward(step)
    
    # Random turn of 45 degrees
    turn = random.randint(0,1)
    if turn == 0:
        t.left(45)
    else:
        t.right(45)



def random_walk(t, step):
    for _ in range(step):
        random_step(t)


# Old code to test functionality
#ninja = turtle.Turtle()
#random_walk(ninja, 100)


t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Turtle 1
t1.penup()
t1.goto(-50,-50)
t1.pendown()
t1.shape('turtle')
t1.color('green')


# Turtle 2
t2.penup()
t2.goto(100,100)
t2.pendown()
t2.shape('turtle')
t2.color('red')


while t1.distance(t2) > 100:
    random_step(t1)
    random_step(t2)



turtle.mainloop()
turtle.Screen().delay(1)
