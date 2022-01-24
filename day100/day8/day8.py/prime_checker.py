import math

from pandas import to_datetime
num = int(input("Write a number: "))

def prime_checker():
    for each_number in range(2,num):
        if num% each_number == 0:
            to_display = "it's not a prime number"
            break
        else:
            to_display = "it is definitly prime number"    
    print(to_display)
   
    
prime_checker()