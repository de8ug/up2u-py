# start-py.py
# python运行程序
# @author: DE8UG
# @公众号：Python随身听
# @官网：https://de8ug.vip/
# 
import os  


cmd_list = ['jupyter notebook',
'python(退出时输入 exit() )',
'python+文件',
'安装python第三方代码库'
]

for index, cmd in enumerate(cmd_list):
    print(index+1, cmd)

cmd = input('选择命令 （输入数字）：')

index = int(cmd)-1
print(f'你选择的是：{cmd_list[index]}')

if index == 1:
    os.system('python')
elif index == 2:
    py_file = input('直接把Python代码文件拖到当前控制台(然后按回车)\n')
    print(f'python {py_file}')
    os.system(f'python {py_file}')
elif index == 3:
    name = input('输入代码库名字，按回车：')
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {name}')
else:
    os.system(cmd_list[index])

input('任意键退出')