#### 基本的测试项

- 业务测试（面向新需求）
- 回归测试 (面向已交付功能)
- 专项测试（聚焦业务与具体平台结合时产生的问题）
  - 移动端性能问题 (启动，响应，卡顿，崩溃，h5加载)
  - 移动端场景问题（弱网测试，兼容性测试，国际化测试）

#### 移动端专项测试关注项

- crash/anr

  - 测试手段：monkey，自动遍历，快进快退，横竖屏切换

- 卡顿（掉帧，gc， cpu）

  - 卡顿测试，内存泄漏

- 响应

  - 冷热启动测试，h5 性能测试

- 发热

  - systrace ，method profile 分析 cpu，mem，io等问题

- 兼容性（品牌，版本，典型分辨率）

  - 回归测试，云测平台

#### 1、启动

```shell
冷启动(5s)：从头开始启动。即连应用进程都没有，从创建应用进程[application.onCreate()]到启动主线程来创建 Activity[activity.onCreate()] 到 Activity 页面的初始绘制。
温启动(2s)：应用进程还在，但 activty 没了，所以温启动需要重新创建 activty
热启动(1.5s)：将驻留在内存中的 activty 带到前台。
首屏启动：首页加载完毕，用户可交互
参考文档；https://developer.android.google.cn/topic/performance/vitals/launch-time?hl=zh-cn

测试过程中主要关注的是冷启动和首屏启动。
冷启动的测试方法：
	package=com.android.xxx
	adb shell pm clear $package #清除应用数据
	adb shell am force-stop $package #终止应用进程
	adb shell am start -S -W $package/.xxx.xxxActivity  #启动app 【其实这块已经标明了冷启动的时间】
	adb logcat | grep -i displayed  #去logcat 中抓数据
首屏启动的测试方法：
	拆帧然后分析，具体如下：
	adb shell am force-stop $package  # 终止进程
	adb shell screenrecord --bugreport --time-limit 20 /data/local/tmp/xxx.mp4 & # 启动录屏并置于后台运行
	adb shell am start -S -W $package/.xxx.xxxActivity  # 启动应用
	等待录屏完成...
	adb pull /data/local/tmp/xxx.mp4 . 
	ffmpeg -i xxx.mp4 -r 10 frames_%03d.jpg  # 使用 ffmpeg 对录屏视频做拆帧处理
	
	或者在代码中埋点：reportFullyDrawn() 
	
----------------------- web站以及webview(h5) -------------------------------
测试m站的性能或者 webview(h5) 这块主要依靠浏览器的devtools 的network 以及 performance 功能来做web页面性能上的分析
因为 web 页面的性能已经标准化，w3c对web页面的性能有标准性的度量，具体可参考：https://github.com/w3c/web-performance
chrome 62.0.3202.0(开发者内部版本)

如何去动化获取性能指标：
	使用appium/selenium 的 execute_script 方法，调用 window.performance api 来获取数据。如 execute_script(return JOSN.stringfy(window.peformance.timing)
```

#### 2、卡顿

```
先看文档：
	卡顿：https://developer.android.google.cn/topic/performance/vitals/render?hl=zh-cn
	冰冻帧：https://developer.android.google.cn/topic/performance/vitals/frozen?hl=zh-cn

主要的检测手段：
	 adb shell dumpsys gfxinfo <package name>
	 官方提供的 Systrace 工具：https://developer.android.google.cn/topic/performance/tracing/command-line?hl=zh-cn
```

#### 3、Crash ANR

```shell
先看文档:
	crash：https://developer.android.google.cn/topic/performance/vitals/crash?hl=zh-cn
	anr：https://developer.android.google.cn/topic/performance/vitals/anr?hl=zh-cn

检测手段：
	adb logcat -s *:E
```

#### 4、弱网

```shell
弱网测试是健壮性测试的一种，即通过模拟弱网环境来检测应用延迟或者丢包的情况。
主要的方式：
    模拟器：
    $(which emulator) -avd [your-avd-image] -netdelay 20000 -netspeed gsm
    真机代理： charles模拟弱⽹ 
    ⽹关： Facebook的ATC (需要硬件支持)
参考资料：https://www.jianshu.com/p/06be11140413
```

#### 5、系统资源

```shell
adb shell dumpsys procstats --hours 3
adb shell dumpsys meminfo packageName
adb shell dupsys batterystas --chraged packageName
adb shell dumpsys netstats detail
adb shell dumpsys gfxinfo packageName
```

#### 6、耗电量

```shell
https://github.com/google/battery-historian  电量消耗报告
耗电量数据收集步骤： 
    adb shell dumpsys batterystats --reset # 清理耗电量数据
    adb shell dumpsys batterystats --enable full-wake-history
   
    appium uiautomator # 运⾏测试⽤例
    
    #收集耗电量数据
     >=7.0 adb bugreport bugreport.zip
     <=6.0 adb bugreport > bugreport.txt
参考资料：https://www.jianshu.com/p/1cf7c690a4d2
```

#### 7、性能分析工具 android profiler

```
先看文档：
https://developer.android.google.cn/studio/profile/android-profiler?hl=zh-cn
```













  

  



  

  

