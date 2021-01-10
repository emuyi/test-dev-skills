#### 其他 desired_caps

https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md

```python
# 测试策略相关的
  udid： 指定设备执行(SN)
  avd：指定要launch的 avd 【自动启动指定的avd】
  noReset:默认 false (stop, clear, but dont uninstall)
  dontStopAppOnReset: 默认 false 本质就是 am start 的时候要不要加 -S
  fullReset:如果为 True(stop, clear, and uninstall)
  chromedriverExecutable：写死 chromedriver.exe 路径
  chromedriverExecutableDir：chromedriver.exe 所在的目录，appium会自动找合适的版本
  unicodeKeyboard：默认 false，设为 True 支持中文输入
  resetKeyboard：和 unicodeKeyboard 配合使用，用于恢复键盘输入。
  chromeOptions：chromedriver的 chromeOptions

# 稳定性相关的
newCommandTimeout：当 client 一直没给 appium 发消息的时候，appium 要等多长时间 默认：60s

# 性能相关的
ignoreUnimportantViews：默认是 false 如果设为 true, 调用uiautomator的setCompressedLayoutHierarchy 方法，对界面元素进行压缩，起到提速的作用
disableAndroidWatchers：默认是false 设为 true, 会停止监测应用无响应或者crash的安卓watcher，减少
cpu的使用，起到提速的作用。
autoGrantPermissions：默认是false，如果要设为true，前提是 noRest 为 false
skipDeviceInitialization：默认是false，设为 true，会跳过安装和运行 settings app，会相应提升启动性
skipServerInstallation：默认是false, 设为 true，跳过 uiautomator2 server的安装
skipUnlock
skipLogcatCapture：默认false，设为true，Skips to start capturing logcat.会相应提升性能
```



