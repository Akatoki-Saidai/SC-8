#距離が遠いとき

while now_dis>3:
  now_dis=CalculateDis()
  now_ang=CalculateAngle()
  forward()
  next_ang=CalculateAngle()
  delta_rad=next_ang-now_ang
  if delta_rad>0:
    turn_left()
  else:
    turn_right()
