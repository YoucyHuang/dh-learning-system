# -*- coding: utf-8 -*-
"""
文本分析小工具 — 词频统计 + 词云
================================
数字人文入门练习：读入一段文字，统计高频词，画出柱状图和词云。

用法：
    python analyze.py                    # 分析默认的 sample_text.txt
    python analyze.py 我的文章.txt       # 分析你自己的文本文件

输出：
    output/top_words.csv      前 50 个高频词（可用 Excel 打开）
    output/frequency.png      高频词柱状图
    output/wordcloud.png      词云图
"""

import sys
import os
import csv
from collections import Counter

# ── 第三方库（需要先 pip install，见 requirements.txt）──
try:
    import jieba
    import matplotlib
    matplotlib.use("Agg")  # 不弹窗，直接存图片
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
except ImportError as e:
    print("缺少依赖库，请先运行：py -3.10 -m pip install -r requirements.txt")
    raise e


# ── 中文停用词：这些词太常见，没有分析价值 ──
STOPWORDS = set("""
的 了 是 在 我 有 和 就 不 人 都 一 一个 上 也 很 到 说 要 去 你 会 着 没有 看 好 自己 这 那 它 我们 他们 她们 什么 怎么 为什么 因为 所以 但是 而且 如果 然后 可以 应该 需要 这个 那个 这些 那些 以及 与 或 等 并 被 把 让 从 对 于 之 中 为 而 及 又 亦 更 还 已经 正在 一直 不是 只是 就是 还是 但是 却 但是 如果 那么 这 个 里 呢 吧 啊 呀 吗
""".split())

# 英文停用词（常见虚词：冠词、介词、连词、代词、助动词等）
ENGLISH_STOPWORDS = set("""
the a an and or but if then else of to in on at for with by from is are was were be been being
it its this that these those as not no yes i you he she we they them their his her my your our
me him us who what which when where why how all any both each few more most other some such
only own same so than too very can will just should now also do does did have has had may might
must shall would could into upon within without between among through during about above below
under over after before while until against because therefore however although though since
""".split())

# 全部停用词合并
STOPWORDS |= ENGLISH_STOPWORDS


def read_text(filepath):
    """读取文本文件，返回字符串。"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text):
    """
    分词：把一段连续的文字切成一个个词语。
    中文没有空格，所以用 jieba 自动切分。
    """
    words = jieba.lcut(text)
    result = []
    for w in words:
        w = w.strip().lower()  # 英文转小写（The 和 the 算同一个词）；中文不受影响
        # 过滤：太短的词、纯标点、纯数字、停用词
        if len(w) < 2:
            continue
        if w in STOPWORDS:
            continue
        if w.isdigit():
            continue
        # 过滤纯标点符号（如 "，" "。" "："）
        if not any(c.isalnum() or '\u4e00' <= c <= '\u9fff' for c in w):
            continue
        result.append(w)
    return result


def count_frequency(words, top_n=50):
    """统计词频，返回 [(词, 次数), ...]，按次数从高到低排序。"""
    counter = Counter(words)
    return counter.most_common(top_n)


def save_csv(freq_list, outpath):
    """把词频结果存成 CSV，方便用 Excel 查看。"""
    with open(outpath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["排名", "词语", "出现次数"])
        for i, (word, count) in enumerate(freq_list, start=1):
            writer.writerow([i, word, count])


def draw_bar_chart(freq_list, outpath):
    """画柱状图：横轴是词语，纵轴是出现次数。"""
    words = [w for w, _ in freq_list]
    counts = [c for _, c in freq_list]

    # 让中文字体能正常显示
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(range(len(words)), counts, color="#8b5e3c")
    ax.set_xticks(range(len(words)))
    ax.set_xticklabels(words, rotation=60, ha="right", fontsize=9)
    ax.set_ylabel("出现次数")
    ax.set_title("高频词统计（Top %d）" % len(words))
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close(fig)
    print("  ✓ 柱状图已保存：", outpath)


def draw_wordcloud(freq_dict, outpath):
    """画词云：词越大，说明出现越频繁。"""
    font_path = r"C:\Windows\Fonts\msyh.ttc"  # 微软雅黑，Windows 自带
    wc = WordCloud(
        font_path=font_path,
        width=1200,
        height=600,
        background_color="white",
        max_words=100,
        colormap="copper",
    )
    wc.generate_from_frequencies(freq_dict)
    wc.to_file(outpath)
    print("  ✓ 词云已保存：", outpath)


def main():
    # 1. 读取文件（命令行可以指定文件，否则用默认样例）
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "sample_text.txt"

    if not os.path.exists(filepath):
        print("找不到文件：", filepath)
        print("请确认文件存在，或运行：python analyze.py 你的文件.txt")
        return

    print("正在分析：", filepath)

    # 2. 确保输出目录存在
    os.makedirs("output", exist_ok=True)

    # 3. 分词
    text = read_text(filepath)
    words = tokenize(text)
    print("  共切分出", len(words), "个有效词语")

    # 4. 统计词频
    freq_list = count_frequency(words, top_n=50)
    freq_dict = {w: c for w, c in freq_list}

    print("\n===== 高频词 Top 20 =====")
    for i, (word, count) in enumerate(freq_list[:20], start=1):
        bar = "█" * (count // 2)
        print(f"{i:2d}. {word:<8} {count:3d} 次  {bar}")

    # 5. 保存结果
    save_csv(freq_list, "output/top_words.csv")
    print("\n  ✓ 词频 CSV 已保存：output/top_words.csv")

    draw_bar_chart(freq_list[:20], "output/frequency.png")
    draw_wordcloud(freq_dict, "output/wordcloud.png")

    print("\n完成！去 output/ 文件夹查看结果吧。")


if __name__ == "__main__":
    main()
