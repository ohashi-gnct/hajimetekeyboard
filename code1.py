import board
import time
import usb_hid
from digitalio import DigitalInOut, Pull,Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard  = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


# スイッチのピンを設定
switch_pins = [board.GP6, board.GP11, board.GP15]
switches = []
for pin in switch_pins:
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    # 内部のプルアップ抵抗を使用
    switch.pull = Pull.UP
    switches.append(switch)

# LEDのピンを設定
led_pins = [board.GP5, board.GP10, board.GP14]
leds = []
for pin in led_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    leds.append(led)

# 入力したい文字列たち
strings = ["hajimemashite", "konnnichiha", "konnbannha"]

while True:
    for switch, led, string in zip(switches, leds, strings):
        led.value = 1
        
        # switch.value == 0がスイッチが押された状態
        # スイッチが押されたとき、対応するLEDを消灯する。
        if switch.value == 0:
            keyboard_layout.write(string)
            led.value = 0
            time.sleep(0.2)
            led.value = 1

    time.sleep(0.01)