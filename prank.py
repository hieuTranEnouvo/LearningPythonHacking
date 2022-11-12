import random
import string
import time

import pyautogui as py

characters = string.ascii_letters
length = 10
number = input("No of messages: ")

for i in range(int(number)):
    output = "".join(random.sample(characters, length))
    py.typewrite(output)
    py.press('Enter')
    time.sleep(2)
