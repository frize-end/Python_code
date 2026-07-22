print("猜数字游戏")
import random
target=random.randint(0,100)
guess_count=0
while True:
    try:
        guess=int(input("请猜一个0~100的数字：(输入-1退出)"))
        if guess==-1:
            print("游戏结束")
            break
        guess_count+=1
        if guess==target:
            print(f"恭喜你猜对了！一共用了{guess_count}次")
            break
        elif guess<target:
            print("太小了")
        else:
            print("太大了")
    except valueError:
        print("输入类型错误！")


