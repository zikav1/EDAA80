from race_turtle import RaceTurtle
from race_window import RaceWindow
import random

class DizzyTurtle(RaceTurtle):
    
    def __init__(self, w: 'RaceWindow', nbr: int, dizziness: int) -> None:
        super().__init__(w, nbr)
        self.dizziness = dizziness
    
    
    def race_step(self):
        wobble = random.randint(-self.dizziness * 5, self.dizziness * 5)
        
        self.left(wobble)
        self.right(wobble)
                
        super().race_step()
    
    
    def __str__(self):
                return f'Nummer {self.number} - DizzyTurtle (Yrsel: {self.dizziness})'
    
    
    