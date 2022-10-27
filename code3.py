import audiocore
import audiopwmio
import board
import array
import time
import math

# 1周期のサイン波を作ってサンプル配列とする
def generate_sine_sample(freq):
    sr = 44100
    length = sr // freq
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        if i < (length // 2):
            sine_wave[i] = 2 ** 15 - 1
    return(audiocore.RawSample(sine_wave, sample_rate=sr))

dac = audiopwmio.PWMAudioOut(board.GP22)
tones_freq = [523, 587, 659, 698, 784, 880, 988, 1047]

while True:
    for freq in tones_freq:
        dac.play(generate_sine_sample(freq), loop=True)
        time.sleep(0.5)
        
        