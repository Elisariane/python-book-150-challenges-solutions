# 009 Write a program that will ask for a number of days and then will show how many hours,
# minutes and seconds are in that number of days.

number_of_days = int(input("Enter with number of days \n"))
total_hours = 24 * number_of_days
total_minutes = 60 * number_of_days
total_seconds = 86400 * number_of_days
print("A", number_of_days, "days, have ", total_hours, "hours", total_minutes,
      "minutes", "and", total_seconds, "seconds")
