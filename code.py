import board
import time
import usb_hid
from digitalio import DigitalInOut, Pull,Direction
from adafruit_hid.keyboard import Keyboard
# とりあえずUS配列前提
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# キーボードの設定を行う
keyboard  = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


# タクトスイッチのつながっているところを設定。
switch_pins = [board.GP11, board.GP12, board.GP13]
switches = []
for pin in switch_pins:
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    # 今回は抵抗を使用しないのでプルアップしておきましょう。
    switch.pull = Pull.UP
    switches.append(switch)

# タクトスイッチが押されているか視覚的にわかりやすいようにledも使う。
led_pins = [board.GP2, board.GP3, board.GP4]
leds = []
for pin in led_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    leds.append(led)

# 入力したい文字列たち
strings = ["hajimemashite", "konnnichiha", "konnbannha"]

# ここから無限ループ
while True:
    for switch, led, string in zip(switches, leds, strings):
        led.value = 1

        if switch.value == 0:
            keyboard_layout.write(string)
            led.value = 0
            time.sleep(0.2)
            led.value = 1

    time.sleep(0.01)
