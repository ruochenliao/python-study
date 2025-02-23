try:
    print("this is try")
except:
    print("this is except")

try:
    print("this is try")
except:
    print("this is except")
finally:
    print("this is finally")

# 创建一个异常
x = -1
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print("this is except")
    print(e)

try:
    x = 1 / 0
except Exception as e:
    print(e)

# 打印堆栈
import traceback

try:
    x = 1 / 0
except Exception as e:
    print("Exception occurred:")
    traceback.print_exc()