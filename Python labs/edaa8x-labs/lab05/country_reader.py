import csv


def read_from_file(filename):
    result_map = {}
    
    with open(filename, "r", newline = "") as csv_file:
        for line in csv.DictReader(csv_file):
            result_map[line.get("Country")] = line.get("Capital")
    
    
    return result_map






        
        
        