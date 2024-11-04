import os
import string

def read_words(filename):
    words = list()
    filepath = os.path.join(os.path.dirname(__file__), filename)
    file = open(filepath, encoding='utf-8')
    
    for line in file:
        
        line_of_words = line.split()
        
        for word in line_of_words:
            
            word2 = word.strip(string.punctuation + string.whitespace).lower()
            words.append(word2)
        
    
    return words        
    
    

def count_only(words: list[str] , count_words: list[str]) -> dict[str, int]:
    
    province_table = {}
    
    for word in words:    
        
        if word in count_words:
            
            if word in province_table:
                province_table[word] += 1
            
            else:
                province_table[word] = 1
    
        
    return province_table 

def count_all_except(words: list[str], stopwords: list[str]) -> dict[str, int]:
    
    table = {}
    
    for word in words:
        
        if word not in stopwords:
            
            if word in table:
                table[word] += 1
            else:
                table[word] = 1 
    
    return table
    
    

def filter_hist(hist, min_count):
    temp_dict = {}
    
    for word, freq in hist.items():
        
        if freq >= min_count:
            
            temp_dict[word] = freq
    
    return temp_dict
    
        



def sorted_hist(hist: dict[str, int]) -> list[tuple[int, str]]:
    
    tuple_list = []
    
    for word, freq in hist.items():
        
        tuple_list.append((freq, word))
    
    tuple_list.sort(reverse=True)
    
    return tuple_list

# -----------------------------------------------------------



# se till att vi öppnar filen i rätt katalog (slå samman 
# katalogen som scriptet ligger i med filnamnet på textfilen)
#filepath = os.path.join(os.path.dirname(__file__), filename)

# öppna filen (utf-8 behövs för att hantera åäö rätt)
#file = open(filepath, encoding='utf-8')

# skriv ut filens innehåll
#for line in file:
#    print(line)

words = read_words('nilsholg.txt')
provinces = read_words('landskap.txt')
#hist = count_only(words, provinces)
#print(hist['skåne'])



stopwords = read_words('undantagsord.txt')
hist = count_all_except(words, stopwords)

sorted_list = sorted_hist(hist)
min_list = filter_hist(hist, 100)

print(min_list)