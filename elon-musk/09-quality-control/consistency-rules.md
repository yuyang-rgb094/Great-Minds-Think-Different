# 一致性规则 / Consistency Rules

## 概述 / Overview

本文档定义了维护 Elon Musk AI Agent Corpus 一致性的规则集合。这些规则确保整个语料库在翻译、风格、格式和来源引用方面保持统一，从而提高数据质量和AI代理的训练效果。

This document defines a set of rules for maintaining consistency across the Elon Musk AI Agent Corpus. These rules ensure uniformity across the corpus in translation, style, formatting, and source attribution, thereby improving data quality and AI agent training effectiveness.

---

## 1. 翻译一致性 / Translation Consistency

### 1.1 关键术语表 / Key Terminology Glossary

以下术语必须在整个语料库中保持一致的翻译：

The following terms must maintain consistent translations throughout the corpus:

| 英文 / English | 中文 / Chinese | 备注 / Notes |
|----------------|----------------|--------------|
| Full Self-Driving | 完全自动驾驶 | 非"全自动驾驶" |
| Autopilot | 自动辅助驾驶 | Tesla标准功能 |
| Neuralink | Neuralink | 保留品牌名 |
| The Boring Company | The Boring Company | 保留品牌名 |
| SpaceX | SpaceX | 保留品牌名 |
| Tesla | 特斯拉 | 首次出现可保留英文 |
| xAI | xAI | 保留品牌名 |
| Grok | Grok | 保留产品名 |
| Grok Heavy | Grok Heavy | 2025年新模型 |
| Optimus | Optimus | Tesla机器人 |
| Cybertruck | Cybertruck | 保留产品名 |
| Starship | 星舰 | SpaceX火箭 |
| Falcon | 猎鹰 | 猎鹰9号/重型 |
| Dragon | 龙飞船 | Crew Dragon等 |
| DOGE | DOGE/政府效率部 | 首次出现需全称 |
| Department of Government Efficiency | 政府效率部 | 全称 |
| Mars Colony | 火星殖民地 | 定居点概念 |
| Multiplanetary | 多行星物种 | 成为多行星物种 |
| Sustainable Energy | 可持续能源 | 能源概念 |
| Artificial General Intelligence | 通用人工智能 | AGI全称 |
| AGI | 通用人工智能/AGI | 根据上下文 |
| Brain-Computer Interface | 脑机接口 | BCI全称 |
| BCI | 脑机接口/BCI | 根据上下文 |
| First Principles | 第一性原理 | 思维方法 |
| Manufacturing | 制造业/生产制造 | 根据上下文 |
| Supply Chain | 供应链 | 商业术语 |
| Vertical Integration | 垂直整合 | 商业策略 |
| Economies of Scale | 规模经济 | 经济学术语 |

### 1.2 公司名和产品名规则 / Company and Product Name Rules

**规则 1.2.1: 品牌名保留**
- 所有公司品牌名保留原始英文
- 首次出现时可在括号内添加中文说明
- 示例: "xAI (埃隆·马斯克的人工智能公司)"

**Rule 1.2.1: Brand Name Preservation**
- All company brand names retain original English
- Chinese explanation may be added in parentheses on first occurrence
- Example: "xAI (Elon Musk's AI company)"

**规则 1.2.2: 产品名处理**
- 有官方中文名的产品使用官方译名
- 无官方中文名的产品保留英文
- 示例: "Model S" → "Model S" (保留), "Cybertruck" → "Cybertruck" (保留)

**Rule 1.2.2: Product Name Handling**
- Products with official Chinese names use official translations
- Products without official Chinese names retain English
- Example: "Model S" → "Model S" (retained), "Cybertruck" → "Cybertruck" (retained)

**规则 1.2.3: 技术术语统一**
- 技术缩写首次出现必须展开
- 后续使用可根据上下文选择缩写或全称
- 示例: "Full Self-Driving (FSD)" 首次出现，后续可用 "FSD"

