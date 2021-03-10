import os
import random
import string


cmd = input("Enter the cmd name: ")

for old in os.listdir(f'./{cmd}/'):
    new = ''.join(random.choices(string.ascii_uppercase, k = 7))
    os.rename(f"./{cmd}/{old}", f"./{cmd}/{new}.gif")