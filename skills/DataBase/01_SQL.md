SQL 是一种结构化查询语言. 由于 SQL 的重要性, 将其单独提取出来, 方便今后工作查询使用. 将以 MySQL

为例来展示 SQL 语法.

#### SQL 的分类

```sql
DQL(数据查询语言 Query): 查询语句, select
DML(数据操作语言 Manipulation): 增删改, insert delete update
DDL(数据定义语言 Definition ): create  alter drop 对表结构进行操作
DCL(数据控制语言 Control): grant 授权; revoke 撤销
TCL(事物控制语言 Trasaction): commit 提交事物, rollback 回滚.
```

#### 一. DQL :  select 

##### 1. 单表查询

```sql
示例数据库来源同目录下 test_db.sql, 可以使用以下方法进行导入.
"""
create database test_db;
source xx/xx/test_db.sql
"""
1.1 简单查询
  select ename, sal * 12 as '年薪' from emp;
  tip. as 起别名, 如果别名是中文的话, 需要用引号括起来,即转化成字符串的形式.
  为例保证 SQL 语句的通用性, 建议 SQL 中的字符串都用 ''包括, 虽然MYSQL 也支持
  引号,但是其他数据库不一定适用. 另外尽量不要使用select *.
  
1.2 条件查询 where 语句
   常用作条件查询的运算符:
    = != > < >= <=
    or ; and
    between A and B相当于A <= data <= B
    is null ; is not null 
    in (a, b, c) 相当于多个 or ; not in
    like 模糊查询 %:匹配多个字符; _匹配一个字符
   
   select deptno, ename, sal from emp where ename = 'king';
   select ename, sal from emp where sal > 1000  and sal < 2000;
   
   示例:找出薪资在1000,2000(包含) 且名字以a开头的员工.
   select ename, sal from emp where (sal between 1000 and 2000) and   ename like 'a%';
   tip：
      1. 当不确定条件优先级的时候,用小括号括起来,小括号的优先级最高.
      2. a% 以a开头的, %b 以b结尾的, %c% 包含c的, %\_% 包含_的,特殊符号要注意使用 
           \ 来进行转义.
      3. between  and 用于数值范围的时候, 是全闭区间[]即相当于 <=且>=
   
   示例:找出没有补贴的员工
   select ename, comm from emp where comm is null or comm = 0;
   找出工资大于2000且部门编号式20或30的员工
   select ename, deptno, sal from emp where sal > 2000 and deptno in (20, 30);
   tip：
      1. 仍旧是优先级的问题，不确定的话就小括号把紧要的括起来
      2. in 一个区间 ，相当于多个 or
   
1.3 数据排序 order by 语句
    asc 升序(默认)；desc 降序
    按照部门升序排序，薪资降序排序
    select deptno, sal from emp order by deptno, sal desc;
    tip：
        多个字段排序，当第一个字段无法完成排序的情况下（有相等的情况），后续的
        字段才有意义。
1.4 分组 group by 语句
 	group by 根据某个字段，某些字段进行分组
 	having 是对分组后的数据进行再次的过滤
 	关于分组函数 count sum avg max min，分组函数一般是对group by分组后的数据进行处理, 当       没有group by时,整张表看做是一组。分组函数具有以下的特点:
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
   2. 分组函数不能用在 where 语句中
 	   "这是因为 SQL 的执行顺序, group by是在where后执行的, 分组函数
 	   是对分组后的数据做处理, where执行的时候,group by还没执行,没有分组
 	   哪来的处理."
 	   
   3. 关于 null计算为null的问题, ifnull(有null的字段, 指定值) 可以处理
 	   select ename, (sal+ifnull(comm, 0))*12 as yearsalary from emp;
 	
       找出每个部门,  不同岗位最高薪资 > 2500 的
       select deptno, sal from emp group by deptno, sal having max(sal) > 2500;
       select deptno, max(sal) from emp where sal > 2500 group by deptno, sal; 效        率更高,想下为什么.建议分开SQL执
   
       tip: only_full_group_by：使用和oracle一样的 group 规则, select的字段都要在group        中, 或者本身是聚合列(SUM,AVG,MAX,MIN) 才行. 
       
1.5 单表 SQL 的查询顺序
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

------

##### 2. 多表查询 ---- 连接查询

```sql
2.1 连接查询分类
	内连接
		1.等值连接: 表连接关系是等量的
		2.非等值连接: 表连接关系不是等量的
		3.自连接:自己和自己连接, 一张表拆成多张表
	外连接(用的多)
		1.左连接: 左边是主表, 右边是副表
		2.右连接: 右边是主表, 左边是副表
	全连接(相关的业务场景极少见)