**Rule 1.2.3: Technical Terminology Uniformity**
- Technical acronyms must be expanded on first occurrence
- Subsequent usage may use acronym or full form based on context
- Example: "Full Self-Driving (FSD)" on first occurrence, then "FSD"

### 1.3 常见表达翻译对照 / Common Expression Translation Reference

| 英文表达 / English Expression | 推荐翻译 / Recommended Translation | 避免使用 / Avoid Using |
|-------------------------------|-----------------------------------|------------------------|
| To be honest | 说实话/老实说 | 诚实地说 |
| The thing is | 问题是/关键是 | 事情是 |
| At the end of the day | 归根结底/说到底 | 在一天结束时 |
| Going forward | 今后/未来 | 向前进 |
| In terms of | 就...而言/在...方面 | 在...条款中 |
| Kind of | 有点/某种程度上 | 种类 |
| Sort of | 算是/某种程度上 | 分类 |
| Pretty much | 基本上/差不多 | 非常漂亮 |
| I mean | 我是说/我的意思是 | - |
| You know | 你知道/要知道 | - |
| Right? | 对吧？/对吗？ | 正确？ |
| Basically | 基本上/本质上 | 基础地 |
| Literally | 字面意义上/确实 | 文学地 |
| Figuratively | 比喻意义上 | 形象地 |
| Insane | 疯狂的/不可思议的 | 疯癫的 |
| Crazy | 疯狂的/离谱的 | 精神错乱的 |
| Next level | 下一个层次/更高水平 | 下一关 |
| Game changer | 游戏规则改变者/颠覆者 | 游戏改变者 |
| Paradigm shift | 范式转变/模式转变 | 范式转移 |

---

## 2. 风格标记一致性 / Style Marker Consistency

### 2.1 Musk 口头禅使用规范 / Musk Catchphrase Usage Standards

**规则 2.1.1: "Literally" 使用**
- 用于强调真实性，非字面意义
- 中文翻译: "字面意义上"、"确实"、"真的"
- 保持原文中的强调语气

**Rule 2.1.1: "Literally" Usage**
- Used to emphasize truthfulness, not literal meaning
- Chinese translation: "字面意义上", "确实", "真的"
- Maintain the emphatic tone from the original

**规则 2.1.2: "The thing is" 使用**
- 用于引出关键观点或转折
- 中文翻译: "问题是"、"关键是"、"事实是"
- 保持口语化风格

**Rule 2.1.2: "The thing is" Usage**
- Used to introduce key points or transitions
- Chinese translation: "问题是", "关键是", "事实是"
- Maintain colloquial style

**规则 2.1.3: "Fundamentally" 使用**
- 用于强调根本原因或本质
- 中文翻译: "从根本上"、"本质上"、"归根结底"
- 保持哲学性思考语气

**Rule 2.1.3: "Fundamentally" Usage**
- Used to emphasize root causes or essence
- Chinese translation: "从根本上", "本质上", "归根结底"
- Maintain philosophical thinking tone

**规则 2.1.4: "Insane/Next level" 等感叹词**
- 用于表达强烈情感或赞美
- 中文翻译: "疯狂的"、"不可思议的"、"下一个层次"
- 保持热情夸张的语气

**Rule 2.1.4: "Insane/Next level" Exclamations**
- Used to express strong emotions or praise
- Chinese translation: "疯狂的", "不可思议的", "下一个层次"
- Maintain enthusiastic, exaggerated tone

### 2.2 情感标记一致性 / Emotion Marker Consistency

| 标记类型 / Marker Type | 英文示例 / English Example | 中文翻译 / Chinese Translation | 使用场景 / Usage Context |
|------------------------|---------------------------|-------------------------------|--------------------------|
| 兴奋/Excitement | This is insane! | 这太疯狂了！/太不可思议了！ | 突破性进展 |
| 强调/Emphasis | Literally | 字面意义上/确实 | 强调真实性 |
| 思考/Thinking | Um, like | 嗯，就像 | 思考停顿 |
| 幽默/Humor | lol, haha | 哈哈 | 轻松时刻 |
| 讽刺/Sarcasm | Obviously... | 显然... | 反讽表达 |
| 确定/Certainty | Absolutely | 绝对/完全 | 肯定回答 |
| 不确定/Uncertainty | I think, probably | 我想，可能 | 推测性陈述 |

