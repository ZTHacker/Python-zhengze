import re

#re.match(pattern, string, flags=0)

#print(re.match('www','www.baidu.com').span())  #在起始位置匹配
#print(re.match('com','www.baidu.com'))   #不在起始位置匹配

#line = "Cats are smarter than dogs"
#.*表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
#matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#re.I表示忽略大小写

#if matchObj:
#	print("matchObj.group():",matchObj.group()) #group(num=0)默认的时候
#	print("matchObj.group():",matchObj.group(1))
#	print("matchObj.group():",matchObj.group(2))
#else:
#	print("No match!!")

#re.search 扫描整个字符串并返回第一个成功的匹配
#re.search(pattern, string, flags=0)

#print(re.search('www','www.baidu.com').span())
#print(re.search('com','www.baidu.com').span())

#line = "Cats are smarter than dogs";
 
#searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
#if searchObj:
#   print ("searchObj.group() : ", searchObj.group())
#   print ("searchObj.group(1) : ", searchObj.group(1))
#   print ("searchObj.group(2) : ", searchObj.group(2))
#else:
#   print ("Nothing found!!")

 #####re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

#检索和替换
#re.sub(pattern,repl,string,count=0)
#pattern:正则中的模式字符串
#repl:替换的字符串，也可以为一个函数
#string:要被查找替换的原始字符串
#count:模式匹配后的替换的最大次数，默认0表示替换所有的匹配

#phone = "2004-959-559 # 这是一个电话号码"

#删除注释
#num = re.sub(r'#.*$',"",phone)
#print("电话号码：",num)

#移除非数字内容
#num = re.sub(r'\D',"",phone)
#print("电话号码：",num)


#findall  在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如没有找到，则返回一个空的列表
#match和search是匹配一次findall匹配所有
#findall(string[, pos[, endpos]])

#pos 可选参数，指定字符串的起始位置
#endpos 可选参数，指定字符串的结束位置，默认为字符串的长度、


#pattern = re.compile(r'\d+')  #查找数字
#result1 = pattern.findall('runoob 123 google 456')
#result2 = pattern.findall('run88oob123google456',0,10)

#print(result1)
#print(result2)


###re.finditer()  和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
#re.finditer(pattern,string,flags=0)

#it = re.finditer(r'\d+','12a32bc43jf3')
#for match in it:
#	print(match.group())


#re.split() split方法按照能够匹配的子串将字符串分割后返回列表
#re.split(pattern,string[,maxsplit=0,flags=0])

#maxsplit  分割次数，maxsplit=1 分割一次，默认为0,不限次数
#flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等


#注：re返回的是正则表达式对象，所以用时可能要强制类型转换

#正则表达式修饰符 - 可选标志

#修饰符	描述
#re.I	使匹配对大小写不敏感
#re.L	做本地化识别（locale-aware）匹配
#re.M	多行匹配，影响 ^ 和 $
#re.S	使 . 匹配包括换行在内的所有字符
#re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
#re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。


#正则表达式模式

#模式	描述
#^	匹配字符串的开头
#$	匹配字符串的末尾。
#.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
#[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
#re*	匹配0个或多个的表达式。
#re+	匹配1个或多个的表达式。
#re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
#re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
#re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
#re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
#a| b	匹配a或b
#(re)	匹配括号内的表达式，也表示一个组
#(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
#(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
#(?: re)	类似 (...), 但是不表示一个组
#(?imx: re)	在括号中使用i, m, 或 x 可选标志
#(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
#(?#...)	注释.
#(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
#(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
#(?> re)	匹配的独立模式，省去回溯。
#\w	匹配数字字母下划线
#\W	匹配非数字字母下划线
#\s	匹配任意空白字符，等价于 [\t\n\r\f]。
#\S	匹配任意非空字符
#\d	匹配任意数字，等价于 [0-9]。
#\D	匹配任意非数字
#\A	匹配字符串开始
#\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
#\z	匹配字符串结束
#\G	匹配最后匹配完成的位置。
#\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
#\n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
#\1...\9	匹配第n个分组的内容。
#\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。



