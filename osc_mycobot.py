from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pythonosc import dispatcher
from pythonosc import osc_server
import threading

received_data = 0

def handle_unity_data(unused_addr, args, data):
    global received_data
    received_data = data
    print(received_data)

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/unity", handle_unity_data, "Data")

ip = "192.168.50.246"
port = 2929

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
print("Serving on {}".format(server.server_address))
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()



# 角度パターンの設定
p_angles = [
    [-75, 43, 86, -35, -170, 0]
    [-7, 82, 70, -74, -170, 0]
    [24, 70, 87, -84, -166,36]
    [20, 86, 43, -58, -163, 36]
]

def mycobot_code():
    global received_data  # グローバル変数を使用

    num_target = received_data - 1
    print("Received", num_target)

    # MyCobotの初期設定
    mc = MyCobot('/dev/ttyAMA0', 1000000)

    # 初期角度、クッションの差、スピードの設定
    start_angles = [0, 30, 0, 0, -170, 90]
    dc_angles = 50  # Difference of cushion
    rl_speed = 100  # Release speed
    df_speed = 80   # Default speed
    c_speed = 100    # Cushion speed

    re_num = 2
    def func(angles, dc):
        new_angles = angles.copy()
        new_angles[3] -= dc
        return new_angles

    #patten = re.compile
    serve_p_angles = p_angles[num_target].copy()
    p_angles_pre = [func(agl, dc_angles) for agl in serve_p_angles]

    print(serve_p_angles)
    print(p_angles_pre)


mycobot_thread = threading.Thread(target=mycobot_code)
mycobot_thread.start()

# 角度のクッションを考慮して新しい角度リストを作成 

