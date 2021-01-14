#### 自动化遍历回归测试工具

##### 为什么需要自动遍历：

- UI自动化只能覆盖核心业务逻辑，新功能来不及上自动化。

- 产品业务测试量较大，新版发布后，老功能来不及全面回归，容易漏测。

- 时间长，强度大的工作后，人容易产生疲乏，对数字的位数，文字的显示等错误信息的敏感度下降。

- 产品的界面深度很深，且包含大量的展示信息功能。

##### 相关工具：

###### monkey

```shell
与其说 monkey 是UI遍历工具，倒不如说它是一款UI压力测试工具。因为 monkey 生成的是伪随机用户事件，这意味着 monkey 的操作完全是随机的，不可控的，并不能很好的满足遍历测试的需求。关于monkey的使用和参数参考：https://developer.android.google.cn/studio/test/monkey?hl=zh-cn
简单示例：
	adb shell monkey -vv -p com.xueqiu.android --pct-touch 50 --pct-motion 20 --throttle 1000 200
    # -v 增加输出的详细度，不加的话是静默模式，每增加一个v，输出的更详细
    # --pct-touch 设置 touch 事件的比例为 50%
    # --pct-motion 设置 motion 事件的比例为 20%
    # --throttle 设置事件之间的间隔事件 (ms)
    # 200 生成 200个随机事件
    此外，-s <seed> 伪随机数生成器的种子值。如果您使用相同的种子值重新运行 Monkey，它将会生成相同的事件序列。
 
```

##### App Crawler

```shell
官方提供的遍历工具
https://developer.android.google.cn/training/testing/crawler
文档写的基本等同没写。。。。
```

##### Maxim

```shell
https://github.com/zhangzhao4444/Maxim
```

##### app_crawler

```
https://github.com/seveniruby/AppCrawler

基于 appium 引擎
    就遍历来讲主要的构成：
        capbilities：和 appium 完全一样，主要也是和 appium 做接轨用的
        testcase：支持一些简单的测试步骤，如；点击某个控件，进入到要遍历的页面
        selectedList: 指定遍历的控件范围及动作
        trigger：可以用例处理突然弹出的窗口
    主要使用方法：
        可以在命令行使用参数来调用 jar 包，但更推荐使用配置文件
        即执行 java -jar appcrawler.jar --demo 会在生成一个 demo.yml 文件
    配置文件快速上手：
       capability：写 appium 的 capability
       testcase: 的 steps 中可以使用简写的 xpath：xxx action：xxx
       selectList: 指定遍历的范围。也可以使用简写的 xpath:xxx, action:xxx  注意这快的定位，定位的是要遍历控件的父类们，即要遍历的大致范围
       firstList：优先遍历的
       lastList：最后遍历的
       tagLimitMax: 20 tagLimitMax：同祖先（同类型）的元素最多点击多少次，如果要覆盖的比较多，尽量写大一些
       效果如下：[基于提供的yaml做的简单配置，实际场景可定好自己的需求，根据需求看文档来做配置修改
       https://github.com/seveniruby/AppCrawler]
```
```yaml
pluginList: []
saveScreen: true
reportTitle: ""
resultDir: "20210114110452"
waitLoading: 500
waitLaunch: 6000
showCancel: true
maxTime: 10800
maxDepth: 10
capability:
  noReset: "true"
  fullReset: "false"
  deviceName: "emulator"
  platformName: 'android'
  automationName: "uiautomator2"
  appPackage: "com.xueqiu.android"
  appActivity: ".view.WelcomeActivityAlias"
  appium: "http://127.0.0.1:4723/wd/hub"
testcase:
  name: "TesterHome AppCrawler"
  steps:
    - xpath: "//*[@text='行情']"
      action: click
    - xpath: "//*[@text='市场']"
      action: click
selectedList:
  - 
   xpath: "//*[contains(@resource-id, 'indices_pager')]//*[@clickable='true']" 
   action: click
  -
   xpath: "//*[contains(@resource-id, 'title_container')]//*[contains(@resource-id, '/title_text')]"
   action: click
  - 
   xpath: //*[contains(@resource-id, 'entrance_view_pager')]//*
   action: click
firstList: [] 
lastList: [] 
backButton:
- given: []
  when: null
  then: []
  xpath: "Navigate up"
  action: null
  actions: []
  times: 0
triggerActions:
- given: []
  when: null
  then: []
  xpath: "share_comment_guide_btn"
  action: null
  actions: []
  times: 0
xpathAttributes:
- "name"
- "label"
- "value"
- "resource-id"
- "content-desc"
- "instance"
- "text"
sortByAttribute:
- "depth"
- "list"
- "selected"
findBy: "default"
defineUrl: []
baseUrl: []
appWhiteList: []
urlBlackList: []
urlWhiteList: []
blackList:
- given: []
  when: null
  then: []
  xpath: ".*[0-9]{2}.*"
  action: null
  actions: []
  times: 0
beforeRestart: []
beforeElement:
- given: []
  when: null
  then: []
  xpath: "/*"
  action: "Thread.sleep(500)"
  actions: []
  times: 0
afterElement: []
afterPage: []
afterPageMax: 2
tagLimitMax: 20
```

```python
 对appCrawler的技术原理的简单理解：
    1、使用 page_source 获取整个页面的控件树结构
    2、根据提供的比较宽泛的 xpath，去控件树中定位元素
    3、为匹配到的每一个元素生成一个唯一的xpath表达式或者id定位表达式
    4、将生成的表达式传递给 appium 进行执行
其实单从遍历功能上来讲的话，个人感觉和使用appium的 find_elements, 然后对定位到的元素列表进行遍历操作，从技术理论上来讲很类似。
```
