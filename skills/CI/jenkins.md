```python
持续集成(CI): 是一种软件开发实践，采用持续集成时，开发人员会定期将代码变更提交到代码仓，系统会自动运行构建和测试操作。通俗来讲，开发人员每提交一个新的功能，系统就会自动构建一个自动化测试对该功能进行验证。持续集成的好处在于能够及时并快速的发现软件质量问题，能够保证产品在快速迭代的同时也具备高质量。  
https://aws.amazon.com/cn/devops/continuous-integration/    
https://www.martinfowler.com/articles/continuousIntegration.html
```

![ci-cd](cicd.png)

```python
Jenkins 是一个持续集成的工具，主要用于构建自动化任务。
doc：https://www.jenkins.io/doc/book/ 
```

#### Jenkins 服务搭建

```shell
doc：https://www.jenkins.io/doc/book/installing/
linux搭建：https://www.jenkins.io/doc/book/installing/linux/
docker搭建：https://www.jenkins.io/doc/book/installing/docker/

# 镜像源
# 安装包：https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/
# 安装包：https://mirrors.aliyun.com/jenkins/debian-stable/
# 插件：https://mirrors.aliyun.com/jenkins/updates/update-center.json

# docker安装注意点：
# 1、docker:dind (docker in docker) Jenkins为了在Jenkins容器中使用docker命令
# 2、通过dockerfile定制了一个配置了docker仓库和blue ocean插件的Jenkins镜像
```

#### Jenkins 简单使用

```shell
# =========================环境准备(linux、war file)==============================
代码仓方面：git 插件一般会默认安装，只需要在linux host上生成ssh key，对应配置 jenkins Credentials
python项目：最好生成下 requirements.txt 文件
# =========================jenkins启动和更新插件源==================================
1、启动jenkins：java -jar jenkins.war --httpPort=8010
2、先安装推荐插件
3、更新插件镜像源头为国内源
   mange jenkis --> manage plugins --> advanced --> Update Site
# =========================freestyle job 配置(pytest+email+allure)===================
1、入口：new item --> freestyle project
2、一个简单job配置如下：
General：
	Discard old builds 设置废弃旧构建项目策略，包括保持几天的构建，保持最大的构建个数等。可根据需要配置【主要目的是减少
	磁盘空间占用】
	
Source Code Management：
	Git 设置好git的repo、Credentials、构建的分支等【ssh with private key】

Build Triggers：
	Poll SCM：可以根据设定的时间去轮询代码库，如果有更新就执行构建
	此外 GitHub hook trigger for GITScm polling：可以通过 hook的方式触发构建，不过这个得要求github和jenkins能互相通信。如果jenkins服务是在内网搭建的话，可能会比较困难，酌情考虑。相关配置方式请google。

Build：
	add build step 选择对应的执行shell
	# 注意shell所在的工作路径是jenkins workspace的路径(源码根目录)
	# 示例：python 单元测试项目的shell编写
	pip3 install -r requirements.txt
    pytest -v ./test_unit

    rm -rf ./allure_report   # 也可以在代码中实现，灵活处理
    pytest --alluredir ./allure_report

    rm -f allure-report.zip 
    zip -r allure-report.zip allure_report  # 作为邮件附件
    
    # WORKSPACE是jenkins的内置变量，当前的job的工作目录  shell下方有个连接可以查看各种内置变量
只需这样一个简单的jenkins job就构建起来了。
```

#### Jenkins 节点管理和用户权限配置

#### Jenkins 生成Allure测试报告和邮件报警

```shell
# 集成 Allure 测试报告
1、mange jenkis --> manage plugins 安装插件 Allure
2、Manage Jenkins --> Global Tool Configuration --> Allure Commandline 设置下name：allure, 版本选择最新即可
3、回到job配置中(my view) Build-->execute shell添加报告生成命令 如：pytest --alluredir ${WORKSPACE}/allure_report
4、Post-build Actions 选择 allure report 告诉下jenkins生成的allure report的路径就可以了，如上方示例的 allure_report

# 邮件报警
mange jenkis --> system config
1、System Admin e-mail address：配置发件人的邮件地址
2、E-mail Notification --> advanced 填写相关的信息 如下方：  # 注意此步骤可以用来测试下是否可以正常收发邮件
'''
SMTP server:  smtp.126.com
Default user e-mail suffix:  @126.com
Use SMTP Authentication
用户名：发件邮箱
密码： # 注意这个是授权码	
SMTP Port: 465
Charset：UTF-8	
'''
3、配置 Extended E-mail Notification， 如果没有需安装下  Extended E-mail 插件
	a、点击 advanced 按照 2 步骤配置下smtp server等信息
	b、Default Content Type: HTML # 这个根据需求来
	c、Default Recipients：收件人，多个收件人用，隔开
	d、Default Subject：主题 如：【自动化构建通知】$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!
	e、Default Content：邮件正文 相关模板可以去网上找：https://www.cnblogs.com/wintest/p/12209751.html
4、job config --> Post-build Actions 选择 editable email notifition
	 重新设置收件人，邮件主题，内容之类...
	 Attachments: allure-report.zip  # allure 的测试报告
	 advanced setting --> Triggers 设置邮箱发送的触发条件 # 具体触发条件看场景，如可以这样设置 Triggers
	 # 第一次失败，第二次失败，fixed

# 如果未收到邮件 	
1、安装插件后jenkins最好重启下
2、Allow sending to unregistered users 注意勾选下 或者让收件人注册下jenkins
3、密码错了
```



#### Jenkins 多任务关联运行

#### Jenkins API

#### Jenkins Pipeline

#### Jenkinsfile

#### Blue Ocean

