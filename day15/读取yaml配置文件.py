
"""
1、第三方库：pyyaml模块
2、安装：pip install pyyaml

3、从yaml文件读取数据只有3步：
     3.0  引入yaml: import yaml
      3.1  打开yaml文件: open函数
      3.2  调用yaml.load加载文件对象，为python对象。

    示例：
    fs = open(yaml文件路径,encoding="utf-8")
    s = yaml.load(fs,yaml.FullLoader)
"""

import yaml
with open("conf.yaml", encoding="utf-8") as fs:
    s = yaml.load(fs, yaml.FullLoader)
    print(s)

