import maze
import turtle

# Asking for input
maze_nbr = int(input('What maze do you want to solve. Available options are 1-5'))

if maze_nbr == 5:
    turtle.Screen().tracer(2)


t = turtle.Turtle()
m = maze.Maze(maze_nbr)

# Pos of entry
x, y = m.entry()

# Placing the turlte at the entrance and customizing it
t.shape('turtle')
t.shapesize(0.25)
t.color('green')
t.penup()
t.goto(x, y)
t.pendown()
t.left(90)




while not m.at_exit(t.pos()):
    
    if not m.wall_at_left(t.heading(), t.pos()):
        t.left(90)
        t.forward(1)
    
    elif not m.wall_in_front(t.heading(), t.pos()):
        t.forward(1)
    
    else:
        t.right(90)
    

turtle.mainloop()




