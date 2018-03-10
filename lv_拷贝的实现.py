# # 利用文件读写实现文件拷贝
# file_name = input("请输入备份的文件名")
# # 打开原文件
# old_f = open(file_name, "w")
# # 创建新文件
# new_file_name = "[附件]" + file_name
# new_f = open(new_file_name, "w")
# while True:
#     # 读取原文内容
#     content = old_f.readline()
#     if len(content) == 0:
#         break
#     # 内容写入新文件
#     new_f.write(content)
#
# # 关闭原文件的新文件
# old_f.close()
# new_f.close()
"""文件的读写造成的文件定位改变"""
# f = open("666.txt", "w+")
# print(f.tell())
# f.write("hello,python")
# print(f.tell())
# content = f.read()
# print("内容为：%s" % content)
# f.close()
"""文件的读取"""
# # read()函数 默认会将文件中的所有内容全部读出 一次性全部读取会出现内存峰值影响性能
# with open("123.txt", "r") as f:
#     content = f.read()
#     print(content)
#
# # read(n) 可以指定每次读出几个字符
# with open("123.txt", "r") as f:
#     content = f.read(3)
#
#
# #readline() 每次读取一行内容
# with open("123.txt", "r") as f:
#     content = f.readline()
#     content1 = f.readline()
#
#
# # 读取大型文件
# with open("123.txt", "r") as f:
#     while True:
#         content = f.readline()
#         if len(content) == 0:
#             break
#         print(content, end="")
#
#
# readlines 一次读取出全部内容 每行作为一个元素 添加到列表中
with open("123.txt", "r") as f:
    result = f.readlines()
    print(result)
""""""