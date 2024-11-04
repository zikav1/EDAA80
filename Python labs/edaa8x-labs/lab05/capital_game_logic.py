import random

class CapitalGame:
    
    def __init__(self, cc_map: dict[str, str]) -> None:
        self._cc_map = cc_map
        self._score = 0
        self._countries = list(cc_map.keys())
        self._current_country = None
        self._country_tracker = list()
        
    
    def start_game(self) -> None:
        
        print('Welcome to Capitals Quiz Game')
        
        rounds = int(input('How many rounds do you want to play?'))
        
        for _ in range(rounds):
            self.question()
        
        print(f'Game is over! You got {self.get_score()} points')
    
    
    def question(self) -> None:
        
        self._current_country = random.choice(self._countries)
        
        if self._current_country not in self._country_tracker:
            guess = input(f'What is the capital of {self._current_country}?')
            
            self._country_tracker.append(self._current_country)
            
            trimmed_guess = guess.strip()
            
            self.check_guess(trimmed_guess)
            
        else:
            self.question()
        
        
        
        
    
    
    def check_guess(self, guess: str) -> None:
        if guess.lower() == self._cc_map[self._current_country].lower():
            print('Correct!')
            self._score += 1
        else:
            print(f'Wrong! The answer is {self._cc_map[self._current_country]}')
        
    def get_score(self):
        return self._score
    
    
    
        