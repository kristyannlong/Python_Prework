# KristyAnn Long


# Task 3 - Coding Questions

# •	Complete the Coding Questions below in one .py file
# •	Create an account at https://github.com/
# •	Upload this file to github.com and submit the Git repository to the google classroom assignment
# •	Watch this video walkthrough
# You will be turing in this assignment to you google classroom. 
# Please save your 5 functions to one .py file demark the question numbers 
# and the question in a comment above it's respective function


# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input 
# of the function. The first line of the code has been defined as below.
#     def hello_name(user_name):
#         .....

def hello_name(user_name):
    """Display a greeting to a user"""
    user_name = "please enter your username:  "
    user_name += "\n(enter 'q' at any time to quit)  "
    message = input(user_name)
    while message != 'q':
        print('Hello ' + message + "!")
        break
    
hello_name("")


# Question 2
# Write a python function, first_odds that prints the odd 
# numbers from 1-100 and returns nothing
#     def first_odds():
#         .....

def first_odds(odd_numbers):
    """Print a list of odd numbers between 1 and 100"""
    odd_numbers = list(range(1, 100, 2))
    print(odd_numbers)
            

first_odds(odd_numbers=1)


# Question 3
# Please write a Python function, max_num_in_list to return the max 
# number of a given list. The first line of the code has been defined as below.
#     def max_num_in_list(a_list):
#         .....

def max_num_in_list(a_list):
    """find the highest number in a list"""
    for number in a_list:
        print(max(a_list))
        break

a_list = (1, 14, 32, 99, 6, 84)
max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless 
# it is also divisible by 400. The return should be boolean Type (true/false).
#     def is_leap_year(a_year):
#         .....

def is_leap_year(a_year):
    """Checking if the given year is a leap year"""    
    if ((a_year % 400 == 0) or
        (a_year % 100 != 0) and
        (a_year % 4 == 0)):
        return True
    else:
        return False
    
a_year = int(input('Enter the year:  '))
is_leap_year(a_year)
print(is_leap_year(a_year))
 

# Question 5
# Write a function to check to see if all numbers in list 
# are consecutive numbers. For example, [2,3,4,5,6,7] are 
# consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
#     def is_consecutive(a_list):
#         .....

def is_consecutive(a_list):
    """Find out if a list of numbers is consecutive"""
    sorted_list = sorted(a_list)
    if all(sorted_list[i] == sorted_list[i-1] 
           + 1 for i in range(1, len(sorted_list))):
        return True
    else:
        return False

print(is_consecutive(a_list= (1, 2, 7, 4)))
