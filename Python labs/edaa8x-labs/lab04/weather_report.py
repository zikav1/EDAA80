from pathlib import Path
import file_reader 
import weather_functions as wf


# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'


n = int(input('What do you want to do? Press 1 for average temperature, 2 for when spring comes and 3 to find min and max temperature for a specific month'))

if n == 1:
    month = int(input('For what month do you want to calculate the average temperature?'))
    avg_temp_list = file_reader.read_from_file(file_path, month)
    
    print(f'Average temperature during month {month} was {wf.calculate_avg_temp(avg_temp_list)}')

elif n == 2:
    spring_temp_list = file_reader.read_from_file(file_path, 0)
    
    print('Looking for spring...')
    print(f'Spring comes during month {wf.when_is_spring(spring_temp_list)}')

elif n == 3:
    month = int(input('For what month do you want to find min and max temperature?'))
    min_max_list = file_reader.read_from_file(file_path, month)
    
    min_temp = min(min_max_list)
    max_temp = max(min_max_list)
    
    print(f'For month {month} the min temperature is {min_temp} and max temperature {max_temp}')

else:
   raise Exception('Not a valid option')
    
    











