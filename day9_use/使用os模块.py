
"""
listdir

1.移植性:
    路径可能找不着 把代码扔到其他电脑上
    跨平台支持不友好 Windows Linux 路径表达

相对路径 - 代码里不出现绝对路径
1.动态获取当前文件的绝对路径 - os.path.abspath(__file__)
2.动态获取所给目录/文件  所在目录
3.动态拼接路径(根据操作系统处理路径拼接符 - win \ liunx /) - os.path.join(顶级目录,要追加到顶级目录之后的目录)
"""

import os
"""
basedir = r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川"
files = os.listdir(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川")
print(files)

# 怎么拼接路径

for file in files:
    print(basedir + "\\" + file)

"""

# 动态获取当前文件的绝对路径  -
file_full_path = os.path.abspath(__file__)
print(file_full_path)

# 2.动态获取所给目录/文件  所在目录
file_dir = os.path.dirname(file_full_path)
print(file_dir)

file_dir = os.path.dirname(file_dir)
print(project_dir)

# 3.得到需要已知目录文件名称
new_path = os.path.join(project_dir,"导包讲解")
print(new_path)

new_path = os.path.join(project_dir,"导包讲解", "kedaibiao.py")
print(new_path)

