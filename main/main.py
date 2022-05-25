import board
import adafruit_lsm9ds1
from smbus2 import SMBus
import time
import datetime
from gps3 import gps3
import bme_test
import RPi.GPIO as GPIO
import config
import sys
sys.path.insert(0, "build/lib.linux-armv7l-2.7/")
import VL53L1X

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c,xg_address=0x6A,mag_address=0x1C)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()

tof.start_ranging(1)

GPIO.setmode(GPIO.BCM)             # GPIOの番号で指定
GPIO.setup(17, GPIO.OUT)           # GPIO17を出力で利用、AIN2(PWM)
GPIO.setup(22, GPIO.OUT)           # GPIO22を出力で利用、BIN2(PWM)
GPIO.setup(4, GPIO.OUT)            # GPIO4を出力で利用、AIN1(dir)
GPIO.setup(27, GPIO.OUT)           # GPIO27を出力で利用、BIN1(dir)

Apwm = GPIO.PWM(17,200)            #GPIO17を100HzのPWM出力とする
Bpwm = GPIO.PWM(22,200)            #GPIO22を100HzのPWM出力とする

def forward():                     #前進
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.HIGH)
    Apwm.ChangeDutyCycle(100)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.HIGH)
    Bpwm.ChangeDutyCycle(100)

def back():                        #後進
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.LOW)
    Apwm.ChangeDutyCycle(100)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.LOW)
    Bpwm.ChangeDutyCycle(100)

def turn_right():                  #右回転
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.HIGH)
    Apwm.ChangeDutyCycle(100)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.LOW)
    Bpwm.ChangeDutyCycle(0)

def turn_left():                   #左回転
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.LOW)
    Apwm.ChangeDutyCycle(0)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.HIGH)
    Bpwm.ChangeDutyCycle(75)

def stopping():
    Apwm.stop()
    Bpwm.stop()

while True:
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.
    print(
        "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            accel_x, accel_y, accel_z
        )
    )
    print(
        "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
    )
    print(
        "Gyroscope (rad/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            gyro_x, gyro_y, gyro_z
        )
    )
    print("Temperature: {0:0.3f}C".format(temp))
    
    [t,p,h]=readData()
    print(str(t)+":"+str(p)+":"+str(h))
    time.sleep(0.5)
    
    data_stream.unpack(new_data)
    print('time : ', data_stream.TPV['time'])
    print('lat : ', data_stream.TPV['lat'])
    print('lon : ', data_stream.TPV['lon'])
    print('alt : ', data_stream.TPV['alt'])
    print('speed : ', data_stream.TPV['speed'])
    
    distance_mm = tof.get_distance()
    print("Time: {} Distance: {}mm".format(datetime.utcnow().strftime("%S.%f"), distance_mm))
    
    time.sleep(1)
