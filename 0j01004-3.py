"""
プログラムを起動すると赤色信号が点灯し、SW1を押すと2秒後に赤色信号が消灯し、青色信号が点灯する。
さらに、5秒後に点滅に変わり、その後赤に変わる。
青色信号が点灯したと同時に歩行者誘導音がなり、2秒後に「間も無く信号が赤になります」と発話させる。
"""

import RPi.GPIO as GPIO
import time
import pygame.mixer

# GPIOsetup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

def lanp_main():
    # 赤色を点灯
    ledlanp_on()
    # SW1を押すと2秒後に赤色が消灯し、青色が点灯
    if GPIO.input(SW1) == 1:
        time.sleep(2)
        ledlanp_off()
        bluelanp_on()
        # ここに歩行者誘導音
        time.sleep(2)
        # ここに間も無く信号が赤になりますアナウンス
    time.sleep(5)

def lanp_flash():
    # 5秒後に点滅に変わる
    count = 0

    while count == 3:
        bluelanp_off()
        time.sleep(1)

        bluelanp_on()
        time.sleep(1)
        count = count + 1

# 赤色ランプ点灯関数
def ledlanp_on():
    return GPIO.output(LED1, GPIO.HIGH)
# 赤色ランプ消灯関数
def ledlanp_off():
    return GPIO.output(LED1, GPIO.LOW)
# 青色ランプ点灯関数
def bluelanp_on():
    return GPIO.output(LED2, GPIO.HIGH)
# 青色ランプ消灯関数
def bluelanp_off():
    return GPIO.output(LED2, GPIO.LOW)

def flow():
    lanp_main()
    lanp_flash()

if __name__ == '__main__':
    flow()
