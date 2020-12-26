1、取得每个部门最高薪水的人员名称

```sql

select 
	e.deptno, ename, sal
from
	emp e 
join 
	(select deptno, max(sal) as maxsal from emp group by deptno) t 
on e.sal = t.maxsal;
```



2、哪些人的薪水在部门的平均薪水之上

```sql
select e.deptno, ename, sal, t.avgsal from emp e join (select deptno, avg(sal) as avgsal from emp group by deptno) t on e.deptno = t.deptno where e.sal > t.avgsal;
```



3、取得部门中（所有人的）平均的薪水等级

```sql
select deptno, avg(grade) from (select deptno, sal from emp) t join salgrade s on t.sal between s.losal and s.hisal group by deptno;
```

4、不准用组函数（Max），取得最高薪水

```sql
select max(avg) from emp;
"pass"
```

5、取得平均薪水最高的部门的部门编号

```sql
select t.deptno, max(avgsal) from (select deptno, avg(sal) as avgsal from emp group by deptno) t group by t.deptno;
```





