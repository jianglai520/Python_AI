# 导入所需要的库
import csv  # CSV文件操作模块，用于将数据保存为CSV格式
import requests  # HTTP请求库，用于发送网络请求获取网页内容
from lxml import html  # HTML解析库，lxml的html模块用于解析HTML文档并使用XPath提取数据
import urllib3  # HTTP客户端库，这里主要用于禁用SSL警告
import time  # 时间模块，用于添加延时避免请求过快
import re  # 正则表达式模块，用于文本匹配和提取

# 禁用urllib3的SSL证书验证警告（因为我们使用了verify=False）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==================== 常量定义 ====================
# 常量通常使用全大写字母命名，这是Python的命名规范
TMDB_BASE_URL = "https://www.themoviedb.org/"  # TMDB网站基础URL
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"  # 电影榜单页面URL

# ==================== 请求头设置 ====================
# headers模拟浏览器访问，避免被网站识别为爬虫而拒绝访问
# User-Agent是HTTP请求头的一部分，告诉服务器客户端的信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


# ==================== 爬取配置 ====================
TOTAL_PAGES = 3  # 设置要爬取的页数，修改这个数字可以控制爬取范围

# ==================== 数据存储 ====================
# 使用列表存储所有电影信息，每个电影是一个字典
all_movies = []

# ==================== 第一阶段：爬取榜单页面，获取电影基本信息 ====================
# 使用for循环遍历每一页，range(1, TOTAL_PAGES + 1)生成从1到TOTAL_PAGES的序列
for page in range(1, TOTAL_PAGES + 1):
    # f-string格式化字符串，{}内的表达式会被计算并替换
    # '=' * 50 表示重复'='字符50次，用于打印分隔线
    print(f"\n{'=' * 50}")
    print(f"正在爬取第 {page}/{TOTAL_PAGES} 页")
    print(f"{'=' * 50}")

    # 构建分页URL
    # 第一页直接使用基础URL，其他页添加?page=参数
    # 这是常见的分页URL格式，如：?page=2, ?page=3
    if page == 1:
        page_url = TMDB_TOP_URL
    else:
        # f-string中可以使用变量，{page}会被替换为实际的页码
        page_url = f"{TMDB_TOP_URL}?page={page}"

    # try-except异常处理：捕获网络请求可能出现的错误
    # 如果某页爬取失败，不会导致整个程序崩溃，而是继续爬取下一页
    try:
        # 发送HTTP GET请求获取网页内容
        # timeout=60: 超时时间60秒，防止请求一直等待
        # headers=headers: 添加请求头，模拟浏览器访问
        # verify=False: 跳过SSL证书验证（解决HTTPS网站的证书问题）
        response = requests.get(page_url, timeout=60, headers=headers, verify=False)

        # 解析HTML文档
        # html.fromstring()将HTML字符串转换为可查询的DOM树结构
        document = html.fromstring(response.text)

        # 使用XPath提取电影卡片元素
        # XPath是一种在XML/HTML文档中查找信息的语言
        # //div: 选择所有div元素（不论层级）
        # contains(@class, 'poster-card'): 筛选class属性包含'poster-card'的元素
        # 这个XPath会返回所有符合条件的div元素列表
        movie_cards = document.xpath("//div[contains(@class, 'poster-card')]")
        print(f"找到 {len(movie_cards)} 个电影卡片")

        # 如果没有找到电影卡片，说明可能已到达最后一页
        if not movie_cards:
            print("未找到电影卡片，可能已到达最后一页")
            break  # break语句跳出循环，停止爬取

        # 临时列表，存储当前页面的电影
        page_movies = []

        # enumerate()函数同时获取索引和元素
        # i是索引（从0开始），card是当前电影卡片元素
        for i, card in enumerate(movie_cards):
            # XPath提取电影标题
            # .//img/@alt: 在当前元素下查找img标签的alt属性
            # .//h2/text(): 查找h2标签的文本内容
            # .//p[@class='title']/text(): 查找class为'title'的p标签的文本
            # | 是XPath的"或"运算符，表示匹配任意一个
            # 返回的是一个列表，按XPath表达式的顺序包含所有匹配结果
            title_elements = card.xpath(".//img/@alt | .//h2/text() | .//p[@class='title']/text()")

            # 条件表达式（三元运算符）
            # 如果title_elements非空，取第一个元素并去除首尾空白
            # 否则使用默认值"未知标题"
            title = title_elements[0].strip() if title_elements else "未知标题"

            # 提取评分（从榜单页面的投票数）
            rating_elements = card.xpath(".//span[contains(@class, 'vote')]/text()")
            rating = rating_elements[0].strip() if rating_elements else ""

            # 提取电影详情页链接
            link_elements = card.xpath(".//a/@href")  # 获取a标签的href属性
            link = link_elements[0] if link_elements else ""

            # 如果链接不是完整的URL（不以http开头），则拼接基础URL
            # lstrip('/') 去除开头的斜杠
            if link and not link.startswith('http'):
                link = TMDB_BASE_URL + link.lstrip('/')

            # 创建电影信息字典
            # 排名计算公式：(当前页-1) * 每页数量 + 当前索引 + 1
            # 例如：第2页第3个电影，排名 = (2-1)*20 + 3 + 1 = 24
            movie_info = {
                '排名': (page - 1) * 20 + i + 1,
                '标题': title,
                '评分': rating,
                '链接': link
            }
            page_movies.append(movie_info)  # 将电影信息添加到当前页列表

        # extend()方法将一个列表的所有元素添加到另一个列表
        all_movies.extend(page_movies)
        print(f"第 {page} 页获取了 {len(page_movies)} 部电影")

        # 每页之间添加延时，避免请求频率过高被封禁
        # time.sleep(2) 暂停2秒
        if page < TOTAL_PAGES:
            time.sleep(2)

    # 捕获所有类型的异常，并打印错误信息
    except Exception as e:
        print(f"第 {page} 页爬取失败: {str(e)}")
        continue  # continue跳过本次循环，继续下一次循环

