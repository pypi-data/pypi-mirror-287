'''
# V0.3
* 增加连接机制
# V0.2
* 解决STOP格物BUG
# V0.1
* 初始化BLE任务
'''
from threading import Thread
import time
import asyncio
from bleak import BleakClient
from bleak import BleakScanner
import socket
import queue
import random

ble_queue = queue.Queue(512)
ble_connect_flag = 0

ble_Client = 0

# 蓝牙设备的MAC地址
DEVICE_ADDRESS = "a4:c1:38:f4:bd:f4"
# 写数据的UUID
SERVICE_WRITE_UUID = "0000fff6-0000-1000-8000-00805f9b34fb"
# 接收通知的UUID
SERVICE_NOTIFY_UUID = "0000fff6-0000-1000-8000-00805f9b34fb"

# 记录数据
watchData = []

sock = 0
socket_data = 0
socket_addr = 0

stop_gewu_flag = 0

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def disconnected_callback(client):
    #print("Disconnected callback called!")
    pass

'''
Date: 2024-02-21 18:15:26
author: zjs
description: 校验端口是否被占用
'''
def checkPort(port, host='localhost'):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except Exception as e:
        e
        return False
    finally:
        s.close()

'''
Date: 2024-02-21 18:24:21
author: zjs
description: 随机生成一个端口
'''

def randomPort():
    global UDP_PORT
    port = random.randint(10000, 49000)
    UDP_PORT = port

    return port if not checkPort(port) else randomPort()


async def ble_main(address):
    global ble_Client,ble_connect_flag,sock,socket_addr,stop_gewu_flag
    par_device_addr = address
    #device = await BleakScanner.find_device_by_address(
    # device = await BleakScanner.find_device_by_name(
    #     par_device_addr,timeout = 3, cb=dict(use_bdaddr=True)  #use_bdaddr判断是否是MOC系统
    # )
    devices = await BleakScanner.discover(timeout = 3, cb=dict(use_bdaddr=True))
    device = None
    for key in devices:
        if key.name==par_device_addr:
            device = key
    if device is None:
        print("正在扫描请稍后 "+ par_device_addr)
        time.sleep(1)
        return

    async with BleakClient(device) as client:
        try:
            # 是否连接
            if not client.is_connected:
                client.connect()
            if not client.is_connected:
                return
            #print(f"Connected: {client.is_connected}")
            ble_Client = client
            # 是否配对
            # paired = await client.pair(protection_level=1)
            #print(f"Paired: {paired}")

            # if paired:

            # 开启通知的接收
            #print('w')

            await client.start_notify(SERVICE_NOTIFY_UUID, notify_callback)
            #print('e')
            await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x03).encode("utf-8"))
            await asyncio.sleep(0.1)
            await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x06).encode("utf-8"))
            await asyncio.sleep(0.1)
            print("蓝牙连接成功!")
            print("BLE PORT:"+ str(UDP_PORT)+ "BLE PORT END")
            try:
                sent = sock.sendto(chr(0xfe).encode("utf-8"), socket_addr)
            except Exception as e:
                pass
            await asyncio.sleep(0.1)
            ble_connect_flag = 1
            # 循环发送指令
            while client.is_connected:
                n = ble_queue.qsize()
                if n > 0:
                    try:
                        # print(n)
                        watchData = []
                        if n > 32:
                            n = 32
                        for i in range(n):
                            watchData.append(ble_queue.get())
                        await client.write_gatt_char(SERVICE_WRITE_UUID,bytes(watchData),response=False)
                    except:
                        pass
                    finally:
                        pass
                await asyncio.sleep(0.02)
                if stop_gewu_flag == 1:
                    stop_gewu_flag = 0
                    await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x03).encode("utf-8"))
                    await asyncio.sleep(0.01)
                    await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x06).encode("utf-8"))
                    await asyncio.sleep(0.01)
                if ble_connect_flag == 0:
                    print("unpair")
                    await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x03).encode("utf-8"))
                    await asyncio.sleep(0.01)
                    await client.write_gatt_char(SERVICE_WRITE_UUID, chr(0x06).encode("utf-8"))
                    await asyncio.sleep(0.01)
                    await client.unpair()
                    await client.disconnect()
                #     while not client.is_connected and ble_connect_flag == 0:
                #         print("wait unpair")
                #         time.sleep(1)
                    break
                        #await client.disconnect()
            #print('Disconnected')
            print('蓝牙连接已断开！')
            try:
                sent = sock.sendto(chr(0xff).encode("utf-8"), socket_addr)
            except Exception as e:
                pass
        except Exception as e:
            print("异常1")
            print(e)
            # await client.unpair()
        finally:
            # # 结束监听
            await client.stop_notify(SERVICE_NOTIFY_UUID)
            await client.unpair()
            # print('2456456')
            # 断开与蓝牙设备的连接
            await client.disconnect()
            print("结束")


