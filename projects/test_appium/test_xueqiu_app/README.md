#### Appium PO 设计方案

##### 基本框架设计：

```python
page层：
    - BasePage 封装基本操作， 如 find， get_toast_msg 等等
    - App 封装应用相关的操作：如lanch_app, close_app, restart_app, background_app 等等
    - MainPage 封装APP首页功能： 如 search等等
    - SearchPage 封装 search 页面的功能， 如 search 和 search后的信息返回等等
    - StackPage 封装行情页面的功能，如一键添加自选等等
    - TradePage 封装【Webview组件】交易页面的功能，如开户功能等等
    - ProfilePage 封装 我的页面功能， 如登录等等

case层:
    - 测试主页search功能，步骤：搜索框输入某支股票并断言该股票的价格
    - 测试search功能，步骤：search页面搜索某支股票并添加股票到自选，然后断言是否添加成功
    - 测试交易页面如A股开户，输入开户信息并断言
    - 测试登录功能
    .....

log&test report层：
    - 使用 logging 模块记录执行流程的log并保存为 running_log.txt
    - allure生成测试报告
    
data 数据驱动(基于yaml)：
    - 测试数据的数据驱动
      因为测试数据驱动需要借助 mark， 所以 yaml 数据的组成得是 [[],[],[]] 的形式
      TODO:如果做成装饰器直接load file 并 mark 配合，如何做
    - PO执行步骤的数据驱动
    　 TODO:将PO测试步骤也变成数驱动的意义
    
utils: 提供一些通用的工具和方法 如 logging class 等

settings: 全局配置项目

run_test.py 入口脚本
```

##### 遇到的问题和优化思路：

```yaml
- 用例执行过程中突然出现各种弹窗怎么办？如何去保证 case 的稳定性
   - 优化思路：在 find 的时候做异常处理，即使用 try...except, 
      在 execept中对弹框做操作，如click，完成后再执行 find  
   - 进一步封装，将这段逻辑封装成装饰器，然后使用装饰器来修饰find

- mian Page 加载的时候需要增加显示等待
- swith context的时候注意加上显示等待来保证用例的稳定性
```
##### 项目收获：

```python
1、装饰器有两大特性：增强函数行为; 导入时即运行。 尤其是导入时即运行对应的思想一定要非常清晰才行。
2、切换到 webview 点击某控件跳转到某个页面，定位该页面上的某个元素的时候，死活定位不到，这时
   需要考虑下，是不是跳转导致新开了一个 window handle。
```