2.2 数据库连表的原理
	数据库连表操作其实就是内部对多张表做了一个笛卡尔乘积, 然后通过某些条件去筛选出有效的数据.
	所以如何从现象上避免笛卡尔乘积效应, 加适当的过滤条件, 但加条件并不会减少匹配次数. 匹配次数
	仍旧是 x * y (以两表联查为例, x为A表的记录数, y为B表的记录数), 不过是查询出来的数据都是
	有效数据.
2.3 内连接等值连接
	示例: 查询员工所在的部门信息.
	select
	 	e.ename, d.dname, d.loc
	 from 
	 	emp e
	 join              # 相当于 inner join, inner可以省略
	  	dept d
	  on               # 连接条件
	  	e.deptno = d.deptno;  
	  	
	 注意, 一定要给表起别名, 一是效率高, 二是可读性好.
	 并且 on 条件后还可以在加 where 语句做过滤.
	 
2.4 内连接非等值连接
	示例一:查询每个员工的员工名,工资,工资等级.
	select 
		e.ename, e.sal, s.grade
	from 
		emp e
	join
		salgrade s
	on 
		e.sal between s.losal and s.hisal;
	示例二: 查询工资等级为1的员工姓名,工资信息.		

	select 
		e.ename, e.sal
	from
		emp e
	join 
		salgrade s
	on 
		e.sal between s.losal and s.hisal
	where
		s.grade = 1;
		
2.5 自连接(考验对表中数据的理解)
	示例:显示每个员工的上级.
		select 
			a.ename as'员工名', b.ename as'领导名'
		from 
			emp a
		join 
			emp b
		on
			a.mgr = b.empno;
	""
	如何去理解内连接, 观察表中字段间的关系,并根据关系去想象拆表
	如上示例,根据员工的领导编号即mgr字段可以拆出一个领导表
	a 表 员工表
+-------+--------+
| empno | ename  |
+-------+--------+
|  7369 | SMITH  |
|  7499 | ALLEN  |
|  7521 | WARD   |
|  7566 | JONES  |
|  7654 | MARTIN |
|  7698 | BLAKE  |
|  7782 | CLARK  |
|  7788 | SCOTT  |
|  7839 | KING   |
|  7844 | TURNER |
|  7876 | ADAMS  |
|  7900 | JAMES  |
|  7902 | FORD   |
|  7934 | MILLER |
+-------+--------+
	b 表 领导表
+-------+--------+
| empno | ename  |
+-------+--------+ 
|  7698 | BLAKE  |
|  7782 | CLARK  |
|  7788 | SCOTT  |
|  7839 | KING   |
|  7902 | FORD   |
|  7566 | JONES  |
+-------+--------+

	""
	注意SQL存在问题! 员工 king 也就是大老板的数据没了, 这说明了内连接只显     示匹配到的数据,没有匹配到的不显示.


2.6 外连接和内连接的区别
	外连接: 常分主副表, 主要去查询主表中的数据,捎带查询副表中的数据,当副表	  中的数据没有和主表相匹配的数据,会用 null 进行填充,也就是说外连接尽量保
	正主表数据的完整性.
	内连接: 首先内连接的表没有主副之分, 关系都是对等的.内连接的表根据某种关
    系连接会将匹配到的信息显示出来,没有匹配到的就不显示,也就是说内连接会有
    丢失数据的可能性.
2.7 左右连接
	解决2.5示例的问题: 完整显示每个员工的上级.(包括大老板)
	select 
		a.ename, b.ename
	from 
		emp a
	left join
		emp b
	on
		a.mgr = b.empno;
	如何变成右连接呢?
    select 
		a.ename, b.ename
	from 
		emp b
	right join
		emp a
	on
		a.mgr = b.empno;
    因此,左连接可以写成右连接, 右连接可以写成左连接
   
   示例一: 找出那个部门没有员工
   select
    	d.dname, d.loc
   from 
   	    emp e
   right join
   	   dept d
   on
      e.deptno = d.deptno
   where
   	  e.ename is null;
    
    示例二：找出每一个员工的部门名称及工资等级。
    
```









