def even_or_odd(number):
    if number % 2 == 0: 
        return "Even" 
    else: 
        return "Odd" 
# Even or Odd Lesson 1 

def number_to_string(num):
    
    string_number = str(num)
    
    return string_number 
# Convert a number to a string 

def get_count(sentence):
  counter = 0
  for char in sentence: 
    if char == "a":
      counter += 1
    elif char == "e":
      counter += 1
    elif char == "i":
      counter += 1
    elif char == "o":
      counter += 1
    elif char == "u":
      counter += 1
      
  return counter 
#Vowel Count 