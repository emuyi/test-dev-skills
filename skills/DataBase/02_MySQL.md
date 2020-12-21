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

##### 4.表操作(DDL)

```sql
1.创建表
create table t_xxx (
	字段名 字段类型 约束,
    ............
)
1.1 常用字段类型
	int: 4 bytes
	bigint: 8 bytes
	char: 定长字符类型, 长度范围0~255
	varchar:变长字符类型, 长度范围 0 ~ 65535 2**16
	float 4b / double 8b /decimal
	date
	BLOB: 存储二进制大文件,如图片,视频流媒体文件之类的.不过一般都不会直接存在数据库中
	CLOB: 特别大的文本文件
	https://www.runoob.com/mysql/mysql-data-types.html
	char 和 vachar 的区别?
	
1.2 约束
	添加约束是用来保证数据的合法性,有效性和完整性.
	not null 数值不能为 null
	unique 唯一,不重复.但可以为 null,因为null不是值,没有可比性. unique(field1, field2)
	primary key
		""
		主键是在一张表中每条记录的唯一标识, 所以主键不为空且唯一.
		每一张表中都应该有主键, 但主键约束只能添加一个. 使用多个字段联合做主键可以,但不推荐,
		因为违背表设计三范式.另外,主键不要和业务产生关系,一个单纯的自然数就可以.(如自增ID主键,
         如uuid之类的)
		""
        设置主键: primary key auto_increment
	foreign key
		设置外键: foreign key(classID) references from t_class(ID)
		""
		设置外键后,意味着涉及外键的两张表之间就有了父子关系,外键值必须要来自外键引用的他表的字段值.
		在删除表,更新数据的时候都具有了约束. 如学生表和班级表, 如果要删除表,得先删除学生表(子)
		在删除班级表(父), 如果要创建表和插入数据,得先去创建班级表和插入数据.
		外键值可以为 null; 最好是其他的主键,如果不是,至少该字段得有个 unique 的约束.
		""
		
	mysql> create table t_class(
    -> cid int primary key auto_increment,
    -> cname varchar(255) unique);

	mysql> create table t_student(
	-> tid int primary key auto_increment,
	-> tname varchar(20) not null,
	-> cid int,
	-> foreign key(cid) references t_class(cid));
	
mysql> desc t_class;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(255) | YES  | UNI | NULL    |                |
+-------+--------------+------+-----+---------+----------------+

mysql> desc t_student;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| tid   | int(11)     | NO   | PRI | NULL    | auto_increment |
| tname | varchar(20) | NO   |     | NULL    |                |
| cid   | int(11)     | YES  | MUL | NULL    |                |
+-------+-------------+------+-----+---------+----------------+


2.删除表 drop table xxx; 修改表结构 alter table xxx add ...

```

##### 引擎

```sql
通俗理解就是数据库存储数据的方式.mysql比较常见的引擎就是InnoDB和MyISAM,其中InnoDB是mysql的默认引擎.
MyISAM 用三个文件来表示一张表, frm表示表结构, myd是数据文件, myi是索引文件, 因此 mysiam 可以转换为压缩,只读表来节省空间.它不支持事务外键,行级锁,崩溃后无法及时进行数据恢复,但是查询速度快,比较适合有大量读操作的场景.
InnoDB: 使用frm文件来表示表结构,而数据和索引是放在表空间里.它支持事务,外键,行级锁,崩溃后数据能及时恢复.
```

##### 事务

```sql
1、对事务的理解
	"当对表数据执行增删改操作的时候,事务能够提供一种安全机制.主要是基于它以下的几点特性:
	A 原子性:一个事务中的操作要么同时成功要么同时失败.
	C 一致性:只有合法的数据才能写入数据库
	I 隔离性:多个事务并发,无论哪个事务先结束,最后的结果都应该是相同的
	D 持久性: 一旦事务提交,不管发生什么(崩溃或出错) 数据都要保存到数据库中
mysql 默认事务是自动提交的,如果想事务不自动提交,可以使用 begin 或start transaction来关闭自动提交.
	"
 2. 对事务隔离的理解
 	"有四个级别:
 	 读未提交(read uncommitted): 
 	 我方事务可以读到对方事务未提交的数据, 由于未提交的数据都是缓存中的数据,所以会出现脏读问题.
 	 读已提交(read committed): 
 	 我方只能读到对方事务提交后的数据, 解决了脏读问题,但会出现不可重复读(即两次查询的结果不一样)的问题.
 	 可重复读(repeatable read)
 	 即便是对方提交了事务,但我方仍旧可重复读取数据,但这份数据已不是存在磁盘上真的数据,所以可能出现幻读问
 	 但 InnoDB 引擎使用了多版本并发控制机制对幻读问题做了处理.
 	 串行化读(Serialization) 
 	 简单理解就是事务要排队执行.
 	"
	mysql默认是使用的 repeatable read 级别
3. 事务操作相关语法	
   开启事务:begin/start transaction;
   提交事务:commit. rollback 回滚事物
   savepoint point_name; 建立保存点,回滚的时候可以 rollback to point_name, 单纯的rollback的话是    回滚到上一个提交的地方.
   
4.事务提交和回滚的原理
	"
	开启事务后,执行的增删改操作都相当于一个历史记录,并没有真正到持久化到磁盘上.
	commit 提交后,数据会保存到数据空中,历史操作记录被清空,事务结束.
	如果rollback,操作记录会被清空,数据回滚到上次的提交操作, 事务结束.
	因此, commit 和 rollback都会结束事务.但mysql的事务不是自动回滚的,
	只有手动执行 rollback 命令后才会回滚数据,因此可以加些逻辑上的判断,去实现
	自动回滚的效果.
	"
 
```

##### 索引

```sql
1.什么是索引,索引的作用
"索引是一种加快数据库查询的数据结构,索引的本质是减小数据库扫描的范围来加速查询."
默认情况下主键,唯一约束的字段都会添加索引.
关于B+树: https://mp.weixin.qq.com/s/MCFHNOQnTtJ6MGVjM3DP4A
2.添加索引,删除索引
  create index 索引名 on 表名(字段);
  drop index 索引名 on 表名;
3.什么情况适合添加索引
  "
  数据量比较大的的情况下
  增删改的操作比较少的字段
  频繁出现中where语句中做查询条件的字段
  "
4.使用 explain 语句查询SQL语句的执行计划
 explain select username from t_user where username = 'ellen';
```

![image-20201221153642098](C:\Users\MUYI\AppData\Roaming\Typora\typora-user-images\image-20201221153642098.png)

#### 三范式

```sql
1. 任何一张表都应该有主键,且每一个字段都应该原子性不可再分
2. 所有非主键字段完全依赖主键,不能产生部分依赖. (复合主键违反了2范式)
	"多对多, 三张表, 关系表加上外键"
3. 所有非主键字段直接依赖主键,不能产生传递依赖.
	"一对多关系, 学生表(外键)和班级表"
范式只是一种依据和理论, 怎么设计表还是要根据需求而定,三范式出来的表,很少冗余,但在速度上不一定就快.
    "一对一关系, 如用户表和用户详细表 可以用外键唯一去设计,即用户详细表加个有外键和唯一的约束的  uid字段"
```

##### 数据库导入和导出

```sql
导出: mysqldump 数据库 > 路径/xx.sql -u "user" -p "passwd";
msyqldump 数据库 表 > 路径/xx.sql -u "user" -p "passwd"; 备份指定表
导入: source xx.sql
```

#### pymysql

```python

```



