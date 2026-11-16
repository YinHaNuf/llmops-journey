score=85   
if score>=60:
    print("及格")
else:
    print("不及格")

score=85
if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")

score = int(input("请输入分数："))

if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")

secret = "芝麻开门"
user_input= input("暗号:")

if user_input == secret:
    print("暗号正确，门已打开")
else:
    print("暗号错误，门未打开")
    