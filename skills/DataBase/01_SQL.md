SQL 是一种结构化查询语言. 由于 SQL 的重要性, 将其单独提取出来, 方便今后工作查询使用. 将以 MySQL

为例来展示 SQL 语法.

##### SQL 的分类

```sql
DQL(数据查询语言 Query): 查询语句, select
DML(数据操作语言 Manipulation): 增删改, insert delete update
DDL(数据定义语言 Definition ): create  alter drop 对表结构进行操作
DCL(数据控制语言 Control): grant 授权; revoke 撤销
TCL(事物控制语言 Trasaction): commit 提交事物, rollback 回滚.
```

##### 一. DQL :  select 

##### 1. 单表查询

```sql
示例数据库来源同目录下 test_db.sql, 可以使用以下方法进行导入.
"""
create database test_db;
source xx/xx/test_db.sql
"""
1.简单查询
  select ename, sal * 12 as '年薪' from emp;
  tip. as 起别名, 如果别名是中文的话, 需要用引号括起来,即转化成字符串的形式.
  为例保证 SQL 语句的通用性, 建议 SQL 中的字符串都用 ''包括, 虽然MYSQL 也支持
  引号,但是其他数据库不一定适用. 另外尽量不要使用select *.
  
 2.条件查询 where子句
   常用作条件查询的运算符:
    = != > < >= <=
    or ; and
    between A and B相当于A <= data <= B
    is null ; is not null 
    in (a, b, c) 相当于多个 or ; not in
    like 模糊查询 %:匹配多个字符; _匹配一个字符
   
   select deptno, ename, sal from emp where ename = 'king';
   select ename, sal from emp where sal > 1000  and sal < 2000;
   
   找出薪资在1000,2000(包含) 且名字以a开头的员工.
   select ename, sal from emp where (sal between 1000 and 2000) and   ename like 'a%';
   tip：
   1.当不确定条件优先级的时候,用小括号括起来,小括号的优先级最高.
   2. a% 以a开头的, %b 以b结尾的, %c% 包含c的, %\_% 包含_的,特殊符号要注意使用 
      \ 来进行转义.
   3. between  and 用于数值范围的时候, 是全闭区间[]即相当于 <=且>=
   
   找出没有补贴的员工
   select ename, comm from emp where comm is null or comm = 0;
   找出工资大于2000且部门编号式20或30的员工
   select ename, deptno, sal from emp where sal > 2000 and deptno in (20, 30);
   tip：
   1. 仍旧是优先级的问题，不确定的话就小括号把紧要的括起来
   2. in 一个区间 ，相当于多个 or
   
 3. 数据排序 order by 子句
    asc 升序(默认)；desc 降序
    按照部门升序排序，薪资降序排序
    select deptno, sal from emp order by deptno, sal desc;
    tip：
    多个字段排序，当第一个字段无法完成排序的情况下（有相等的情况），后续的
    字段才有意义。
 4. 分组 group by 子句
 	group by 根据某个字段，某些字段进行分组
 	having 是对分组后的数据进行再次的过滤
 	关于分组函数 count sum avg max min，分组函数一般是对group by分组后的数据进行处理, 当没有group by时,整张表看做是一组。分组函数具有以下的特点:
 	1. 分组函数(类似归约函数) 会忽略 null 
 	  select sum(comm) from emp; 
 	    +-----------+
        | sum(comm) |
        +-----------+
        |   2200.00 |
        +-----------+
 	  插一句:在SQL中任何和null进行的计算结果都是null.
 	  所以这里会有一个面试题: count(*) 和 count(某个字段) 的区别
 	  count(*) 查询的是整个记录的条数, count字段,如果字段中有null的话,
 	  会忽略null.
 	2. 分组函数不能用在 where 子句中
 	   "这是因为 SQL 的执行顺序, group by是在where后执行的, 分组函数
 	   是对分组后的数据做处理, where执行的时候,group by还没执行,没有分组
 	   哪来的处理."
 	   
 	3. 关于 null计算为null的问题, ifnull(有null的字段, 指定值) 可以处理
 	 select ename, (sal+ifnull(comm, 0))*12 as yearsalary from emp;
 	
   找出每个部门,  不同岗位最高薪资 > 2500 的
   select deptno, sal from emp group by deptno, sal having max(sal) > 2500;
   select deptno, max(sal) from emp where sal > 2500 group by deptno, sal; 效率更高,想下为什么.建议分开SQL执行看看.
   
 tip: only_full_group_by：使用和oracle一样的group 规则, select的列都要在group中,或者本身是聚合列(SUM,AVG,MAX,MIN) 才行 
     4. 单表 SQL 的查询顺序
      select
      ....
      from
      ....
      where
      .....
      group by
      .....
      having
      .....
      order by
      .....
      
      from --> where --> group by --> having --> select --> order by
```











