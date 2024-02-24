import numpy as np
import sounddevice as sd
import time

# 定义
sample_rate = 1000  # 采样率
duration = 1  # 音频时长
total_time_sleep = 5 * 60  # 总间隔时长
sound_volume = 0.000001

# 打包用户交互模块
def user_interaction():
    print(">当前参数定义如下：")
    print(f">采样率：{sample_rate}")
    print(f">音频时长：{duration}")
    print(f">总间隔时长（分钟）：{total_time_sleep / 60}")
    print(f">音量调节：{sound_volume:.10f}".rstrip('0').rstrip('.'))

    try:
        user_input = input("\n>输入间隔分钟数，直接按下Enter 则使用默认值[5min]:")
        if user_input:
            new_total_time_sleep = int(user_input) * 60
            print(f">总间隔时长已更改为 {user_input} 分钟")
            return new_total_time_sleep
        else:
            print(">使用默认参数执行")
            return total_time_sleep
    except ValueError:
        print(">输入无效，使用默认参数执行")
        return total_time_sleep

# 生成白噪声音频
def generate_white_noise(sample_rate, duration):
    num_samples = int(sample_rate * duration)
    samples = np.random.randn(num_samples)
    samples *= sound_volume  # 调整音量
    return samples

# 播放音频
def play_audio(samples, sample_rate):
    sd.play(samples, samplerate=sample_rate)
    sd.wait()

# 主程序
def main():
    num_run = 0
    new_total_time_sleep = user_interaction()
    print(">开始运行")
    while True:
        # 生成并播放白噪声
        noise = generate_white_noise(sample_rate, duration)
        play_audio(noise, sample_rate)
        
        # 状态显示
        num_run += 1
        print(f"\r>已唤醒蓝牙音响{num_run}次，正在等待下一次唤醒...",end="")

        # 延迟等待
        time.sleep(new_total_time_sleep)

if __name__ == "__main__":
    main()
