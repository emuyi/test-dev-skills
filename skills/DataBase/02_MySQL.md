##### DB & DBMS

```python
DB: Database 存在硬盘上的文件.
DBMS: Database Manage system 数据库管理系统. 用来管理数据库和编译数据库语句. 
常见的 DBMS 如:
    关系型数据库: MySQL, Oracle, MariaDB(类似 MySQL 的开源版本) , PostgreSQL, SQLserver
    非关系型数据库: MongoDB, Redis
```

##### MySQL

````sql
1. MySQL server 安装及配置 
2. MySQL 客户端及客户端工具
   mysql-client: 官方提供的一个客户端工具合集,如 mysql commands line, mysql shell 之类的
   常见的客户端图形交互工具: navicat, 官方的 mysql workbench, phpadmin3
3. MySQL 数据库操作命令
   show databases;
   create database xxx;
   use database xxx;
   show tables;
   desc yyy; 查看表 yyy 结构 即查看表的字段名,字段类型,值是否是 null, 是否是主键, 外键...
   show create table yyy; 显示表 yyy 的创建语句.
   select database(); 查看当前使用的数据库
   等等
  
````

