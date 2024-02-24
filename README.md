# wakeup-your-bluetooth-speaker

在使用电脑连接蓝牙时，经常因为长时间无音频播放而导致蓝牙断开；我们需要使用时，却需要重新连接。

这个程序的最终目的是确保蓝牙音箱保持连接。通过定期播放微量白噪声，它模拟了活跃的音频流，以防止蓝牙音箱因为长时间没有音频流而自动断开连接。这种方法确保了蓝牙音箱的持续连接，从而提高了用户体验。

## Prepare

直接运行 Python 源代码是最被推荐的方案。你需要先执行以下代码安装依赖：

```Python
pip install numpy sounddevice tqdm
```

如果你想使用一键包，请前往[Release](https://github.com/Gloridust/wakeup-your-bluetooth-speaker/releases/).

## Release

提示：集成包体积大、打开速度慢，建议有能力使用源码的用户下载 Python 源码包
