from pathlib import Path 
import country_reader
import capital_game_logic

# Reading the countries and their respective capitals
file_path = Path(__file__).parent / 'european_capitals_full.csv'
cc = country_reader.read_from_file(file_path)

game = capital_game_logic.CapitalGame(cc)


game.start_game()
    
    
    
    
    