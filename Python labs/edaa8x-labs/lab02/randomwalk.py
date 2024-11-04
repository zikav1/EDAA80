import random
import turtle

t = turtle.Turtle()
t.speed(10)

def random_walk(steps, step_size):
    for _ in range(steps):
        
        random_turn = random.randint(0, 1)
        
        if random_turn == 0:
            t.left(45)
        else:
            t.right(45)    
        
        t.forward(step_size)



random_walk(100,10)

turtle.mainloop()