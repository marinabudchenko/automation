def is_year_leap (number):

    return True if number % 4 == 0 else False 

year_to_choice = 2024

result = is_year_leap (year_to_choice)

print (f"Год {year_to_choice}: {result}")
