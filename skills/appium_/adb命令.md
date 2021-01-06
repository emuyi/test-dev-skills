## ADB

````python
ADB：Android Debug Bridge ，用于和安卓设备进行通信。

adb 包括：
	1. adb client：位于PC上，用来发送操作请求
    2. adb server：PC上的后台进程，通过监听本机的5037端口，来接收 client 的指令，并转发给 adbd【管理 client 和 adbd 之间的通信】
    3. adbd (adb守护进程)：设备上的一个后台进程，会根据收到指令来操作设备。
adb 的工作原理：
	adb client 启动后会先检测是否有 adb server进程在运行，没有的话会启动adb server并绑定本地5037的TCP端口，通过该端口与adb client进行通信。同时也会扫描PC连接的设备，一旦发现设备上的 adbd 进程，会在对应的端口进行连接，当 server 与所有的设备建立好连接后，就可以使用adb client来发送指令操作设备。
    
使用 adb devices -l 检测设备连接状态 如下：
# emulator-5554  device  product:sdk_gphone_x86_arm....
 emulator-5554：SN
 device: 连接状态 主要有三个状态：
 """
 offline：设备没有连接到adb server或者没有响应
 device: 设备已经连接到 adb server【！但不能作为设备启动状态的检测，因为设备已经连接到adb的时候可能还在启动】
 no device：没有设备连接
 """
 -l 参数能列出设备的一些信息，在多设备连接的时候可以帮助区分设备
    
    
adb 常用命令：
 - adb -s 
 - adb start-server 启动 adb 服务， adb kill-server 干掉 adb 服务
 - adb reboot 重启设备
 - adb reboot-bootloader 进入 fastboot 模式(烧写镜像)
 - adb forward 端口转发：将本地端口上的请求转发到设备的端口上
      建立转发：adb forward tcp:6100 tcp:8080
      查看状态：adb forward --list      
      取消转发：adb forward --remove tcp:6100 
 - adb reverse 端口反向转发：将设备端口上的请求转发到本地端口上
      adb reverse tcp:8080 tcp:8000 查看和取消同 adb forward
      # 如：本地使用 python -m http.server 8000 在 8000 端口起个服务，去手机上浏览器上访问localhost:8080  
  - adb install xxx.apk (加 -r 参数是覆盖安装)
  - adb uninstall packageName (-k 保存数据和缓存目录)
  - adb pull remote local [！拉取系统权限目录需要获取root权限，adb root/ adb remount挂在系统文件文为可读写状态 ]
  - adb push local remote
  - adb logcat https://developer.android.google.cn/studio/command-line/logcat?hl=zh-cn
  
adb shell命令
 - Android 自带的命令 位于设备/system/bin/目录下
 - adb shell am (activity manager)
	-- start -n com.android.camera2/com.android.camera.CameraLauncher 启动相机
    -- start -S com.android.camera2/com.android.camera.CameraLauncher 先停止再启动
	-- start -W com.android.camera2/com.android.camera.CameraLauncher 等待应用完成启动	
    -- start -a android.intent.action.VIEW -d http://www.bing.com 启动默认浏览器打开指定的网址
    -- start -a android.intent.action.CALL -d tel:10010 启动拨号器拨打 10010
    -- force-stop packageName 强行停止与 package（应用的软件包名称）关联的所有进程
 - adb shell pm (package manager)
	-- pm list package 列出所有的应用
    -- pm list pacage -s 列出系统应用
    -- pm list package -3 列出第三方应用
    -- pm list package -f 列出包名及对应的apk名及存放位置
    -- pm list package -i 列出包名及安装来源
    -- 所有命令后可以加 关键字进行查找，如
    	adb shell pm list package -3 -i xueqiu
    -- pm path packageName  查看对应包名的apk所在的位置
    -- pm dump packageName  dump 对应包名应用的信息 
    -- pm install xx.apk 当 apk 放在设备上的时候，使用 pm install安装 (如果在pc上，用adb install)
    -- pm uninstall packageName 同 adb uninstall
    -- pm clear packageName 
    -- pm set-install-location , pm get-install-location , 设置应用安装位置，获取应用安装位置
    
  - adb shell input 向设备发送按键事件
    -- adb shell input text hello
    -- adb shell input tap x y
    -- adb shell input swipe x1,y1,x2,y2
    -- adb shell input keyevent keycode
  
  - adb shell screencap -p /sdcard/aa.png  !!推荐这个 adb exec-out screencap -p > file.png
    adb shell screenrecord -time-limit 10 /sdcard/aa.mp4
    
  - adb shell uiautomator dump /sdcard/aa.xml
  - adb shell wm size 获取设备分辨率
  - adb shell getprop 以key：value的形式来存储信息，可以.key获取对应的value
	adb shell getprop ro.build.version.sdk
  - adb dumpsys  https://developer.android.google.cn/studio/command-line/dumpsys?hl=zh-cn
    如：adb shell dumpsys activity | grep mCurrentFocus
       adb shell dumpsys window | grep mCurrentFocus
官方介绍：https://developer.android.google.cn/studio/command-line/adb?hl=zh-cn
命令集合：https://www.wanandroid.com/blog/show/2310 
````

