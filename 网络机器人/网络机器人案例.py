# 导入所需要的库
import csv
import requests
from lxml import html
import urllib3
import time
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 常量(全大写)
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 设置要爬取的页数
TOTAL_PAGES = 3  # 修改这个数字来设置要爬取的页数

all_movies = []

for page in range(1, TOTAL_PAGES + 1):
    print(f"\n{'=' * 50}")
    print(f"正在爬取第 {page}/{TOTAL_PAGES} 页")
    print(f"{'=' * 50}")

    # 构建分页URL - 所有页都使用相同的URL模板
    if page == 1:
        page_url = TMDB_TOP_URL
    else:
        page_url = f"{TMDB_TOP_URL}?page={page}"

    try:
        response = requests.get(page_url, timeout=60, headers=headers, verify=False)

        # 解析数据，获取电影列表
        document = html.fromstring(response.text)

        # 使用更可靠的XPath查找电影卡片
        movie_cards = document.xpath("//div[contains(@class, 'poster-card')]")
        print(f"找到 {len(movie_cards)} 个电影卡片")

        if not movie_cards:
            print("未找到电影卡片，可能已到达最后一页")
            break

        # 提取电影基本信息和链接
        page_movies = []
        for i, card in enumerate(movie_cards):
            # 提取电影标题
            title_elements = card.xpath(".//img/@alt | .//h2/text() | .//p[@class='title']/text()")
            title = title_elements[0].strip() if title_elements else "未知标题"

            # 提取评分（从榜单页面）
            rating_elements = card.xpath(".//span[contains(@class, 'vote')]/text()")
            rating = rating_elements[0].strip() if rating_elements else ""

            # 提取电影链接
            link_elements = card.xpath(".//a/@href")
            link = link_elements[0] if link_elements else ""
            if link and not link.startswith('http'):
                link = TMDB_BASE_URL + link.lstrip('/')

            movie_info = {
                '排名': (page - 1) * 20 + i + 1,  # 计算总排名
                '标题': title,
                '评分': rating,
                '链接': link
            }
            page_movies.append(movie_info)

        all_movies.extend(page_movies)
        print(f"第 {page} 页获取了 {len(page_movies)} 部电影")

        # 每页之间稍作延迟
        if page < TOTAL_PAGES:
            time.sleep(2)

    except Exception as e:
        print(f"第 {page} 页爬取失败: {str(e)}")
        continue

print(f"\n总共获取了 {len(all_movies)} 部电影的基本信息")

# 3. 访问每个电影详情页获取更多信息
print("\n开始获取电影详细信息...")
for idx, movie in enumerate(all_movies):
    if not movie['链接']:
        continue

    try:
        print(f"\n正在获取第 {idx + 1}/{len(all_movies)} 部电影详情: {movie['标题']}")

        # 添加延时，避免请求过快
        time.sleep(1)

        detail_response = requests.get(movie['链接'], timeout=60, headers=headers, verify=False)
        detail_doc = html.fromstring(detail_response.text)

        # 提取年份 - 从标题中提取 (1994)
        title_with_year = detail_doc.xpath("//h2//text()")
        year = ""
        for text in title_with_year:
            match = re.search(r'\((\d{4})\)', text)
            if match:
                year = match.group(1)
                break
        movie['年份'] = year

        # 提取上映时间 - 从 span.release
        release_elements = detail_doc.xpath("//span[@class='release']/text()")
        movie['上映时间'] = release_elements[0].strip() if release_elements else ""

        # 提取类型（流派）- 从 span.genres
        genre_elements = detail_doc.xpath("//span[@class='genres']//a/text()")
        movie['类型'] = ', '.join([g.strip() for g in genre_elements]) if genre_elements else ""

        # 提取时长 - 从 span.runtime
        runtime_elements = detail_doc.xpath("//span[@class='runtime']/text()")
        movie['时长'] = runtime_elements[0].strip() if runtime_elements else ""

        # 提取评分 - 从 user_score_chart 的 data-percent 属性
        score_chart = detail_doc.xpath("//div[@class='user_score_chart']/@data-percent")
        if score_chart:
            movie['评分'] = score_chart[0] + '%'
        elif not movie['评分']:
            movie['评分'] = ""

        # 提取语言 - bdi元素的父级的后续文本
        bdi_elements = detail_doc.xpath("//bdi[text()='默认语言']")
        if bdi_elements:
            parent = bdi_elements[0].getparent()
            if parent is not None:
                parent_text = parent.tail
                if parent_text:
                    movie['语言'] = parent_text.strip()
                else:
                    movie['语言'] = ""
            else:
                movie['语言'] = ""
        else:
            movie['语言'] = ""

        # 提取导演和编剧 - 查找包含person链接的人物
        person_links = detail_doc.xpath("//a[contains(@href, '/person/')]/text()")
        person_names = [name.strip() for name in person_links if name.strip()]

        # 查找 Director 和 Screenplay 的位置
        all_text = detail_doc.xpath("//text()")
        director_idx = -1
        screenplay_idx = -1

        for i, text in enumerate(all_text):
            if 'Director' in text:
                director_idx = i
            if 'Screenplay' in text:
                screenplay_idx = i

        # 根据位置提取导演和编剧
        if director_idx >= 0 and person_names:
            movie['导演'] = person_names[0] if len(person_names) > 0 else ""
        else:
            movie['导演'] = ""

        if screenplay_idx >= 0 and person_names:
            movie['作者'] = person_names[1] if len(person_names) > 1 else ""
        else:
            movie['作者'] = ""

        print(
            f"  ✓ 获取成功 - 年份:{movie['年份']}, 类型:{movie['类型']}, 时长:{movie['时长']}, 评分:{movie['评分']}, 语言:{movie['语言']}, 导演:{movie['导演']}")

    except Exception as e:
        print(f"  ✗ 获取失败: {str(e)}")
        movie['年份'] = ""
        movie['上映时间'] = ""
        movie['类型'] = ""
        movie['时长'] = ""
        movie['语言'] = ""
        movie['导演'] = ""
        movie['作者'] = ""

# 保存为CSV文件
if all_movies:
    csv_file = '电影榜单.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['排名', '标题', '年份', '上映时间', '类型', '时长', '评分', '语言', '导演', '作者', '链接']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_movies)
    print(f"\n成功保存 {len(all_movies)} 部电影到 {csv_file}")
    print(f"文件位置: {csv_file}")
