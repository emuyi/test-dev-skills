```python

appium server log分析：
        --> POST /wd/hub/session
        Calling AppiumDriver.createSession() with args: [{"deviceName":"Android
        Session created with session id: fecb53eb-2252-436a-b697-a0ba989f0439
        Starting 'com.xueqiu.android' directly on the device
        Running 'D:\android\sdk\platform-tools\adb.exe -P 5037 start-server'
        Connected devices: [{"udid":"emulator-5554","state":"device"}]
        adb shell getprop ro.build.version.release 校验版本
        use proper release device
       push and  install  io.appium.settings 确保它运行起来
       Setting IME to 'io.appium.settings/.UnicodeIME'
       forwarding UiAutomator2 Server port 6790 to local port 8210
       adb shell  forward tcp:8210 tcp:6790
      install and check  io.appium.uiautomator2.server is installed or not
      Getting install status for io.appium.uiautomator2.server.test

      Getting install status for com.xueqiu.android
      performed fast reset on the installed 'com.xueqiu.android' application (stop and clear)
      adb.exe -P 5037 -s emulator-5554 shell am start -W -n com.xueqiu.android/com.xueqiu.android.view.WelcomeActivityAlias
       <-- POST /wd/hub/session 200  app启动，返回200 ok

       --> POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/timeouts 【设置隐式等待 5000ms】
       <-- POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/timeouts 200

       --> POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/element
       {"using":"id","value":"tv_search"}  webdriver:  json wire protocol
       <-- POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/element 200 4061 ms - 137

      --> POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/element/a6f6802d-e205-4c00-ad44-2245cfccb2a8/click
      {"id":"a6f6802d-e205-4c00-ad44-2245cfccb2a8"} json wire protocol
      <-- POST /wd/hub/session/fecb53eb-2252-436a-b697-a0ba989f0439/element/a6f6802d-e205-4c00-ad44-2245cfccb2a8/click 200 1591 ms - 14

      ...........一系列一来一回的请求响应..............

       Closing session, cause was 'New Command Timeout of 60 seconds expired. Try customizing the timeout using the 'newCommandTimeout' desired capability'
       Removing session 'fecb53eb-2252-436a-b697-a0ba989f0439' from our master session list
       delete uiautomator2 server session
       shell ime set io.appium.settings/.UnicodeIME'  : rest ime
       am force-stop com.xueqiu.android'
       Removing forwarded port socket connection: 8210
       ....

```



