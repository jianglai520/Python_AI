import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


# ==================== 配置部分 ====================
def setup_chinese_font():
    """配置中文字体"""
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False


def create_figure():
    """创建画布和子图"""
    fig, axs = plt.subplots(2, 2, figsize=(20, 12))
    fig.suptitle('TMDB_TOP300电影榜单数据统计', fontsize=20, fontweight='bold', y=0.98)

    ax1: Axes = axs[0, 0]  # 左上：年份趋势
    ax2: Axes = axs[0, 1]  # 右上：语言分布
    ax3: Axes = axs[1, 0]  # 左下：类型分布
    ax4: Axes = axs[1, 1]  # 右下：评分占比

    return fig, ax1, ax2, ax3, ax4


# ==================== 数据加载与处理 ====================
def load_data(filepath='data/movies.csv'):
    """加载电影数据"""
    data = pd.read_csv(
        filepath,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )
    return data


def clean_data(data):
    """清洗数据：填补缺失的年份"""
    missing_years = data['年份'].isnull().sum()
    if missing_years > 0:
        print(f"发现 {missing_years} 条缺失的年份数据，正在从'上映时间'中提取...")
        data['年份'] = data['年份'].fillna(data['上映时间'].str[:4].astype('Int64'))
    return data


# ==================== 图表绘制函数 ====================
def plot_yearly_trend(ax1, data):
    """图表1：每年上映电影数量变化（折线图）"""
    # 统计每年的电影数量
    year_count = data.groupby('年份').size()

    # 生成完整的年份范围
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    all_years = range(min_year, max_year + 1)

    # 组装数据，缺失年份补0
    x_years = list(all_years)
    y_counts = [int(year_count.get(year, 0)) for year in all_years]

    # 绘制折线图
    ax1.plot(x_years, y_counts,
             color='#2196F3',
             linewidth=2,
             linestyle='-',
             marker='o',
             markersize=5,
             markerfacecolor='white',
             markeredgecolor='#2196F3')

    ax1.set_title('每年上映电影数量变化', fontsize=15, pad=10)
    ax1.set_xlabel('年份', fontsize=11)
    ax1.set_ylabel('电影数量', fontsize=11)
    ax1.set_xticks(x_years[::7])
    ax1.set_yticks(range(0, max(y_counts) + 5, 3))
    ax1.grid(linestyle='--', alpha=0.5, color='gray')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)


def plot_language_distribution(ax2, data, top_n=15):
    """图表2：不同语言对应的电影数量（柱状图）"""
    # 统计各语言的电影数量
    language_count = data['语言'].value_counts().head(top_n)

    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()

    # 绘制柱状图
    bars = ax2.bar(x_language, y_language,
                   color='#4CAF50',
                   width=0.7,
                   edgecolor='white',
                   linewidth=0.5)

    # 添加数值标签
    for bar, value in zip(bars, y_language):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{int(value)}',
                 ha='center', va='bottom', fontsize=8)

    ax2.set_title(f'不同语言对应的电影数量（Top{top_n}）', fontsize=15, pad=10)
    ax2.set_xlabel('语言', fontsize=11)
    ax2.set_ylabel('电影数量', fontsize=11)
    ax2.tick_params(axis='x', rotation=65)
    ax2.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)


def plot_type_distribution(ax3, data):
    """图表3：不同类型电影数量（柱状图）"""
    # 统计各类型的电影数量
    type_count = {}
    for types in data['类型'].dropna().str.split(','):
        for movie_type in types:
            movie_type = movie_type.strip()
            if movie_type:
                type_count[movie_type] = type_count.get(movie_type, 0) + 1

    # 按数量排序
    sorted_types = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    x_types = [item[0] for item in sorted_types]
    y_values = [item[1] for item in sorted_types]

    # 绘制柱状图
    bars = ax3.bar(x_types, y_values,
                   color='#FF9800',
                   width=0.7,
                   edgecolor='white',
                   linewidth=0.5)

    # 添加数值标签
    for bar, value in zip(bars, y_values):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{int(value)}',
                 ha='center', va='bottom', fontsize=8)

    ax3.set_title('不同类型的电影数量', fontsize=15, pad=10)
    ax3.set_xlabel('类型', fontsize=11)
    ax3.set_ylabel('电影数量', fontsize=11)
    ax3.tick_params(axis='x', rotation=65)
    ax3.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)


def plot_score_pie(ax4, data, threshold_ratio=0.02):
    """图表4：各个评分的电影占比（饼状图）"""
    # 统计各评分的电影数量
    score_count = data['评分'].value_counts()

    # 合并占比小于阈值的为"其他"
    total_num = score_count.sum()
    threshold = total_num * threshold_ratio

    large_scores = score_count[score_count >= threshold]
    small_scores = score_count[score_count < threshold]

    if len(small_scores) > 0:
        large_scores = pd.concat([
            large_scores,
            pd.Series([small_scores.sum()], index=['其他'])
        ])

    scores = large_scores.index.astype(str).tolist()
    values = large_scores.values.tolist()

    # 定义颜色列表
    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
              '#FF9F40', '#C9CBCF', '#7BC8A4', '#F7464A', '#46BFBD']

    # 绘制饼状图
    wedges, texts, autotexts = ax4.pie(
        values,
        labels=scores,
        autopct='%1.1f%%',
        startangle=90,
        radius=1.0,
        colors=colors[:len(values)],
        pctdistance=0.8,
        textprops={'fontsize': 9}
    )

    # 美化百分比文本
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(8)

    ax4.set_title('各个评分的电影占比', fontsize=15, pad=10)

    # 添加图例
    ax4.legend(
        wedges, scores,
        title="评分",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=9,
        title_fontsize=10
    )


# ==================== 保存与显示 ====================
def save_and_show(fig, save_path='data/movies_statistics1.png'):
    """调整布局、保存图片并显示"""
    plt.subplots_adjust(
        left=0.08,
        right=0.92,
        top=0.93,
        bottom=0.08,
        wspace=0.3,
        hspace=0.45
    )

    plt.savefig(
        save_path,
        bbox_inches='tight',
        dpi=150,
        facecolor='white',
        edgecolor='none'
    )

    print(f"✅ 图表已保存到: {save_path}")
    plt.show()


# ==================== 主函数 ====================
def main():
    """主函数：执行完整的数据分析流程"""
    # 1. 配置中文字体
    setup_chinese_font()

    # 2. 创建画布
    fig, ax1, ax2, ax3, ax4 = create_figure()

    # 3. 加载数据
    print("📊 正在加载数据...")
    data = load_data()

    # 4. 清洗数据
    print("🧹 正在清洗数据...")
    data = clean_data(data)

    # 5. 绘制图表
    print("📈 正在绘制图表...")
    plot_yearly_trend(ax1, data)
    plot_language_distribution(ax2, data)
    plot_type_distribution(ax3, data)
    plot_score_pie(ax4, data)

    # 6. 保存并显示
    print("💾 正在保存图表...")
    save_and_show(fig)

    print("✨ 完成！")


# ==================== 程序入口 ====================
if __name__ == '__main__':
    main()
