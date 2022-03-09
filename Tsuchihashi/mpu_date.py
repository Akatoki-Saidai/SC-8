import FaBo9Axis_MPU9250
import time

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

def write_csv(accel,gyro,magnet):
	dt_now = datetime.datetime.now()
	with open('mpu_date.csv','a') as f:
		f.write(dt_now.strftime('%Y/%m/%d %H:%M:%S') + "," + str(accel) + "," + str(gyro) +","+str(magnet)+"\n")


setup()
get_calib_param()

print("データ取得を開始します")

if __name__ == '__main__':
	try:
		while True:
			accel = mpu9250.readAccel()
            print('accel:' + str(accel))
            gyro = mpu9250.readGyro()
            print('gyro:' + str(gyro))
            magnet = mpu9250.readMagnet()
            print('magnet:' + str(magnet))
			print(str(t)+":"+str(p)":"+str(h)+"\n")
			write_csv(accel,gyro,magnet)
			time.sleep(1)
	except KeyboardInterrupt:
		print("処理を中止")