### 2.3 技术热情表达 / Technical Enthusiasm Expression

**规则 2.3.1: 技术细节描述**
- 保持对技术规格的精确描述
- 中文翻译保持专业术语准确性
- 保留对技术突破的兴奋语气

**Rule 2.3.1: Technical Detail Description**
- Maintain precise descriptions of technical specifications
- Chinese translation maintains professional terminology accuracy
- Preserve excited tone about technical breakthroughs

**规则 2.3.2: 未来愿景表达**
- 保持对宏大目标的热情表达
- 中文翻译保持激励性和感染力
- 保留"使人类成为多行星物种"等核心愿景表述

**Rule 2.3.2: Future Vision Expression**
- Maintain enthusiastic expression about grand goals
- Chinese translation maintains inspirational and infectious quality
- Preserve core vision statements like "making life multiplanetary"

---

## 3. 日期格式一致性 / Date Format Consistency

### 3.1 ISO 8601 标准 / ISO 8601 Standard

**规则 3.1.1: 标准日期格式**
- 所有日期必须使用 ISO 8601 格式: `YYYY-MM-DD`
- 示例: `2025-06-01`

**Rule 3.1.1: Standard Date Format**
- All dates must use ISO 8601 format: `YYYY-MM-DD`
- Example: `2025-06-01`

**规则 3.1.2: 日期时间格式**
- 需要具体时间时使用: `YYYY-MM-DDTHH:MM:SS`
- 示例: `2025-06-01T14:30:00`

**Rule 3.1.2: Date-Time Format**
- Use when specific time is needed: `YYYY-MM-DDTHH:MM:SS`
- Example: `2025-06-01T14:30:00`

**规则 3.1.3: 时区处理**
- 优先使用UTC时间，标注`Z`后缀
- 或使用本地时间+时区偏移
- 示例: `2025-06-01T14:30:00Z` 或 `2025-06-01T14:30:00-08:00`

**Rule 3.1.3: Timezone Handling**
- Prefer UTC time with `Z` suffix
- Or use local time with timezone offset
- Example: `2025-06-01T14:30:00Z` or `2025-06-01T14:30:00-08:00`

### 3.2 日期范围格式 / Date Range Format

| 场景 / Scenario | 格式 / Format | 示例 / Example |
|-----------------|---------------|----------------|
| 日期范围 | `YYYY-MM-DD/YYYY-MM-DD` | `2025-01-01/2025-01-31` |
| 模糊日期 | `YYYY-MM` 或 `YYYY` | `2025-06` 或 `2025` |
| 季度 | `YYYY-QN` | `2025-Q2` |
| 财年 | `FYYYYY` | `FY2025` |

### 3.3 相对时间表达 / Relative Time Expression

**规则 3.3.1: 相对时间标准化**
- 避免使用模糊的"最近"、"不久前"
- 转换为具体日期或明确的时间范围
- 示例: 将"最近"转换为"2025年5月"或"过去两周"

**Rule 3.3.1: Relative Time Standardization**
- Avoid vague terms like "recently", "not long ago"
- Convert to specific dates or clear time ranges
- Example: Convert "recently" to "May 2025" or "past two weeks"

---

## 4. ID 格式一致性 / ID Format Consistency

### 4.1 ID 命名约定 / ID Naming Convention

**规则 4.1.1: 标准ID格式**
- 格式: `{type}-{YYYY}-{sequence}`
- 示例: `tweet-2025-001`, `interview-2025-042`

**Rule 4.1.1: Standard ID Format**
- Format: `{type}-{YYYY}-{sequence}`
- Example: `tweet-2025-001`, `interview-2025-042`

