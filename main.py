import numpy as np
import sounddevice as sd
import time
from tqdm import tqdm

# 定义
sample_rate = 1000  # 采样率
duration = 1  # 音频时长
total_time_sleep = 5 * 60  # 总间隔时长
sound_volume = 0.00001

# 生成白噪声音频
def generate_white_noise(sample_rate, duration):
    num_samples = int(sample_rate * duration)
    samples = np.random.randn(num_samples)
    samples *= sound_volume  # 调整音量，以避免过于刺耳
    return samples

# 播放音频
def play_audio(samples, sample_rate):
    sd.play(samples, samplerate=sample_rate)
    sd.wait()

# 主程序
def main():
    with tqdm(total=total_time_sleep) as pbar:
        while True:
            # 生成并播放白噪声
            noise = generate_white_noise(sample_rate, duration)
            play_audio(noise, sample_rate)
            
            # 更新进度条
            for _ in range(total_time_sleep // duration):
                time.sleep(duration)
                pbar.update(duration)
                if pbar.n >= total_time_sleep:
                    break

if __name__ == "__main__":
    main()
