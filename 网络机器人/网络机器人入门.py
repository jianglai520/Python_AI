import requests as re
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求获取数据
response = re.get(target_url)

# 解析数据(输出数据到控制台)
# print(response.text)

# 将数据转换为html文档对象
document = html.fromstring(response.text)


# 解析数据
# 解析表头
th_list = document.xpath("//table[@id ='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格中的数据
tr_list = document.xpath("//table[@id ='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)

