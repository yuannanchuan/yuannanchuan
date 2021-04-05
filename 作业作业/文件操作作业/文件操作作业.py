"""
1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表有哪些key-value），格式如下：



person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]

ps:其它是指同学们自行补充哈，与第一个字典的key一样，值不一样。

创建一个txt文本文件，来添加数据

a.第一行添加如下内容：

name,age,gender,hobby,motto


b.从第二行开始，每行添加具体用户信息，例如：

yuze,17,男,假正经, I am yours

cainiao,18,女,看书,Lemon is best!
"""


person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,
               {"name":"哈哈", "age": 29, "gender": "女", "hobby": "真正经", "motto": "我喜欢学习"}]

fs = open("py37期文件作业呀.txt", "w", encoding="utf-8")
fs.write("name,age,gender,hobby,motto\n")
for person_dict in person_info:
    fs.write(f"{person_dict['name']}, {person_dict['age']},{person_dict['gender']},"
             f"{person_dict['hobby']}, {person_dict['motto']}")
    fs.write("\n")

fs.close()

"""
mylist = []

fs = open("数据路径作业.txt", encoding="utf-8")
for line_data in fs.readlines():
    line_data = line_data.strip("\n")
    print(line_data)
    part_data_list = line_data.split("@")
    print(part_data_list)
    new_dict = {}
    for data in part_data_list:
        temp_list = data.split(":")
        new_dict[temp_list[0]] = temp_list[1]
    print(new_dict)
    mylist.append(new_dict)

print("列表内容", mylist)

"""