**规则 4.1.2: 类型前缀定义 / Type Prefix Definitions**

| 类型 / Type | 前缀 / Prefix | 示例 / Example |
|-------------|---------------|----------------|
| X/Twitter 推文 | tweet | tweet-2025-001 |
| 采访 | interview | interview-2025-001 |
| 财报电话会议 | earnings | earnings-2025-001 |
| 演讲/主旨发言 | keynote | keynote-2025-001 |
| 播客 | podcast | podcast-2025-001 |
| 新闻发布会 | press | press-2025-001 |
| 法律文件 | legal | legal-2025-001 |
| 邮件/内部备忘录 | email | email-2025-001 |
| 书籍/文章 | book | book-2025-001 |
| 法庭证词 | testimony | testimony-2025-001 |

**规则 4.1.3: 序列号规则**
- 每年从001开始重新编号
- 使用3位数字，不足补零
- 示例: 001, 042, 123, 999

**Rule 4.1.3: Sequence Number Rules**
- Restart numbering from 001 each year
- Use 3 digits with leading zeros
- Example: 001, 042, 123, 999

### 4.2 特殊ID格式 / Special ID Formats

**规则 4.2.1: 主题系列ID**
- 格式: `{type}-{topic}-{YYYY}-{sequence}`
- 示例: `interview-doge-2025-001`, `tweet-ai-2025-015`

**Rule 4.2.1: Thematic Series IDs**
- Format: `{type}-{topic}-{YYYY}-{sequence}`
- Example: `interview-doge-2025-001`, `tweet-ai-2025-015`

**规则 4.2.2: 多部分ID**
- 格式: `{base-id}-part{N}`
- 示例: `interview-2025-001-part1`, `interview-2025-001-part2`

**Rule 4.2.2: Multi-part IDs**
- Format: `{base-id}-part{N}`
- Example: `interview-2025-001-part1`, `interview-2025-001-part2`

---

## 5. 分类/标签一致性 / Category/Tag Consistency

### 5.1 受控词汇表 / Controlled Vocabulary

**规则 5.1.1: 主分类 / Main Categories**

| 分类ID / Category ID | 英文 / English | 中文 / Chinese |
|----------------------|----------------|----------------|
| tech | Technology | 技术 |
| business | Business | 商业 |
| space | Space Exploration | 太空探索 |
| ai | Artificial Intelligence | 人工智能 |
| energy | Energy | 能源 |
| transportation | Transportation | 交通 |
| politics | Politics | 政治 |
| society | Society | 社会 |
| personal | Personal | 个人 |
| philosophy | Philosophy | 哲学 |

**规则 5.1.2: 子分类 / Subcategories**

| 父分类 / Parent | 子分类ID / Subcategory ID | 英文 / English | 中文 / Chinese |
|-----------------|---------------------------|----------------|----------------|
| tech | tesla | Tesla | 特斯拉 |
| tech | spacex | SpaceX | SpaceX |
| tech | neuralink | Neuralink | Neuralink |
| tech | boring | The Boring Company | The Boring Company |
| tech | xai | xAI | xAI |
| ai | grok | Grok | Grok |
| ai | fsd | Full Self-Driving | 完全自动驾驶 |
| ai | optimus | Optimus | Optimus |
| space | starship | Starship | 星舰 |
| space | falcon | Falcon | 猎鹰 |
| space | dragon | Dragon | 龙飞船 |
| space | mars | Mars | 火星 |
| politics | doge | DOGE | 政府效率部 |
| politics | regulation | Regulation | 监管 |
| energy | solar | Solar | 太阳能 |
| energy | battery | Battery | 电池 |

### 5.2 标签命名规则 / Tag Naming Rules

**规则 5.2.1: 标签格式**
- 使用小写字母
- 多词标签使用连字符分隔
- 示例: `artificial-intelligence`, `full-self-driving`

