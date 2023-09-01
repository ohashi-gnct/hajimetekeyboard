import audiocore
import audiopwmio
import board
import array
import time
import math
import analogio
from digitalio import DigitalInOut, Pull,Direction

# 1周期の方形波を作ってサンプル配列とする
def generate_sine_sample(freq):
    sr = 44100
    length = sr // freq
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        if i < (length // 2):
            sine_wave[i] = 2 ** 15 - 1
    return audiocore.RawSample(sine_wave, sample_rate=sr)

dac = audiopwmio.PWMAudioOut(board.GP22)

# 鳴らす音の周波数
tones_freq = [523, 587, 659]
# ドは 523
# レは 587
# ミは 659
# ファは 698
# ソは 784
# ラは 880
# シは 988
# 高いドは 1047

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

while True:
    for switch, led, tone_freq in zip(switches, leds, tones_freq):
        led.value = 0
        
        # switch.value == 0がスイッチが押された状態
        # スイッチが押されたとき、対応するLEDを消灯する。
        if switch.value == 0:
            dac.play(generate_sine_sample(tone_freq), loop=True)
            led.value = 1
            time.sleep(0.35)
            dac.stop()
            led.value = 0

    time.sleep(0.01)
