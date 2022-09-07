from re import I
from turtle import Turtle
import random
from ast import Break
print(">>>>>>>RANDOM NUMBER GAME<<<<<<<")
n = random.randint(0, 10)
i = 0

while i <= 1 :
 i += 1
 a = int(input("ENTER YOUR NO: "))
 
 if a == n: 
      print("CORRECT GUESS")
      break
 if a > 10 :
      
      print(" INVALID NUMBER ")
 if a > n :
     
      print("YOUR NUMBER IS GREATER")
      continue
 if a < n :
      print("YOUR NUMBER IS LESSER ")
      continue
 if i == 2 :
      print(" YOUR ATTEMPTS ARE OVER ")
      break

else:
     print("YOUR 2 ATTEMPTS ARE OVER ")

print(n)








