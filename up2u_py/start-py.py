import os  


cmd_list = ['jupyter notebook',
'python(退出时输入 exit() )',
'python+文件'
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
else:
    os.system(cmd_list[index])