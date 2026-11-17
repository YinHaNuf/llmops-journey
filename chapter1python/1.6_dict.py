""" scores = {}

while True:
    cmd=input("查/加/全部/退出：")
    if cmd=="加":
        name = input("姓名：")
        score=input("成绩：")
        scores[name]=score
    elif cmd=="查":
        name=input("姓名：")
        print(f"{name}:{scores.get(name,'没有这个人')}")
    elif cmd=="全部":
        for k,v in scores.items():
            print(f"{k}->{v}分")
    elif cmd =="退出":
        break
 """

text = "apple banana apple orange banana apple"
print(text.split( ))
apple =0
banana=0
orange=0
for fruit in text.split( ):
    if fruit=='apple':
        apple+=1
    elif fruit=='banana':
        banana+=1
    elif fruit=='orange':
        orange+=1
print(f"apple:{apple},banana:{banana},orange:{orange}")