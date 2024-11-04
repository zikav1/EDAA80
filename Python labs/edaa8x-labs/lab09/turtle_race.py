from race_window import RaceWindow
from mole_turtle import MoleTurtle 
from dizzy_turtle import DizzyTurtle
from absentminded_turtle import AbsentmindedTurtle

import random

class TurtleRace:
    def __init__(self, w: 'RaceWindow') -> None:
        self._w = w
        self._turtles = []
        
        for i in range(8):
            
            turtle_num = random.randint(1, 3)
            
            if turtle_num == 1:
                self._turtles.append(MoleTurtle(w, i + 1))
            
            elif turtle_num == 2:
                dizzyness = random.randint(1, 5)
                self._turtles.append(DizzyTurtle(w, i + 1, dizzyness))
            
            else:
                absent = random.uniform(0, 100)
                self._turtles.append(AbsentmindedTurtle(w, i + 1, absent))
                            
        
        
        
        self._race_results = []
        

    def start_race(self):
        while len(self._turtles) > 0:
            for t in self._turtles:
                t.race_step()
                if t.xcor() >= w.X_END_POS:
                    self._race_results.append(t)
                    self._turtles.remove(t)
        

    def print_placement(self):
        for i in range(3):
            print(f'På plats {i + 1}: {self._race_results[i]}')

        
    def __str__(self):
        
        lineup = ''
        
        for turtle in self._turtles:
            lineup += str(turtle)
            lineup += '\n'
        
        return lineup




w = RaceWindow()
race = TurtleRace(w)
print(race)
race.start_race()
race.print_placement()