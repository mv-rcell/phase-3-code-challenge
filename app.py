def add_numbers(num1,num2):
    return num1 + num2

def is_even(number):
     return number % 2 == 0: True
      
def reverse_string(text):
    return text[::-1]

def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count
    
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def apply_decorator (func):
   return decorator_func(func)

def decorator_func(func):
    def color(red,blue):
       print("Decorator Applied")
       return func(red,blue)
    return (color)

def sort_by_age (people)
  return sorted_(people, key=lambda person: person[1])



def merge_dicts("dictionary 1","dictionary 2")
     merged_dictionary = {}

for key,value in dictionary1.items():
   if key in merged_dictionary:
      merged_dictionary[key] += value
    else:
      merged_dictionary[key] = value

for key,value in dictionary2.items():
   if key in merged_dictionary:
      merged_dictionary[key] += value
    else:
      merged_dictionary[key] = value

 return merged_dictionary


class Car :
    def_init_(self,make,model, yesr):
         
         self.make = make
         self.model = model
         self.year = year
    
    def display_info(self):
       
       print(f"Make: {self.make}")
       print(f"Model: {self.model}")
       print(f"Year: {self.year}")
       