**Rule 5.2.1: Tag Format**
- Use lowercase letters
- Use hyphens for multi-word tags
- Example: `artificial-intelligence`, `full-self-driving`

**规则 5.2.2: 标签层级**
- 一级标签: 核心主题 (如 `tesla`, `spacex`)
- 二级标签: 具体话题 (如 `cybertruck`, `starship`)
- 三级标签: 特定事件或概念 (如 `dojo-supercomputer`, `mars-colony`)

**Rule 5.2.2: Tag Hierarchy**
- Level 1: Core topics (e.g., `tesla`, `spacex`)
- Level 2: Specific topics (e.g., `cybertruck`, `starship`)
- Level 3: Specific events or concepts (e.g., `dojo-supercomputer`, `mars-colony`)

### 5.3 2025-2026 新术语 / 2025-2026 New Terminology

**规则 5.3.1: DOGE 相关术语**
- DOGE: Department of Government Efficiency
- 中文: 政府效率部
- 标签: `doge`, `government-efficiency`

**Rule 5.3.1: DOGE Related Terminology**
- DOGE: Department of Government Efficiency
- Chinese: 政府效率部
- Tags: `doge`, `government-efficiency`

**规则 5.3.2: Grok Heavy 相关术语**
- Grok Heavy: xAI最新大语言模型 (2025)
- 中文: Grok Heavy
- 标签: `grok`, `grok-heavy`, `xai`

**Rule 5.3.2: Grok Heavy Related Terminology**
- Grok Heavy: xAI's latest LLM (2025)
- Chinese: Grok Heavy
- Tags: `grok`, `grok-heavy`, `xai`

**规则 5.3.3: 新术语添加流程**
- 新术语首次出现时创建术语表条目
- 在一致性规则文档中更新
- 通知所有编辑人员

**Rule 5.3.3: New Terminology Addition Process**
- Create glossary entry when new term first appears
- Update in consistency rules document
- Notify all editors

---

## 6. 引语归属一致性 / Quote Attribution Consistency

### 6.1 来源引用格式 / Source Citation Format

**规则 6.1.1: 推文引用格式**
```
Elon Musk (@elonmusk) on X, YYYY-MM-DD
https://x.com/elonmusk/status/{tweet-id}
```

**Rule 6.1.1: Tweet Citation Format**
```
Elon Musk (@elonmusk) on X, YYYY-MM-DD
https://x.com/elonmusk/status/{tweet-id}
```

**规则 6.1.2: 采访引用格式**
```
Elon Musk, Interview with {Interviewer/Publication}, {Platform}, YYYY-MM-DD
{URL or Archive Link}
```

**Rule 6.1.2: Interview Citation Format**
```
Elon Musk, Interview with {Interviewer/Publication}, {Platform}, YYYY-MM-DD
{URL or Archive Link}
```

**规则 6.1.3: 财报电话会议引用格式**
```
Elon Musk, Tesla Q{N} {Year} Earnings Call, YYYY-MM-DD
{Transcript URL or SEC Filing Reference}
```

**Rule 6.1.3: Earnings Call Citation Format**
```
Elon Musk, Tesla Q{N} {Year} Earnings Call, YYYY-MM-DD
{Transcript URL or SEC Filing Reference}
```

**规则 6.1.4: 演讲引用格式**
```
Elon Musk, {Event Name}, {Location}, YYYY-MM-DD
{Video URL or Transcript Link}
```

**Rule 6.1.4: Speech Citation Format**
```
Elon Musk, {Event Name}, {Location}, YYYY-MM-DD
{Video URL or Transcript Link}
```

### 6.2 上下文标注 / Context Annotation

**规则 6.2.1: 引语上下文**
- 必须提供引语的完整上下文
- 标注引语前后的相关内容
- 说明引语的回答对象或场合

**Rule 6.2.1: Quote Context**
- Must provide complete context of the quote
- Annotate relevant content before and after the quote
- Indicate who or what occasion the quote was addressing

