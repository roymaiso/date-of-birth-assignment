import calendar

age = int(input("Age: "))
date = int(input("Date Of Birth: "))
month = int(input("Month Of Birth: "))
current_year = int(input("Current year: "))

year_of_birth = current_year - age

day_of_birth = calendar.weekday(year_of_birth, month, date)
day_string = calendar.day_name[day_of_birth]
month_string = calendar.month_name[month]

print("You were born on " + day_string + " " + month_string + " in " + str(year_of_birth))
