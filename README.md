# 🌳 DH 学习体系 · Digital Humanities Learning System

一个为**数字人文（Digital Humanities）学习**打造的单页交互式知识管理工具。以知识树为核心，整合了学习进度追踪、文本批注、富文本笔记和 Python 语法速查四大功能。

> 🎯 面向人群：准备攻读数字人文硕士（如德国德累斯顿工大 DH 项目）的跨学科学习者。

## ✨ 功能特性

| 模块 | 说明 |
| --- | --- |
| 📚 **知识树** | 10 大知识分支、40+ 知识点，覆盖 DH 理论、编程、HCI、数据建模、数字化呈现等 |
| ✅ **技能清单** | 螺旋式复习机制，标记已掌握技能，自动提醒久未复习的条目 |
| 📅 **时间线** | 入学前到毕业 4 个学期的完整学习规划 |
| 📝 **批注系统** | 选中文字右键即可高亮、添加链接、改字体颜色/加粗，并写富文本批注 |
| 📓 **笔记本** | 汇总所有批注 + 内置 Python 语法 5 组速查笔记 |
| 💬 **学习助手** | 内置问答 + 跨知识点搜索 |
| 🌓 **深色模式** | 浅色/深色主题切换 |

## 🚀 在线使用

直接访问 GitHub Pages 地址即可使用（无需安装）：

```
https://youcyhuang.github.io/dh-learning-system/
```

所有进度和批注保存在你浏览器的本地存储（localStorage）中。

## 🛠️ 技术栈

- 纯前端，单文件实现：**HTML + CSS + JavaScript**
- 无需后端、无需构建工具、无第三方依赖
- 数据持久化：`localStorage`
- 富文本编辑：原生 `contenteditable` + `document.execCommand`

## 📁 项目结构

```
dh-learning-system/
├── index.html      # 全部应用（HTML/CSS/JS 内联）
├── README.md       # 项目说明
└── .gitignore      # Git 忽略规则
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
