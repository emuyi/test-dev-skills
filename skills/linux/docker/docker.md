docker 是 Linux 容器技术的一种封装，也可以简单理解为是一种轻量级的虚拟机。与传统的虚拟机架构相比，docker不虚拟内核

而是直接使用宿主机的内核，因此具有启动快，占用资源少的优点。它主要的是通过 **Linux 命名空间**来实现多个docker 容器之间

网络，进程，以及文件目录等之间的隔离，使用**cgroups** 来实现资源(CPU, MEM, IO)等之间的隔离，**联合文件系统**去定制镜像中的目录。

#### docker 安装

- 安装 
  - https://docs.docker.com/engine/install/ubuntu/
- 加速器配置
  - https://blog.csdn.net/dsl59741/article/details/107876795

#### docker 常用命令

```shell
官方文档： https://docs.docker.com/reference/
docker version
docker info
docker ${command} --help
```

##### 1、镜像命令

```shell
# 1. docker镜像和容器的区别
docker image 可以简单理解为一个携带安装环境的应用安装包，而 docker container是镜像包运行后的示例，是一个进程(具有独立的网络，进程控件，目录即一个简化版的虚拟机)，一个镜像可以起多个容器示例，类似于面向对象中的类和对象的关系
# 2. 镜像相关的命令
docker images # 查看镜像，-a：显示所有的镜像，-q：只显示镜像id
docker search # 搜索镜像，更建议去https://hub.docker.com/搜索
docker pull # 拉取镜像 默认是拉取latest，如果要指定版本，docker pull mysql:5.7
docker rmi -f # 删除镜像
```

##### 2、容器命令

```shell
docker ps # 查看容器  默认是查看正在运行的容器， -a：正在运行的容器+历史运行过的容器 
		  # -q：只显示容器的id
docker rm  -f 容器id (容器name)  # docker ps -aq | xargs docker rm -f

docker start id/name 
docker restart id/name
docker stop id/name
docker kill id/name

docker run 
	# 注意run的流程，会先从本地找镜像，有的话直接执行，没有去仓库拉取镜像并执行
	# --name 给容器命名
	# -d 后台运行
	# -p 端口映射 主机端口:容器端口
	# -v mount 文件挂载
	# -e 设置环境变量

docker top # 查看容器中的进程
docker logs -f --tail 20 id/name # 查看容器日志
docker inspect  # 查看容器元数据
docker exec -it 容器id bash # 进入容器，新开起一个终端
docker attach 容器id  # 进入容器，进入正在执行的终端
docker cp 容器id:容器路径 host路径	# 从容器中拷贝文件到主机
```