print(f"\n总共获取了 {len(all_movies)} 部电影的基本信息")

# ==================== 第二阶段：访问每个电影详情页，获取详细信息 ====================
print("\n开始获取电影详细信息...")

# 遍历所有电影，获取详细信息
for idx, movie in enumerate(all_movies):
    # 如果链接为空，跳过这部电影
    if not movie['链接']:
        continue

    try:
        print(f"\n正在获取第 {idx + 1}/{len(all_movies)} 部电影详情: {movie['标题']}")

        # 每次请求前延时1秒，降低请求频率
        time.sleep(1)

        # 发送GET请求获取电影详情页内容
        detail_response = requests.get(movie['链接'], timeout=60, headers=headers, verify=False)
        detail_doc = html.fromstring(detail_response.text)

        # 【提取年份】
        # 从页面标题中提取年份，格式如 "(1994)"
        # //h2//text(): 获取所有h2标签及其子元素的文本内容
        title_with_year = detail_doc.xpath("//h2//text()")
        year = ""
        # 遍历所有文本，使用正则表达式查找年份
        for text in title_with_year:
            # re.search()在文本中搜索匹配的模式
            # r'\((\d{4})\)' 是正则表达式：
            #   \( 匹配左括号
            #   (\d{4}) 捕获组，匹配4位数字
            #   \) 匹配右括号
            # match.group(1) 获取第一个捕获组的内容（即4位数字）
            match = re.search(r'\((\d{4})\)', text)
            if match:
                year = match.group(1)
                break  # 找到后跳出循环

        movie['年份'] = year

        # 【提取上映时间】
        # //span[@class='release']/text(): 查找class为'release'的span标签的文本
        release_elements = detail_doc.xpath("//span[@class='release']/text()")
        movie['上映时间'] = release_elements[0].strip() if release_elements else ""

        # 【提取电影类型】
        # //span[@class='genres']//a/text(): 查找genres下的所有a标签的文本
        genre_elements = detail_doc.xpath("//span[@class='genres']//a/text()")
        # join()方法将列表用指定分隔符连接成字符串
        # [g.strip() for g in genre_elements] 是列表推导式，对每个元素去除空白
        movie['类型'] = ', '.join([g.strip() for g in genre_elements]) if genre_elements else ""

        # 【提取时长】
        runtime_elements = detail_doc.xpath("//span[@class='runtime']/text()")
        runtime_elements= runtime_elements[0].strip() if runtime_elements else ""
        h_res = re.search(r"(\d+)h",runtime_elements)
        m_res = re.search(r"(\d+)m", runtime_elements)
        h = int(h_res.group(1)) if h_res else 0
        m = int(m_res.group(1)) if m_res else 0

        movie['时长'] = h * 60 + m


        # 【提取评分】
        # @data-percent: XPath获取属性的语法，获取data-percent属性的值
        score_chart = detail_doc.xpath("//div[@class='user_score_chart']/@data-percent")
        if score_chart:
            # 将百分比数值加上'%'符号
            movie['评分'] = score_chart[0] + '%'
        elif not movie['评分']:
            movie['评分'] = ""

        # 【提取语言】
        # 查找包含"默认语言"文本的bdi元素
        bdi_elements = detail_doc.xpath("//bdi[text()='默认语言']")
        if bdi_elements:
            # getparent()获取父元素
            parent = bdi_elements[0].getparent()
            if parent is not None:
                # tail属性获取元素后面的文本（同级后续文本）
                # 例如：<strong><bdi>默认语言</bdi></strong> 英语
                # parent.tail 就是 " 英语"
                parent_text = parent.tail
                if parent_text:
                    movie['语言'] = parent_text.strip()
                else:
                    movie['语言'] = ""
            else:
                movie['语言'] = ""
        else:
            movie['语言'] = ""

        # 【提取导演和编剧】
        # 查找所有指向人物页面的链接（href包含'/person/'）
        person_links = detail_doc.xpath("//a[contains(@href, '/person/')]/text()")
        # 列表推导式 + 条件过滤：只保留非空的姓名，并去除空白
        person_names = [name.strip() for name in person_links if name.strip()]

        # 获取页面所有文本内容，用于定位Director和Screenplay的位置
        all_text = detail_doc.xpath("//text()")
        director_idx = -1  # 记录"Director"文本的索引位置
        screenplay_idx = -1  # 记录"Screenplay"文本的索引位置

        # 遍历所有文本，查找关键词位置
        for i, text in enumerate(all_text):
            if 'Director' in text:  # 如果文本包含"Director"
                director_idx = i
            if 'Screenplay' in text:  # 如果文本包含"Screenplay"
                screenplay_idx = i

        # 根据位置提取导演和编剧
        # 逻辑：如果找到了Director关键词，且有人物列表，则第一个人物通常是导演
        if director_idx >= 0 and person_names:
            movie['导演'] = person_names[0] if len(person_names) > 0 else ""
        else:
            movie['导演'] = ""

        # 如果找到了Screenplay关键词，且人物列表有至少2人，则第二个人物通常是编剧
        if screenplay_idx >= 0 and person_names:
            movie['作者'] = person_names[1] if len(person_names) > 1 else ""
        else:
            movie['作者'] = ""

        # 打印成功信息，显示提取到的关键字段
        print(
            f"  ✓ 获取成功 - 年份:{movie['年份']}, 类型:{movie['类型']}, 时长:{movie['时长']}, 评分:{movie['评分']}, 语言:{movie['语言']}, 导演:{movie['导演']}")

    # 异常处理：如果某部电影详情获取失败，设置所有字段为空字符串
    except Exception as e:
        print(f"  ✗ 获取失败: {str(e)}")
        movie['年份'] = ""
        movie['上映时间'] = ""
        movie['类型'] = ""
        movie['时长'] = ""
        movie['语言'] = ""
        movie['导演'] = ""
        movie['作者'] = ""

# ==================== 第三阶段：保存数据到CSV文件 ====================
if all_movies:
    csv_file = '电影榜单3.csv'

    # open()打开文件
    # 'w': 写入模式，如果文件存在则覆盖
    # newline='': 防止CSV文件出现多余的空行
    # encoding='utf-8-sig': UTF-8编码带BOM，Excel打开时不会乱码
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        # 定义CSV文件的列名（表头）
        fieldnames = ['排名', '标题', '年份', '上映时间', '类型', '时长', '评分', '语言', '导演', '作者', '链接']

        # DictWriter: 字典写入器，可以将字典列表直接写入CSV
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()  # 写入表头（列名）
        writer.writerows(all_movies)  # 写入所有数据行

    print(f"\n成功保存 {len(all_movies)} 部电影到 {csv_file}")
    print(f"文件位置: {csv_file}")
