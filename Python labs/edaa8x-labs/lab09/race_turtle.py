import turtle
from race_window import RaceWindow
import random

class RaceTurtle(turtle.Turtle):
    
    '''
    Skapar en sköldpadda som ska springa i RaceWindow-objektet w och som
    har start-nummer nbr. Sköldpaddan startar med pennan nere och
    nosen vänd åt höger.
    '''
    def __init__(self, w: 'RaceWindow' , nbr: int) -> None:
        super().__init__()
        self.number = nbr
        
        x = w.get_start_X(self.number)
        y = w.get_start_Y(self.number)
        
        self.penup()
        self.goto(x, y)        
        self.right(0)
        self.pendown()
        
    def race_step(self):
        
        random_step = random.randint(1, 6)
        self.forward(random_step)
    
    def __str__(self):
        return f'Nummer {self.number}'