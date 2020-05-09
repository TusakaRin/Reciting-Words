# -*- coding: utf-8 -*-

# @Time : 2020/5/9 12:29
# @Author : yfdai


import time
import sys


animation = "|/-\\"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("End!")
