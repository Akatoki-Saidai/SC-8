import RPi.GPIO as GPIO
import config
import time

GPIO.setmode(GPIO.BCM)             # GPIOの番号で指定
GPIO.setup(17, GPIO.OUT)           # GPIO17を出力で利用、AIN2(PWM)
GPIO.setup(22, GPIO.OUT)           # GPIO22を出力で利用、BIN2(PWM)
GPIO.setup(4, GPIO.OUT)            # GPIO4を出力で利用、AIN1(dir)
GPIO.setup(27, GPIO.OUT)           # GPIO27を出力で利用、BIN1(dir)

Apwm = GPIO.pwm(17,100)            #GPIO17を100HzのPWM出力とする
Bpwm = GPIO.pwm(22,100)            #GPIO22を100HzのPWM出力とする

def forward():                     #前進
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.HIGH)
    Apwm.ChangeDutyCycle(75)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.HIGH)
    Bpwm.ChamgeDutyCycle(75)

def back():                        #後進
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.LOW)
    Apwm.ChangeDutyCycle(75)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.LOW)
    Bpwm.ChamgeDutyCycle(75)

def turn_right():                  #右回転
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.HIGH)
    Apwm.ChangeDutyCycle(75)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.HIGH)
    Bpwm.ChamgeDutyCycle(0)

def turn_left():                   #左回転
    Apwm.start(0)                  #右車輪
    GPIO.output(4,GPIO.HIGH)
    Apwm.ChangeDutyCycle(0)
    Bpwm.start(0)                  #左車輪
    GPIO.output(27,GPIO.HIGH)
    Bpwm.ChamgeDutyCycle(75)

def stopping():
    i = 0
    while(75-i >= 0):
        Apwm.start(0)                  #右車輪
        GPIO.output(4,GPIO.HIGH)
        Apwm.ChangeDutyCycle(75-i)
        Bpwm.start(0)                  #左車輪
        GPIO.output(27,GPIO.HIGH)
        Bpwm.ChamgeDutyCycle(75-i)
        time.sleep(0.5)
        i = i - 5
    else:
        Apwm.stop()
        Bpwm.stop()

while(1):
    act=input("処理を入力>>>")
    if act=="f":
        print("forward")
        print("何秒前進しますか？")
        while(1):
            sec=input("秒数を入力>>>")
            if sec.isdecimal():
                sec=float(sec)
                print(f'{sec}{"秒前進します"}')
                forward()
                time.sleep(sec)
                stopping()
                break
    elif act=="b":
        print("back")
        print("何秒後進しますか？")
        while(1):
            sec=input("秒数を入力>>>")
            if sec.isdecimal():
                sec=float(sec)
                print(f'{sec}{"秒後進します"}')
                back()
                time.sleep(sec)
                stopping()
                break
    elif act=="r":
        print("turn right")
        print("何秒右回転しますか？")
        while(1):
            sec=input("秒数を入力>>>")
            if sec.isdecimal():
                sec=float(sec)
                print(f'{sec}{"秒右回転します"}')
                turn_right()
                time.sleep(sec)
                stopping()
                break
    elif act=="l":
        print("turn left")
        print("何秒左回転しますか？")
        while(1):
            sec=input("秒数を入力>>>")
            if sec.isdecimal():
                sec=float(sec)
                print(f'{sec}{"秒左回転します"}')
                turn_left()
                time.sleep(sec)
                stopping()
                break
    elif act=="c":
        print("cancel")
        print("プログラムを終了します")
        GPIO.cleanup()
    else:
        print("有効な文字が入力されていません")
