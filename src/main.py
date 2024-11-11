from gpiozero import Motor  # gpiozeroモジュールを使用
import time


hane_motor = Motor(23, 24) # ハネの制御
sorenoido_motor = Motor(16, 20) # 射出用ソレノイド
meta_motordriver = Motor(19, 26) # モータードライバーを操作するモータードライバー
meta_motordriver.forward(1)

def main():
    pass