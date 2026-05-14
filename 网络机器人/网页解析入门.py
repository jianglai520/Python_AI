from lxml import html

# 读取 html 文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_content = f.read()
    # print(html_content)

    document = html.fromstring(html_content)  # 将 HTML 内容转换为 lxml 文档对象


    #解析表头 -- xpath语法
    # th_list = document.xpath("//table/tbody/tr[1]/td/text()")   #注意: xpath 路径格式: //标签名/属性名/属性值,索引索引从1开始
    # print(th_list)


    #遍历表格内容
    tr_list = document.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("td/text()")
        print(td_list)


