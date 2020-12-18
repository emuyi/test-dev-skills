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
     数组 arry=(item1 item2 item3...)
     1、数字
     	i=1;echo $i;echo $((i+1))  
  		((i=i+1));echo $i 类似 +=
 三、字符串操作
     1、拼接字符串，直接连着写就行
     name='ellen';echo "hello $name"
     2、获取字符串的长度 ${#name}
     3、提取子字符串 ${name:start:stop}  注意 shell 是前后全包
     4、字符串替换 x='1234567';echo $x | sed 's/2/3/g'
 四、布尔表达式
 	$? 命令的返回值，0 表示正确，非0表示错误
 	见下方流程控制

 五、数组
 	1、数组定义 
 		array=(value1 value2 value3...) 中间用空格隔开
 		或 array[0] = 1
 		   array[1] = 2
 		   .....
 		再或通过命令结果创建数组
           array=(`ls`)
 		
 	2、可以通过索引赋值直接新增值，修改值
 		array[0]=1
 	3、获取数组中的元素、长度
 		所有元素：${array[*]} 或者 ${array[@]} 
 		长度：和获取字符串的长度
 			 数组的长度 ${#array[*]}
 			 数组中元素的长度 ${#array[n]}  
```

##### 三、流程控制

```shell
一、条件判断
if [ condition ];then ....;fi                ！！！ 注意[ condition ] 要加空格
if [ condition ];then....;else...;fi
if [ condition ];then....;elif [ condition ];then ...;eles...;fi

测试条件：
	1、数字判断
	  a) [ 2 -eq 2] / [2 -ne 3]
	   -gt > 、-ge >= 、 -lt < 、-le <=、
	  b) (( 2==2 ))  请用这种形式！！！！
(())是一种数学计算命令，它除了可以进行最基本的加减乘除运算，还可以进行大于、小于、等于等关系运算，以及与、或、非逻辑运算。当 a 和 b 相等时，(( $a == $b ))判断条件成立，进入 if，执行 then 后边的 echo 语句
'''
if (($a >=0 && $a <= 10));then echo '1-10';elif (( $a >10 && $a <= 20));then echo '11~20';elif (( $a >20 && $a <=30));then echo '21-30';else echo 'No';fi
注意！这里只是命令行演示，写脚本的时候注意编码规范。
'''
	2、字符串比较
	   [ $A == $A ]  注意 == 和 != 要加空格
	   [ $A != $B ]
	   [ -n "$A" ] 字符串不为空 
	   [ -z "$A" ] 字符串为空
	   [[ $A == a* ]] 字符串 以 a开头的 
	   [[ $A =~ y$ ]] 字符串 以 y 结尾的
	   
	3、逻辑判断 || && !
        if [] && [] 或 if [] && ();
        if [ $name == 'ellen' ] && (($age==19));then echo 11;else echo 22;fi
	4、文件判断
        -e 判断对象是否存在
        -d 判断对象是否存在，并且为目录
        -f 判断对象是否存在，并且为常规文件
        -L 判断对象是否存在，并且为符号链接
        -h 判断对象是否存在，并且为软链接
        -s 判断对象是否存在，并且长度不为0
        -r 判断对象是否存在，并且可读
        -w 判断对象是否存在，并且可写
        -x 判断对象是否存在，并且可执行
        -O 判断对象是否存在，并且属于当前用户
        -G 判断对象是否存在，并且属于当前用户组
        -nt 判断file1是否比file2新  [ "/data/file1" -nt "/data/file2" ]
        -ot 判断file1是否比file2旧  [ "/data/file1" -ot "/data/file2" ]
        
        如：
            if [ -f a.txt ];then rm -f a.txt;fi 
            if [ ! -d demo ];then mkdir -p demo;fi
			if [ -x bin ];then echo 'echo exit and x';else touch bin; chmod +x bin;fi
            
二、for 循环
	 1、做数字计算；for((i=0;i<10;i++));do echo $i;done
	 2、for .. in ..;do..;done 可以遍历数组，遍历用空格隔开的字符串，或者某个命令的结果
	 array=(1 2 3 4);for i in ${array[*]};do echo $i;done
	 s='hello from the otherside';for i in $s;do echo $i;done
	 for i in $(ls);do echo $i;done
  
三、while 循环 
	i=0;while(($i<10));do echo $i;((i++));done
	i=0;while(($i<10));do echo $i;let i++;done
	
shell 循环也支持 break 或 continue
  
```

##### 四、函数

```shell
func(){
	actions;
	return xx
}
1、传递参数 func 1 2 3 4 5 6 7 8 9 xx
   函数内部是用 $1 $2 .. 分别对应传递的参数。$0 依旧是执行脚本的路径
   1、$#表示参数的个数，$@ 符串显示所有向脚本传递的参数
   2、$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数
   3、$* 和 $@ 的区别
      1、如果没有被双引号括起来，二者没有多大的区别，都是接收所有的参数，类似于 python 的 args
      2、 如果是 "$*", "$@"  "$*" 会将参数合并组成一条传入，"$@" 每个参数是独立的，会依次被传入。
   "
   #!/bin/bash
    f(){
    for i in "$*";do echo $i;done
    for i in "$@";do echo $i;done
    return 2
    }
    f 1 2 3 4 5
	echo $?

	1 2 3 4 5
    1
    2
    3
    4
    5
	2

   "
2、使用 $? 接收返回值，没有返回值，以最后一条命令的结果为返回值。

3、如果给 shell 脚本传参数，$0 代表的是执行脚本的路径，$1, $2, $3 分别指代一次传递的参数，不过最多可以传递 9个参数
```



需补

http://c.biancheng.net/view/739.html

http://c.biancheng.net/view/773.html

http://c.biancheng.net/view/2860.html

https://www.cnblogs.com/shoufeng/p/11388060.html









