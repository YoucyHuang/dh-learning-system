# 🌳 DH 学习体系 · Digital Humanities Learning System

一个为**数字人文（Digital Humanities）学习**打造的单页交互式知识管理工具。以知识树为核心，整合了学习进度追踪、文本批注、富文本笔记和 Python 语法速查四大功能，支持**中 / 英 / 德三语切换**。

> 🎯 面向人群：准备攻读数字人文硕士（如德国德累斯顿工大 DH 项目）的跨学科学习者。

## 🖼️ 在线演示（Demo）

**直接访问，无需安装：**

```
https://youcyhuang.github.io/dh-learning-system/
```

> 💡 所有进度和批注保存在你浏览器的本地存储（localStorage）中，不会上传到服务器。

## ✨ 功能特性

| 模块 | 说明 |
| --- | --- |
| 🌐 **三语切换** | 界面与知识树标题支持 中文 / English / Deutsch 实时切换 |
| 📚 **知识树** | 10 大知识分支、40+ 知识点，覆盖 DH 理论、编程、HCI、数据建模、数字化呈现等 |
| ✅ **技能清单** | 螺旋式复习机制，标记已掌握技能，自动提醒久未复习的条目 |
| 📅 **时间线** | 入学前到毕业 4 个学期的完整学习规划 |
| 📝 **批注系统** | 选中文字右键即可高亮、添加链接、改字体颜色/加粗，并写**富文本批注** |
| 📓 **笔记本** | 汇总所有批注 + 内置 Python 语法 5 组速查笔记 |
| 💬 **学习助手** | 内置问答 + 跨知识点搜索 |
| 🌓 **深色模式** | 浅色/深色主题切换 |

## 📦 附带项目：文本分析小工具

本仓库还包含一个 **NLP 入门练习项目**（见 [`nlp-text-analysis/`](nlp-text-analysis/)）：

- 🈶 中文分词（jieba）
- 🔢 词频统计
- 📈 柱状图（matplotlib）
- ☁️ 词云（wordcloud）

运行结果示例：

```bash
py -3.10 -m pip install -r nlp-text-analysis/requirements.txt
py -3.10 nlp-text-analysis/analyze.py
```

## 🛠️ 技术栈

**主应用：**
- 纯前端，单文件实现：**HTML + CSS + JavaScript**
- 无需后端、无需构建工具、无第三方依赖
- 国际化（i18n）：自建轻量翻译框架，支持 zh/en/de
- 数据持久化：`localStorage`
- 富文本编辑：原生 `contenteditable` + `document.execCommand`

**NLP 项目：**
- Python 3.10 + jieba + matplotlib + wordcloud

## 📁 项目结构

```
dh-learning-system/
├── index.html            # 主应用（HTML/CSS/JS 内联）
├── README.md             # 项目说明
├── LICENSE               # MIT 协议
├── .gitignore            # Git 忽略规则
└── nlp-text-analysis/    # NLP 文本分析小项目
    ├── analyze.py        # 词频统计 + 词云脚本
    ├── requirements.txt  # Python 依赖
    ├── sample_text.txt   # 样例文本
    ├── README.md         # 子项目说明
    └── output/           # 生成的图表（词云、柱状图）
```

## 🎨 设计理念

这个工具源于一个真实的痛点：数字人文学习跨度极大——从人文理论、编程到法律伦理——传统笔记工具（Notion/Obsidian）的整理成本很高。因此设计目标是：

1. **打开即用**，零整理成本
2. **学习即标注**，阅读过程中随手做批注
3. **螺旋式复习**，对抗遗忘曲线
4. **降低认知负荷**，尤其适合 ADHD 学习者

## 👤 作者

**Youcy Huang** — 研究型艺术家 / 跨媒介创作者，正在申请数字人文方向硕士。

- GitHub: [@YoucyHuang](https://github.com/YoucyHuang)

## 📄 License

MIT License — 欢迎学习、参考、二次开发。
