import re

s1 = '18809090000是我的手机号，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗？'
s2 = '我的手机号是18809090000，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗？'

result = re.match(r"1[3-9]\d{9}", s1)  #从字符串的开头开始匹配(返回第一个匹配项)--如果开头匹配不成功，则报错--Match对象
print(result.group())  # group() 返回匹配项--重点关注
print(result.span())  # span() 返回匹配项的索引位置
print(result.start())  # start() 获取匹配项的起始索引位置
print(result.end())  # end() 获取匹配项的结束索引位置
print()

result = re.search(r"1[3-9]\d{9}", s2)    #从任意位置开始，搜索第一个匹配项(返回第一个匹配项)--Match对象
print(result.group())
print(result.span())
print(result.start())
print(result.end())
print()

result = re.findall(r"1[3-9]\d{9}", s1)  #从任意位置开始，搜索所有匹配项(返回list)
print(result)
print(len(result))
print()

# 正则表达式
s3 = "18809900000是我的手机号，188开头的，以0结尾的；我的另一个手机号是15500008888，两个QQ分别是1259989092和13880901293821，邮箱为python666@163.com，请给我发邮件。"
print(re.findall(r"188.*", s3)) # . 匹配任意字符
print(re.findall(r"188.?", s3)) # .? 匹配0个或1个
print(re.findall(r"188.+", s3)) # + 匹配1个或多个
print()


print(re.findall(r"188\d{8}", s3))  #{8} 匹配8个
print(re.findall(r"155\d{6,10}", s3))  # {6,10} 匹配6-10个
print(re.findall(r"155\d{6,}", s3)) # {6,} 匹配6个或更多
print()

print(re.findall(r"1[38]\d{8}", s3)) # [38] 匹配1或3或8
print(re.findall(r"1[^38]\d{8}", s3)) # [^38] 匹配非1或3或8
print(re.findall(r"1[3-9]\d{8}", s3)) # [3-9] 匹配3-9
print(re.findall(r"^1[3-9]\d{9}", s3))  # ^ 匹配开头
print(re.findall(r"^1[3-9]\d{9}$", s3)) # $ 匹配结尾
print()


print(re.findall(r"\w+@\w+\.\w+", s3, re.ASCII))     # \w 匹配任意字符(字母、数字、下划线), re.ASCII 匹配ASCII字符
print()

s4 = "现在的时间是2026-02-06 10:05:25,今天的天气还可以,气温是28度"
print(re.findall(r"\d{4}-\d{2}-\d{2}", s4))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s4))