from race_turtle import RaceTurtle
from race_window import RaceWindow
import random

class MoleTurtle(RaceTurtle):
    
    def __init__(self, w: 'RaceWindow', nbr: int) -> None:
        super().__init__(w, nbr)
    
    
    def race_step(self):
        
        chance = random.randint(1, 5)
        
        if chance == 1:
            self.penup()
        else:
            self.pendown()
        
        super().race_step()
    
    def __str__(self):
        return f'Nummer {self.number} - MoleTurtle'
    