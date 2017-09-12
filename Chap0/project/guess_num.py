# coding:utf-8

from random import randint

print("这是一个猜数字游戏")
print("游戏规则")
print("""
- 程序随便生成一个二十以内的数字，用户有 10 次机会猜测
- 程序根据用户输入，给与一定提示（大了、小了、正确)
- 猜对或者用完 10 次机会，游戏结束""")


code = randint(1, 20)
guess = int(input("请输入数字："))
guesses = 1 

print("你还有 9 次机会")
if guess == code:
    print("正确")
    
elif guess > code:
    print("大了")
    
elif guess < code:
    print("小了")

            
              
while guess != code and guesses < 10:
    
    guesses += 1
    guess = int(input("请输入数字："))
    time = 10 - guesses 
    print("你还有 %d 次机会 " % time)
       
    if guess == code:
        print("正确")
        print("游戏结束")
    
    elif guess >  code:
        print("大了")
    
    elif guess < code:
        print("小了")
            
if guess != code:
    print("游戏结束")
            

            
        
           

            
               


