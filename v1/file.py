"""
 读取文件中的数据
"""
import sys

file = None
try:
    file = open("test.py","w+")
    data = file.read()
    print(F"data:{data}")
    for r in range(10000):
        print(F"{r}")
        file.write(str(r)+'\n')
except FileNotFoundError as e:
    print(f"没有找到文件:{type(e)}")
finally:
    file.close()
    print("clear!!!")
sys.stderr.write("stderr")
sys.stdout.write("stdout")
