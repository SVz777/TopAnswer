from lib.oneKey import OneKey

if __name__ == '__main__':
    apps=['baiwan','chongding','zhishi']
    c=int(input("1:百万英雄\n2:冲顶大会\n3:芝士超人\n"))
    print(apps[c-1])
    oneKey=OneKey(apps[c-1],1)
    oneKey.start()