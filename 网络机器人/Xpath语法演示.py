from lxml import html

# 读取 html 文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_content = f.read()
    # print(html_content)


    # 解析html文本，将其转换为一个html文档对象
    document = html.fromstring(html_content)
    # print(document.text_content())


    # 解析表头 --xpath语法
    # /table/thread/tr/td/text() 从根节点开始搜索
    # //table/tbody/tr/td/text() 从当前节点开始搜索(从父节点开始搜索)
    # th_list = document.xpath("//table/tbody/tr/td/text()")
    # print(th_list)

    # th_list = document.xpath("html/body/div[3]/table/thead/tr/th/text()")
    # print(th_list)

    # th_list = document.xpath("//thead/tr/th/text()")
    # print(th_list)

    # tr[2] 索引索引从1开始,
    # td_list = document.xpath("//tbody/tr[1]/td/text()")
    # print(td_list)

    # for td in td_list:
    #     print(td)

    #last 最后一个元素
    # td_list = document.xpath("//tbody/tr[last()]/td/text()")
    # print(td_list)

    # last -1 倒数第二个元素
    # td_list = document.xpath("//tbody/tr[last()-1]/td/text()")
    # print(td_list)


    # attar@属性选择器
    # p_list = document.xpath("//p[@class]/text()")
    # print(p_list)

    #p[@class = 'xn'] 匹配class属性为xn的p标签
    # p_list = document.xpath("//p[@class = 'xn']/text()")
    # print(p_list)

    # *
    # p_list = document.xpath("//thead/tr/*/text()")
    # print(p_list)

    # @src: 表示匹配src属性
    p_list = document.xpath("//td/img/@src")
    print(p_list)



