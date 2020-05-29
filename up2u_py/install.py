import os
import sys
import requests
from bs4 import BeautifulSoup

url_miniconda = 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/'
html = requests.get(url_miniconda).content
# print(html)

html = BeautifulSoup(html, 'html.parser')
# print(html)

tr_list = html.find_all('tr')
# print(tr_list[:10])

latest = []
for tr in tr_list:
    a = tr.find('a')
    if 'Miniconda3-latest' in a.text:
        latest.append(a.text)
        

# print(latest)

for index, mini in enumerate(latest):
    print(index+1, mini)

choose = input("""
>> 你想选择哪个版本(选择数字)？
注意：
- 按系统选择，Windows选择带Windows的，Mac选择带mac的，其他选Linux
- 注意系统位数，64位选择带x86_64的，32位系统选择x86的
""")
print(f'== 你选择的版本是：{latest[int(choose)-1]}')

print('-->>>开始下载...')

name = latest[int(choose)-1]
with open(name, 'wb') as f:
    f.write(requests.get(f'{url_miniconda}{name}').content)

print('下载完成!')

# TODO： 如果下载失败，直接到qq群里下载

WINDOWS = sys.platform.startswith("win") or (sys.platform == "cli" and os.name == "nt")

install = input('>> 是否开始安装（y/n）？')
if install.lower() == 'y':
    if not WINDOWS:
        print(f'执行命令：sh {name}')  # for *nix
        # os.system(f'sh {name}')
    # TODO: for windows
    else:
        os.system(f'open {name}')
else:
    print('下次再说')

print('开始自动安装jupyter')
os.system('pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple')

print('----现在去打开 start-py 程序，开始写代码----')

exit()


