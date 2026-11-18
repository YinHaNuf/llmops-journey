import os, sys, json
from pathlib import Path
from datetime import datetime
import random

# 试一段：
print("当前目录：", os.getcwd())
print("Python 版本：", sys.version)
print("今天是：", datetime.now().strftime("%Y-%m-%d"))
print("随机数：", random.randint(1, 100))