# 乔布斯访谈语料索引

## 概述

本索引包含乔布斯智能体语料库中的9篇核心访谈，涵盖1985年至2010年，跨越乔布斯职业生涯的不同阶段。每篇访谈包含Markdown和JSON两种格式的文件。

## 访谈列表

### A级来源（最高价值）

| 编号 | ID | 标题 | 日期 | 时长 | 关键段落数 | 核心主题 |
|------|-----|------|------|------|-----------|---------|
| 1 | `stanford-2005` | 斯坦福大学毕业演讲 | 2005-06-12 | 15分钟 | 11 | 串联点滴、爱与失去、面对死亡、Stay hungry stay foolish |
| 2 | `playboy-1985` | Playboy专访 | 1985-02-01 | 180分钟 | 8 | 技术愿景、苹果vs IBM、财富观、思想的自行车 |
| 3 | `d5-2007` | D5峰会：乔布斯与盖茨对话 | 2007-05-30 | 90分钟 | 8 | 个人电脑历史、设计哲学、技术与人文 |
| 4 | `return-to-apple-1997` | 回归苹果——波士顿Macworld | 1997-08-06 | 30分钟 | 5 | 危机管理、产品线精简、专注战略 |
| 5 | `iphone-launch-2007` | iPhone发布会 | 2007-01-09 | 90分钟 | 6 | 重新定义手机、多点触控、产品发布艺术 |
| 6 | `ipad-launch-2010` | iPad发布会 | 2010-01-27 | 90分钟 | 5 | 第三类设备、后PC时代、品类创造 |
| 7 | `d8-2010` | D8大会访谈 | 2010-06-01 | 75分钟 | 6 | Google竞争、Flash争议、后PC时代、隐私 |

### B级来源（高价值）

| 编号 | ID | 标题 | 日期 | 时长 | 关键段落数 | 核心主题 |
|------|-----|------|------|------|-----------|---------|
| 8 | `60-minutes-2003` | CBS 60 Minutes访谈 | 2003 | 20分钟 | 6 | iPod成功、完美主义、不做焦点小组 |
| 9 | `pbs-1996` | PBS访谈（NeXT时期） | 1996 | 15分钟 | 5 | 失败与重生、互联网愿景、教育改革 |

## 按人生阶段分类

### 早期苹果时代（1976-1985）
- `playboy-1985`：30岁，苹果巅峰时期，Macintosh发布后

### 荒野岁月（1985-1997）
- `pbs-1996`：41岁，NeXT时期，反思失败与学习

### 重振苹果（1997-2006）
- `return-to-apple-1997`：42岁，回归苹果，危机管理
- `60-minutes-2003`：48岁，iPod成功，苹果转型

### 黄金时代（2007-2011）
- `iphone-launch-2007`：51岁，iPhone发布，重新定义手机
- `d5-2007`：52岁，与盖茨历史性对话
- `stanford-2005`：50岁，最经典的毕业演讲
- `ipad-launch-2010`：55岁，iPad发布，后PC时代
- `d8-2010`：55岁，讨论Google竞争与苹果哲学

## 按思维模式索引

| 思维模式 | 相关访谈 |
|---------|---------|
| 直觉思维 / 信任直觉 | stanford-2005, playboy-1985, 60-minutes-2003 |
| 产品哲学 / 体验至上 | d5-2007, d8-2010, 60-minutes-2003, iphone-launch-2007 |
| 极简思维 / 专注 | return-to-apple-1997, stanford-2005 |
| 设计哲学 | d5-2007, d8-2010, ipad-launch-2010 |
| 远见思维 / 技术预测 | playboy-1985, pbs-1996, d5-2007, d8-2010 |
| 热爱驱动 | stanford-2005, d5-2007, 60-minutes-2003, pbs-1996 |
| 韧性思维 / 面对失败 | stanford-2005, pbs-1996, return-to-apple-1997 |
| 死亡意识 / 存在主义 | stanford-2005 |
| 竞争思维 | playboy-1985, d8-2010 |
| 品类创造 | iphone-launch-2007, ipad-launch-2010 |

## 经典语录速查

| 语录 | 来源访谈 |
|------|---------|
| "Stay hungry. Stay foolish." | stanford-2005 |
| "Your time is limited, so don't waste it living someone else's life." | stanford-2005 |
| "The only way to do great work is to love what you do." | stanford-2005 |
| "You can't connect the dots looking forward." | stanford-2005 |
| "It's the bicycle for our minds." | playboy-1985 |
| "I want to put a ding in the universe." | playboy-1985 |
| "Design is really about how something works." | d5-2007 |
| "The intersection of technology and liberal arts." | d5-2007 |
| "It's not the consumers' job to know what they want." | 60-minutes-2003 |
| "Today, Apple is going to reinvent the phone." | iphone-launch-2007 |
| "PCs are going to be like trucks." | d8-2010 |
| "The cure for Apple is not cost-cutting. The cure for Apple is to innovate." | return-to-apple-1997 |
| "We'd rather have fewer products that are great than more products that are mediocre." | d8-2010 |
| "It's the Internet in your pocket." | iphone-launch-2007 |
| "Death is very likely the single best invention of Life." | stanford-2005 |

## 文件结构

```
04-interviews/
├── interviews-index.md          # 本文件
├── interviews-index.json        # JSON格式索引
├── stanford-2005.md             # 斯坦福毕业演讲（Markdown）
├── stanford-2005.json           # 斯坦福毕业演讲（JSON）
├── playboy-1985.md              # Playboy专访（Markdown）
├── playboy-1985.json            # Playboy专访（JSON）
├── d5-2007.md                   # D5峰会对话（Markdown）
├── d5-2007.json                 # D5峰会对话（JSON）
├── 60-minutes-2003.md           # 60 Minutes访谈（Markdown）
├── 60-minutes-2003.json         # 60 Minutes访谈（JSON）
├── d8-2010.md                   # D8大会访谈（Markdown）
├── d8-2010.json                 # D8大会访谈（JSON）
├── pbs-1996.md                  # PBS访谈（Markdown）
├── pbs-1996.json                # PBS访谈（JSON）
├── return-to-apple-1997.md      # 回归苹果（Markdown）
├── return-to-apple-1997.json    # 回归苹果（JSON）
├── iphone-launch-2007.md        # iPhone发布会（Markdown）
├── iphone-launch-2007.json      # iPhone发布会（JSON）
├── ipad-launch-2010.md          # iPad发布会（Markdown）
└── ipad-launch-2010.json        # iPad发布会（JSON）
```

## 统计信息

- **访谈总数**：9篇
- **关键段落总数**：60个
- **可提取语录总数**：56条
- **时间跨度**：1985-2010（25年）
- **A级来源**：7篇
- **B级来源**：2篇
- **乔布斯年龄跨度**：30-55岁
