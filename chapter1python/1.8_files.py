scores = [85, 92, 78]

# 写 —— 每个数字一行
with open("scores.txt", "w", encoding="utf-8") as f:
    for s in scores:
        f.write(str(s) + "\n")    # str() 把数字转字符串

# 读 —— 读回来求和
total = 0
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        total = total + int(line.strip())

print(total)   # 255