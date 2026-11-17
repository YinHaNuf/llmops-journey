# 1.9 异常处理 —— 安全计算器

while True:
    cmd = input("输入算式（如 10/2）或 q 退出：")
    if cmd == "q":
        break
    try:
        x, op, y = cmd.split()
        x, y = int(x), int(y)
        if op == "+":
            r = x + y
        elif op == "-":
            r = x - y
        elif op == "*":
            r = x * y
        elif op == "/":
            r = x / y
        else:
            r = "不支持的运算符"
    except ValueError:
        r = "格式错了，写成 10 / 2 这样"
    except ZeroDivisionError:
        r = "不能除以零"
    print(r)