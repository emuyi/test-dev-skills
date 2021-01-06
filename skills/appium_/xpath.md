```xml
！！pycharm 中有能执行 xpath 表达式的插件(xpathview+xslt)，可以辅助定位。

<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book>
        <title lang="eng" id="1">Harry Potter</title>
        <book>
            <title lang="eng" id="2">Learning XML</title>
            <price>20.95</price>
        </book>
        <price>29.99</price>
    </book>
    <book>
        <title lang="eng">Learning XML</title>
        <price>39.95</price>
    </book>
</bookstore>

xpath 查找元素

常用：
    //title[@lang] 选取属性为lang的所有title元素
    //title[@lang="eng"]
    //book | // *[@lang="eng"]  选取所有的book元素和 属性为lang 且属性值为 eng 的元
    . 当前节点
    .. 当前节点的父节点
    //* 匹配所有的节点
    //*/title[contains(@lang, "e")] 匹配所有lang属性包含 e 的 title 元素
    //*[@lang="eng" and @id] 匹配lang属性值为 eng并还有id属性的所有元素
-------------------------------------------------------------------------------
    绝对定位节点：
        /bookstore 从根节点开始找起
        /bookstore/book 表示根节点下面是book的子节点
    相对定位节点(主用)：
        //book 所有的book子元素，不管在文档中的位置
        //@lang 找到所有为属性为lang的元素，不管位置在哪
	   //book[price > 35] 选取所有的book元素，其中price元素的值 > 35
	   * 匹配任意的元素节点
	   @* 匹配任意的属性节点
        /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
        /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
  
```

