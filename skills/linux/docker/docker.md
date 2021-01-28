docker 是 Linux 容器技术的一种封装，也可以简单理解为是一种轻量级的虚拟机。与传统的虚拟机架构相比，docker不虚拟内核

直接使用宿主机的内核，因此具有启动快，占用资源少的优点。它主要的是通过 **Linux 命名空间**来实现多个docker 容器之间网络，

进程，目录等之间的隔离，**cgroups** 来实现资源(CPU, MEM, IO)等之间的隔离，**联合文件系统**去定制镜像中的目录。

#### docker 安装及加速器配置

- 安装 
  - https://cloud.tencent.com/developer/article/1167995
  - https://docs.docker.com/engine/install/ubuntu/
- 加速器配置
  - https://blog.csdn.net/dsl59741/article/details/107876795





