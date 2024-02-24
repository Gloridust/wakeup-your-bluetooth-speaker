import numpy as np
import sounddevice as sd
import time

# 定义采样率和音频时长
sample_rate = 44100
duration = 1  # 1 秒钟的音频

# 生成白噪声音频
def generate_white_noise(sample_rate, duration):
    num_samples = int(sample_rate * duration)
    samples = np.random.randn(num_samples)
    samples *= 0.3  # 调整音量，以避免过于刺耳
    return samples

# 播放音频
def play_audio(samples, sample_rate):
    sd.play(samples, samplerate=sample_rate)
    sd.wait()

# 主程序
def main():
    while True:
        # 生成并播放白噪声
        noise = generate_white_noise(sample_rate, duration)
        play_audio(noise, sample_rate)
        time.sleep(5 * 60)  # 每隔 5 分钟播放一次

if __name__ == "__main__":
    main()
