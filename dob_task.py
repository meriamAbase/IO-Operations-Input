#  ================================== INTRO ==================================
# For this task, I am going to write a program that reads data from a text file
# called "BOB.txt".
# The file contains a list of 25 individuals with the following information:
# surname, first name, day of birth, month of birth, and year of birth.
# I am then going to create two seperate lists, one for the names and one for
# the birthdates.

# ================================ dob_task.py ================================
# First, the code is opening a file named "DOB.txt" in read mode and assigning
# it to the variable "file".
# Then, it is using list comprehension to split each line of the file into a
# list of words and storing it in the variable "line".
with open("DOB.txt", "r") as file:
    line = [content.rsplit() for content in file]

# To print out the names and birthdates of the indiviuals in two seperate lists: 

# For the names, we are iterating over each item in the "line" list and printing
# the first and second elements of each item (first name and surname).

# For the birthdates, we are iterating over each item in the "line" list and printing
# the third, fourth and fifth elements of each item (day, month and year).

# To print the heading bold, we use "\033[1m" at the start of the heading and
# "\033[0m" at the end to define an end point.
print("==============\033[1m Name \033[0m==============") 
for item in line:
    print(f"{item[0]} {item[1]}")
print("============\033[1m Birthdate \033[0m============")   
for item in line:
    print(f"{item[2]} {item[3]} {item[4]}") 
