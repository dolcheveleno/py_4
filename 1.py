# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls')

from hashlib import new
from ntpath import join

line = 'олрабв читсм абвопьп мгнеп попабвщршр мтпо'
print(line)
str = line.split() 
print(str)
for elem in str:
    if elem.find('абв') != -1:
        str.remove(elem) 
print(str)            
newline = ' '.join(str) 
print(newline)    