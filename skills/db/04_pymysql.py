"""
python连接 mysql 主要有两个模块, pymysql 和 sqlalchemy
    pymysql只是提供了对mysql(MariaDB)数据库的操作功能, 并且功能比较单一
    SQLAlchemy 不仅可以连接 mysql, 也可以操作 postgrepsql等其他数据库, 提供的功能相对比较丰富, 比如数据库连接池之类的.

Django ORM 对象关系映射
    数据库的表（table） --> 类（class）
    记录（record，行数据）--> 对象（object）
    字段（field）--> 对象的属性（attribute）

关于 pymysql:
    根据配置信息使用 pymysql.connect 实例化一个数据库连接对象 connection
    并通过 connection.cursor 实例化一个 cursor对象(类似指针)
    通过 cursor.execute() 执行 SQL 语句.
    1.执行增删改操作的时候, pymysql 默认不是自动提交, 需要使用 connection.commit() 提交
     也就说这其实提供了类似数据库事务的数据安全机制. 即 sql 执行无误的时候 commit, 有误的时候
     可以 rollback() [实现这点可在程序中做逻辑处理如 try..except..之类的]
    2.执行查询操作的时候, pymysql提供了
        fetchall 全取
        fetchone 一次取一条,并且将cursor向下移动
        fetchmany 一次取 n 条, 并且将cursor向下移动 n 位
        返回的结果形式会根据 cursorclass 参数来确定, 如果没有指定cursorclass值,将会以元祖的信息
        来组织返回值, 如果指定 cursorclass=pymsql.cursors.DictCursor 会以字典的形式返回数据结果.
    3. 注意! cursor 和文件对象类似也是需要关闭的, 所以可以用 with 进行上下文管理, 最后, 记得关闭数据
        连接.
    4. pymysql 为了处理sql注入的问题, 在执行 sql 语句的时候提供了 %s 这样的占位符(占位符的形式根据
      传过来的参数的类型确定, 一般 list 和 tuple是 %s, dict 的话是%()s).

"""
import pymysql.cursors

id = [1, 2, 3, 4]
username = ['ellen', 'hank', 'bobby', 'paige']

# 创建数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='xxx',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:
# ------------------- DML 增加/删除/修改------------------

        sql_insert = 'insert into t_user values(%s, %s)'
        sql_delete = 'delete from t_user where username=%s '
        sql_update = 'update t_user set username=%s where id=%s'
        # ret = cursor.execute(sql_insert, (1, 'ellen'))  # 执行单条语句
        # cursor.executemany(sql_insert, list(zip(id, username)))  # 批量执行语句
        # cursor.execute(sql_delete, ('paige', ))
        # try:
        #     cursor.execute(sql_update, ('hank', 3))
        #     connection.commit()  # 默认情况下不是自动提交的
        # except:
        #     connection.rollback()  # 提供了回滚的机制
# ------------------------ DQL 查询--------------------------------
        sql_select = "select id, username from t_user where username like 'h%'"
        cursor.execute(sql_select)
        ret = cursor.fetchall()  # 一次性将所有记录查出来
        # ret = cursor.fetchone() # 一次取一条记录,并且将指针向下移一位
        # ret = cursor.fetchmany(2)   # 一次取多条记录,并且将指针向下移 size 位
        print(ret)
finally:
    connection.close()  # 无论如何要记得关闭连接
