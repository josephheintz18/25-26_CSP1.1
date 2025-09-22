# import the datetime module to get the current date/year
import datetime as dt

# ask user for their name then welcome them
print("Welcome to the not so new year")
user = input("What is your name")
print("HOWDY HO", user, "welcome to THE program LEAVE NOW LEAVE! Just kidding you gotta stay")

# ask user for their age
age = input("How old are you?")

# get the current year using the datetime object that resides in the datetime module
curr_year = dt.datetime.now().year

# prepare and display output
birth_year = curr_year - int(age)
print("Hmmm... were you born in", birth_year, ".")