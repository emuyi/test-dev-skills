##### 一、hello world

```shell
#!/bin/bash      #！表示用什么解释器，一般都是 bash, 还有sh
echo "hello world"
```

##### 二、变量和基本数据类型

```shell
一、变量
    1、变量命名
        num=1
        welcome="hello from the otherside"
     注意:
        =左右不能有空格
        双引号支持转义，$开头的变量会被自动替换。
     2、使用变量
        echo $welcome
        echo ${welcome} 更严谨
        注意：变量不需要定义也可以被引用，未引用的变量默认是空值。
     3、系统变量
        $HOME
        $PWD
        ~ ：家目录
        $PATH
        $RNADOM 随机数
      4、执行命令并把结果保存为变量
        ret=$(ls)
        ret=`ls`
      5、设置只读变量
        readonly x
二、数据类型
     数字 123
     字符串 "hello" 或 '$a'
     布尔值 true false
     数组 arry=(item1,item2,item3...)
     1、数字
     	i=1;echo $i;echo $((i+1))  !!!
  		((i=i+1));echo $i 类似 +=
 三、字符串操作
     1、拼接字符串，直接连着写就行
     name='ellen';echo "hello $name"
     2、获取字符串的长度 ${#name}
     3、提取子字符串 ${name:start:stop}  注意 shell 是前后全包
     4、字符串替换 x='1234567';echo $x | sed 's/2/3/g'
 四、布尔表达式
 	$? 命令的返回值，0 表示正确，非0表示错误
 	 1、整数比较
 	 先pass

 五、数组
 	
 	   
```



##### 三、流程控制

##### 四、函数







