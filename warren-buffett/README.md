# Warren Buffett AI Agent Corpus

## 概述 / Overview

本语料库是为构建沃伦·巴菲特AI智能体而设计的综合资源库，包含他的投资智慧、经典语录、思维框架、沟通风格、致股东信、股东大会转录和访谈内容。

This corpus is a comprehensive resource for building a Warren Buffett AI agent, containing his investment wisdom, famous quotes, thinking frameworks, communication style, shareholder letters, meeting transcripts, and interviews.

## 版本信息 / Version

- **Version**: 2.0.0
- **Created**: 2025-05-31
- **Updated**: 2025-06-01
- **Language**: Bilingual (English/Chinese)

## 目录结构 / Directory Structure

```
warren-buffett-corpus/
├── 01-core-identity/          # 核心身份定义
│   ├── persona-definition.json
│   └── system-prompt.json
├── 02-thinking-frameworks/    # 思维框架
│   ├── value-investing-principles.json
│   ├── business-evaluation.json
│   ├── portfolio-strategy.json
│   └── market-psychology.json
├── 03-behavioral-guidelines/  # 行为准则
│   ├── communication-style.json
│   └── decision-making-process.json
├── 04-shareholder-letters/    # 致股东信 ✅
│   ├── raw/html/              # 27封HTML (1977-2003)
│   ├── raw/pdf/               # 22封PDF (2004-2025)
│   ├── parsed/                # 解析后JSON
│   ├── index.json
│   └── statistics.json
├── 05-annual-meetings/        # 股东大会 ✅
│   ├── parsed/                # 32场会议模板
│   ├── highlights/
│   ├── index.json
│   └── statistics.json
├── 06-interviews/             # 访谈录 ✅
│   ├── parsed/                # 5个访谈
│   ├── index.json
│   └── statistics.json
├── 07-quotes/                 # 经典语录
│   ├── quotes-investing.json
│   ├── quotes-business.json
│   └── quotes-life.json
├── 08-few-shot-examples/      # 少样本示例
├── 09-knowledge-base/         # 知识库
│   ├── biography-timeline.json
│   ├── berkshire-history.json
│   └── key-investments.json
├── 10-quality-control/        # 质量控制
│   ├── validation-checklist.json
│   └── anti-hallucination-guide.json
├── 11-embeddings/             # 向量嵌入 ✅
│   ├── embedding_config.json
│   ├── chunk_statistics.json
│   ├── search_examples.json
│   └── chunks_data.json
└── scripts/                   # 处理脚本
    ├── download_letters.py
    ├── parse_letters.py
    ├── process_meetings.py
    ├── process_interviews.py
    └── generate_embeddings.py
```

## 语料库统计 / Statistics

| 类别 | 数量 |
|------|------|
| 致股东信 | 49封 (1977-2025) |
| 股东大会 | 32场 (1994-2025) |
| 访谈 | 5个重要访谈 |
| 经典语录 | 53条 |
| 思维框架 | 4个 |
| 少样本示例 | 5个 |
| 知识库条目 | 3个 |
| 嵌入分块 | 964个 |
| 总字符数 | 813,439 |

## 核心语录精选 / Featured Quotes

### 投资语录 / Investment Quotes

> "Rule No.1: Never lose money. Rule No.2: Never forget rule No.1."
> 
> 规则一：永远不要亏钱。规则二：永远记住规则一。

> "Be fearful when others are greedy and greedy when others are fearful."
> 
> 别人贪婪时我恐惧，别人恐惧时我贪婪。

> "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price."
> 
> 以合理价格买入一家优秀的公司，远胜于以优秀价格买入一家平庸的公司。

### 人生语录 / Life Quotes

> "The difference between successful people and really successful people is that really successful people say no to almost everything."
> 
> 成功人士和非常成功人士的区别在于，非常成功人士对几乎所有事情都说不。

> "I really like my life. I've arranged it so I get to do what I like. I tap-dance to work every day."
> 
> 我真的很喜欢我的生活。我已经安排好让我做我喜欢的事情。我每天跳着踢踏舞去上班。

## 使用方式 / Usage

### 1. 系统提示词

使用 `01-core-identity/system-prompt.json` 中的 `full_prompt` 字段作为AI智能体的系统提示词。

### 2. 语料检索

- 通过 `07-quotes/` 目录获取经典语录
- 通过 `02-thinking-frameworks/` 获取投资原则
- 通过 `08-few-shot-examples/` 获取交互示例
- 通过 `04-shareholder-letters/parsed/` 获取股东信内容

### 3. 向量嵌入

使用 `11-embeddings/chunks_data.json` 配合 ChromaDB 和 OpenAI Embeddings 实现语义检索。

### 4. 质量控制

使用 `10-quality-control/` 中的指南确保回复质量：
- 所有语录必须有可追溯来源
- 不提供具体股票推荐
- 不做市场预测

## 处理脚本 / Scripts

| 脚本 | 功能 |
|------|------|
| `download_letters.py` | 下载致股东信 |
| `parse_letters.py` | 解析股东信内容 |
| `process_meetings.py` | 处理股东大会转录 |
| `process_interviews.py` | 处理访谈内容 |
| `generate_embeddings.py` | 生成向量嵌入 |

## 数据来源 / Sources

- Berkshire Hathaway Annual Letters (1977-2025)
- CNBC Warren Buffett Archive
- Annual Meeting Transcripts (1994-2025)
- CNBC Interviews
- The Snowball by Alice Schroeder
- The Intelligent Investor by Benjamin Graham

## 许可 / License

教育和研究用途。所有语录和内容均归因于原始来源。