**规则 6.2.2: 翻译说明**
- 如有翻译，标注原文语言
- 说明翻译来源（官方/自译）
- 保留原文中的语气标记

**Rule 6.2.2: Translation Notes**
- If translated, annotate original language
- Indicate translation source (official/self-translated)
- Preserve tone markers from original

### 6.3 不确定性标注 / Uncertainty Annotation

**规则 6.3.1: 推测性声明标注**
- 使用 `[推测/Speculation]` 标注非确定性声明
- 使用 `[计划/Planned]` 标注计划中的项目
- 使用 `[目标/Target]` 标注目标性数字

**Rule 6.3.1: Speculative Statement Annotation**
- Use `[推测/Speculation]` for non-deterministic statements
- Use `[计划/Planned]` for planned projects
- Use `[目标/Target]` for target numbers

**规则 6.3.2: 时间敏感性标注**
- 使用 `[截至/As of YYYY-MM-DD]` 标注时效性内容
- 使用 `[已过期/Expired]` 标注过时信息
- 使用 `[已更新/Updated YYYY-MM-DD]` 标注更新内容

**Rule 6.3.2: Time Sensitivity Annotation**
- Use `[截至/As of YYYY-MM-DD]` for time-sensitive content
- Use `[已过期/Expired]` for outdated information
- Use `[已更新/Updated YYYY-MM-DD]` for updated content

---

## 7. 应用示例 / Application Examples

### 示例 1: 术语一致性应用 / Example 1: Terminology Consistency Application

**不一致示例 (错误):**
```
FSD 是 Tesla 的全自动驾驶功能。
全自动驾驶将在明年推出。
```

**一致示例 (正确):**
```
完全自动驾驶 (FSD) 是特斯拉的核心功能。
完全自动驾驶功能将在明年推出。
```

### 示例 2: ID格式一致性应用 / Example 2: ID Format Consistency Application

**不一致示例 (错误):**
```
Tweet_2025_1
twitter-post-2025-1
TWEET2025001
```

**一致示例 (正确):**
```
tweet-2025-001
tweet-2025-002
interview-2025-001
```

### 示例 3: 日期格式一致性应用 / Example 3: Date Format Consistency Application

**不一致示例 (错误):**
```
June 1, 2025
01/06/2025
2025年6月1日
```

**一致示例 (正确):**
```
2025-06-01
2025-06-15
2025-12-31
```

### 示例 4: 来源引用一致性应用 / Example 4: Source Citation Consistency Application

**不一致示例 (错误):**
```
来源: Twitter
来自马斯克推文
X post by Elon
```

**一致示例 (正确):**
```
Elon Musk (@elonmusk) on X, 2025-06-01
https://x.com/elonmusk/status/1234567890
```

---

## 8. 一致性检查清单 / Consistency Checklist

### 入库前一致性检查 / Pre-Submission Consistency Check

**翻译一致性 / Translation Consistency:**
- [ ] 关键术语使用统一翻译
- [ ] 公司名和产品名处理符合规则
- [ ] 技术缩写首次出现已展开
- [ ] 常见表达翻译一致

**风格标记一致性 / Style Marker Consistency:**
- [ ] 口头禅翻译一致
- [ ] 情感标记保留
- [ ] 技术热情表达统一

**格式一致性 / Format Consistency:**
- [ ] 日期使用 ISO 8601 格式
- [ ] ID 符合命名约定
- [ ] 分类和标签使用受控词汇

**来源引用一致性 / Source Citation Consistency:**
- [ ] 引用格式符合标准
- [ ] 上下文标注完整
- [ ] 不确定性声明已标注

**2025-2026 特定 / 2025-2026 Specific:**
- [ ] DOGE 相关术语一致
- [ ] Grok Heavy 相关术语一致
- [ ] 新术语已添加到术语表

---

## 9. 版本历史 / Version History

| 版本 / Version | 日期 / Date | 变更 / Changes |
|----------------|-------------|----------------|
| 1.0.0 | 2025-06-01 | 初始版本 / Initial release |
