# *__coding: UTF-8__*
import socket
import uuid
def getinfo():
    myip=socket.gethostbyname(socket.gethostname())
    print("本机IP地址是：:"+myip)
    node=uuid.getnode()
    mac=uuid.UUID(int=node).hex[-12:]
    print("本机Mac地址是："+mac)
