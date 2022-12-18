import sys
from logg import logging

num_1 = 0
num_2 = 0

def init(a,b):
    global num_1
    global num_2 
    num_1 = a
    num_2 = b   

def do_it ():
    if num_2 !=0:
        return num_1 / num_2
    else:
        logging.warning("Error! Division by zero")
        sys.exit("Ошибка! деление на ноль!")
