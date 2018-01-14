import datetime
import subprocess
import os


def backup(app):
    day,time = datetime.datetime.now().strftime("%Y%m%d:%H").split(':')
    print(day,time)
    apppath=rf"..\screen\{app}"
    filepath=rf"test_datas\{day}\{time}"
    if os.path.exists(f"{apppath}\{filepath}"):
        print("haved")
    else:
        os.makedirs(rf"{apppath}\{filepath}")
    print(rf"del {apppath}\*_*.png {apppath}\*.txt")
    subprocess.check_call(rf"del {apppath}\*_*.png {apppath}\*.txt",shell=True)
    print(rf'move {apppath}\*.png {apppath}\{filepath}')
    subprocess.call(rf'move {apppath}\*.png {apppath}\{filepath}',shell=True)
    print("ok")


if __name__ == '__main__':
    backup("zhishi")