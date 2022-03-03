#距離を出す

import math

pi=math.pi

Goal_lat=a #ゴール地点の経度（決まったら入れる）
Goal_lng=b #ゴール地点の緯度（決まったら入れる）

gps_lat=data_stream.TPV['lat']
gps_lng=data_stream.TPV['lon']

delta_lng=Goal_lng-gps_lng
omega=math.acos(math.sin(gps_lat*2*pi/360)*math.sin(Goal_lat*2*pi/360)+math.cos(gps_lat*2*pi/360)*math.cos(Goal_lat*2*pi/360)*math.cos(delta_lng*2*pi/360))

def CalculateDis():
    return 6378.137*10**3*omega
    
