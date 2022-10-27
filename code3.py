# ここにコードを書いてね :-)
import audiocore
import audiopwmio
import board
import array
import time
import math
import analogio

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
tones_freq = [523, 587, 659, 698, 784, 880, 988, 1047]

# 音階のしきい値 近いほど高い音
adc_thresholds = [13000, 13300, 13800, 14600, 15500, 18000, 38000, 65535]

# 無音になるしきい値
adc_threshold_stop = 12000
adc = analogio.AnalogIn(board.A1)

while True:
    for freq, threshold in zip(tones_freq, adc_thresholds):
        if adc.value < adc_threshold_stop:
            dac.stop()
            time.sleep(0.1)
            break
        
        elif adc.value < threshold:
            dac.play(generate_sine_sample(freq), loop=True)
            time.sleep(0.1)
            break
    
    

