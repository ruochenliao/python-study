# read
f = open("demofile.txt", "r")
print(f.read())
f.close()

# write
"""
"w" - Write - will overwrite any existing content
"""
f = open("demofile.txt", "w")
f.write("\nNow the file has more content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())

"""
"a" - Append - will append to the end of the file
"""
f = open("demofile.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())

# delete
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

f = open("demofile.txt", "w")
f.write("hello world\n who are you\n")
f.close()


# with 语句
"""
使用 with 语句进行文件操作是一种推荐的做法，因为它可以确保文件在使用完毕后自动关闭，
即使在处理文件的过程中发生了异常。
with 语句会创建一个上下文管理器，负责在进入和退出时执行特定的操作。
"""
with open("demofile.txt", "r") as f:
    print(f.read())