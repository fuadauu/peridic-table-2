from mimetypes import guess_all_extensions
import random
n= random.randint(1,10)
attempts=4
print("welcome to the game")
print("i am tinkig of a nuber between 1 and 10")
while attempts > 0 :
    guess=int(input("enter a guess"))
    if guess==n:
     print("congra you have got the number")
     break
    elif guess<n:
     print("too low")
    else:
     print("too high")
    attempts-=1
    if attempts==0:
     print("you have lost the game")
     print("the number was",n)