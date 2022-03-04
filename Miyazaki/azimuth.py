import math

pi=math.py

def CalculateAngle():
  Goal_lng=a #ゴール地点の経度
  Goal_lat=b #ゴール地点の緯度
  
  gps_lat=data_stream.TPV['lat']
  gps_lng=data_stream.TPV['lon']
  
  delta_lng=Goal_lng-gps_lng
  azimuth=90-math.degrees(math.atan2(math.cos(math.radians(gps_lat))*math.tan(math.radians(Goal_lat))-math.sin(math.radians(gps_lat))*math.cos(math.radians(delta_lng))),math.sin(math.radians(delta_lng)))
  return float(azimuth)
