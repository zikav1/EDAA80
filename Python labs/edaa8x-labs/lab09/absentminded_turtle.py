from race_turtle import RaceTurtle
from race_window import RaceWindow
import random

class AbsentmindedTurtle(RaceTurtle):
    
    def __init__(self, w: 'RaceWindow', nbr: int, absentmindedness: float) -> None:
        super().__init__(w, nbr)
        self.absentmindedness = absentmindedness / 100
    
    
    def race_step(self):
        
        chance = random.randint(0, 100) / 100
        
        if chance < self.absentmindedness:
            return
        
        super().race_step()

    def __str__(self):
        return f'Nummer {self.number} - AbsentmindedTurtle ({self.absentmindedness * 100} % Frånvarande)'