count = 0
# 回调监听
def notify_callback(sender, data):
    global socket_addr,count
    try:
        #recv_data_handler(data)
        sent = sock.sendto(data, socket_addr)
        count = count + 1
        if count > 20:
            print('$$jump_ble$$')
            count = 0
    except Exception as e:
        #print("异常2")
        pass

def ble_service(address):
    while True:
        try:
            asyncio.run(ble_main(address))
        except:
            time.sleep(1)

def ble_service_name(name):

    while True:
        try:
            asyncio.run(ble_main(name))
        except:
            time.sleep(1)

def hex2str(n):
    if n >=0 and n<=9:
        return 0x30 + n
    else:
        return 0x41+ (n-0x0A)

def start_udp_server():
    global socket_addr,stop_gewu_flag
    while True:
        try:
            socket_data, socket_addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            if len(socket_data) == 2 and socket_data[0] == 0x03 and socket_data[1] == 0x06:
                stop_gewu_flag = 1

            for i in range (len(socket_data)):
                #print(socket_data[i])
                ble_queue.put(hex2str(socket_data[i]>>4))
                ble_queue.put(hex2str(socket_data[i]&0x0f))
        except Exception as e:
            pass


def open_gewu_ble_name(address):
    global com_connect_flag,ble_connect_flag,sock
    randomPort()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print("UDP Receiver started...")

    th = Thread(target=ble_service,args=(address,))
    th.start()

    t2 = Thread(target=start_udp_server)
    t2.start()

    com_connect_flag = 0
    #write_config(address)
    while True:
        time.sleep(0.1)
        if ble_connect_flag == 1:
            time.sleep(0.1)
            break

import platform

currentOs = platform.system()

'''
Date: 2024-03-26 16:55:17
author: zjs
description: 获取本机ip
'''
def getCurrentIp():
    s = None
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        if s is not None:
            s.close()

    return ip


'''
Date: 2024-03-26 16:55:17
author: zjs
description: 获取内网ip.用于绑定 udp
'''
def getHostIp():
    if currentOs == 'Windows':
        return getCurrentIp()
    elif currentOs == 'Darwin':
        return '0.0.0.0'


CLEARGC_UDP_PORT = 26485
BROADCAST_ADDRESS = getHostIp()
CLOSE_MESSAGE = 'CLOSE'

'''
Date: 2024-07-23 16:51:24
author: zjs
description: udp 广播端口是否被占用
'''


def isPortInUse():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.bind((BROADCAST_ADDRESS, CLEARGC_UDP_PORT))
            s.close()
            return False
        except OSError:
            return True
'''
Date: 2024-07-23 16:55:23
author: zjs
description: 监听udp 广播
param {*} port
'''
def startUdpListener():
    global ble_connect_flag
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((BROADCAST_ADDRESS, CLEARGC_UDP_PORT))
            while True:
                data, addr = s.recvfrom(1024)
                result = data.decode()
                print(f"接收'{result}' 来自 {addr}")
                if result == CLOSE_MESSAGE:
                    # 在这里处理你得蓝牙结束
                    ble_connect_flag = 1
                    time.sleep(0.4)
                    exit(0)

    except Exception as e:
        # print(e)
        ble_connect_flag = 1
        time.sleep(0.4)
        exit(0)

'''
Date: 2024-07-23 17:01:53
author: zjs
description: 关闭历史udp服务 并处理蓝牙缓存
'''
def restartUdpAndClearGc():
    # 如果被占用 广播一下让他关闭
    if isPortInUse():
        print("有历史进程未关闭")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(CLOSE_MESSAGE.encode(), (BROADCAST_ADDRESS, CLEARGC_UDP_PORT))
            print(f"发送'{CLOSE_MESSAGE}' 给 {CLEARGC_UDP_PORT}")
        time.sleep(1)

    # 重新开始监听
    startUdpListener()

Thread(target=restartUdpAndClearGc).start()
