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



