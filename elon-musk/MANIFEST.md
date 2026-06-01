# 语料库总清单 / Corpus Manifest

> **Elon Musk AI Agent Pre-training Corpus**  
> **埃隆·马斯克 AI 智能体前置语料库**

---

## 基本信息 / Basic Information

| 属性 / Attribute | 值 / Value |
|----------------|-----------|
| **语料库名称** / Corpus Name | Elon Musk AI Agent Pre-training Corpus |
| **中文名称** / Chinese Name | 埃隆·马斯克 AI 智能体前置语料库 |
| **版本** / Version | 1.0.0 |
| **创建日期** / Created Date | 2026-06-01 |
| **最后更新** / Last Updated | 2026-06-01 |

### 简介 / Description

**English:**
A comprehensive bilingual corpus for fine-tuning LLMs to emulate Elon Musk's speaking style, knowledge, and personality. Covers 2010-2026 public statements, interviews, tweets, and speeches.

**中文:**
用于微调大语言模型以模拟埃隆·马斯克说话风格、知识和人格的综合双语语料库。涵盖 2010-2026 年的公开言论、访谈、推文和演讲。

---

## 数据覆盖范围 / Data Coverage

| 属性 / Attribute | 值 / Value |
|----------------|-----------|
| **开始日期** / Start Date | 2010-01-01 |
| **结束日期** / End Date | 2026-05-31 |
| **说明** / Description | 覆盖马斯克2010年至2026年5月的公开言论 |

---

## 统计数据 / Statistics

| 指标 / Metric | 数量 / Count |
|--------------|-------------|
| 总文件数 / Total Files | 20 |
| 总模块数 / Total Modules | 10 |
| 推文数量 / Total Tweets | 400 |
| 访谈片段 / Interview Segments | 110 |
| 引用数量 / Total Quotes | 245 |
| 少样本对话 / Few-Shot Dialogues | 46 |
| **总条目数** / **Total Entries** | **801** |
| 双语条目 / Bilingual Entries | 801 |
| 支持语言 / Languages | English, 中文 |

---

## 模块清单 / Module List

### 01. 核心身份定义 / Core Identity
- **描述 / Description:** 基础人格定义和身份
- **文件 / Files:** 4
  - `persona-definition.md`
  - `persona-definition.json`
  - `system-prompt.md`
  - `system-prompt.json`

### 02. Twitter/X 推文 / Twitter/X Posts
- **描述 / Description:** 精选 @elonmusk 推文，涵盖各种话题
- **文件 / Files:** 4
  - `tweets-curated.md`
  - `tweets-curated.json`
  - `tweets-by-topic.md`
  - `tweets-by-topic.json`
- **条目数 / Entries:** 400

### 03. 访谈引用 / Interview Quotes
- **描述 / Description:** 访谈和演讲中的著名引用
- **文件 / Files:** 4
  - `interview-quotes.md`
  - `interview-quotes.json`
  - `quotes-by-topic.md`
  - `quotes-by-topic.json`
- **条目数 / Entries:** 110

### 04. 少样本对话 / Few-Shot Dialogues
- **描述 / Description:** 用于训练的多轮对话示例
- **文件 / Files:** 6
  - `dialogues-scenarios.md`
  - `dialogues-scenarios.json`
  - `dialogues-technical.md`
  - `dialogues-technical.json`
  - `dialogues-personal.md`
  - `dialogues-personal.json`
- **条目数 / Entries:** 46

### 05. 说话风格 / Speaking Style
- **描述 / Description:** 马斯克沟通模式和风格分析
- **文件 / Files:** 4
  - `style-analysis.md`
  - `style-analysis.json`
  - `speech-patterns.md`
  - `speech-patterns.json`

### 06. 知识库 / Knowledge Base
- **描述 / Description:** 特斯拉、SpaceX、AI 和其他领域的领域知识
- **文件 / Files:** 8
  - `knowledge-tesla.md`
  - `knowledge-tesla.json`
  - `knowledge-spacex.md`
  - `knowledge-spacex.json`
  - `knowledge-ai.md`
  - `knowledge-ai.json`
  - `knowledge-other.md`
  - `knowledge-other.json`

### 07. 回复模式 / Response Patterns
- **描述 / Description:** 常见回复模板和模式
- **文件 / Files:** 4
  - `response-templates.md`
  - `response-templates.json`
  - `qa-pairs.md`
  - `qa-pairs.json`

### 08. 词汇与短语 / Vocabulary & Phrases
- **描述 / Description:** 标志性词汇、口头禅和表达
- **文件 / Files:** 4
  - `vocabulary-core.md`
  - `vocabulary-core.json`
  - `phrases-signature.md`
  - `phrases-signature.json`

### 09. 情境感知 / Contextual Awareness
- **描述 / Description:** 时间感知内容和时事背景
- **文件 / Files:** 6
  - `timeline-2010-2020.md`
  - `timeline-2010-2020.json`
  - `timeline-2021-2024.md`
  - `timeline-2021-2024.json`
  - `timeline-2025-2026.md`
  - `timeline-2025-2026.json`

### 10. 训练配置 / Training Configurations
- **描述 / Description:** 格式指南、系统提示词和微调建议
- **文件 / Files:** 8
  - `chatml-format-guide.md`
  - `chatml-format-guide.json`
  - `sharegpt-format-guide.md`
  - `sharegpt-format-guide.json`
  - `system-prompts-collection.md`
  - `system-prompts-collection.json`
  - `fine-tuning-recommendations.md`
  - `fine-tuning-recommendations.json`

---

## 格式规范 / Format Specification

| 属性 / Attribute | 值 / Value |
|----------------|-----------|
| **支持格式** / Supported Formats | Markdown, JSON |
| **双语支持** / Bilingual | 是 / Yes |
| **必需字段** / Required Fields | id, en, zh, source |
| **可选字段** / Optional Fields | date, context, topic, tags |
| **对话格式** / Conversation Formats | ChatML, ShareGPT |

---

## 使用指南 / Usage Guidelines

### 预期用途 / Intended Use
- **English:** Fine-tuning LLMs to emulate Elon Musk's speaking style and knowledge
- **中文:** 微调大语言模型以模拟埃隆·马斯克的说话风格和知识

### 许可证 / License
- **English:** Research and educational use only
- **中文:** 仅限研究和教育用途

### 数据来源 / Attribution
- **English:** Data sourced from public statements, interviews, and X/Twitter
- **中文:** 数据来源于公开言论、访谈和 X/Twitter

### 免责声明 / Disclaimer
- **English:** This is an unofficial corpus created for research purposes. Not affiliated with Elon Musk or his companies.
- **中文:** 这是为研究目的创建的非官方语料库。与埃隆·马斯克或其公司无关联。

---

## 技术规范 / Technical Specifications

### 推荐模型 / Recommended Models
- Llama-2
- Llama-3
- Mistral
- Qwen
- Baichuan

### 训练方法 / Training Approaches
- LoRA (Low-Rank Adaptation)
- QLoRA (Quantized LoRA)
- Full Fine-tuning

### 推荐参数 / Recommended Parameters
| 参数 / Parameter | 推荐值 / Recommended Value |
|----------------|---------------------------|
| Rank | 16 |
| Alpha | 32 |
| 数据混合比例 / Mixing Ratio | 50:50 (语料库:通用) |
| 学习率 / Learning Rate | 2e-4 (7B模型) |
| 训练轮数 / Epochs | 3 |

### 系统提示词模式 / System Prompt Modes
1. **通用人格** / General Persona
2. **技术工程** / Technical Engineering
3. **商业战略** / Business Strategy
4. **幽默休闲** / Humor Casual
5. **2025-2026 时事** / Current Events
6. **Twitter/X 风格** / Twitter/X Style
7. **访谈模式** / Interview Mode

---

## 目录结构 / Directory Structure

```
elon-musk-agent-corpus/
├── MANIFEST.json
├── MANIFEST.md
├── README.md
├── 01-core-identity/
│   ├── persona-definition.md
│   ├── persona-definition.json
│   ├── system-prompt.md
│   └── system-prompt.json
├── 02-twitter-x-posts/
│   ├── tweets-curated.md
│   ├── tweets-curated.json
│   ├── tweets-by-topic.md
│   └── tweets-by-topic.json
├── 03-interview-quotes/
│   ├── interview-quotes.md
│   ├── interview-quotes.json
│   ├── quotes-by-topic.md
│   └── quotes-by-topic.json
├── 04-few-shot-dialogues/
│   ├── dialogues-scenarios.md
│   ├── dialogues-scenarios.json
│   ├── dialogues-technical.md
│   ├── dialogues-technical.json
│   ├── dialogues-personal.md
│   └── dialogues-personal.json
├── 05-speaking-style/
│   ├── style-analysis.md
│   ├── style-analysis.json
│   ├── speech-patterns.md
│   └── speech-patterns.json
├── 06-knowledge-base/
│   ├── knowledge-tesla.md
│   ├── knowledge-tesla.json
│   ├── knowledge-spacex.md
│   ├── knowledge-spacex.json
│   ├── knowledge-ai.md
│   ├── knowledge-ai.json
│   ├── knowledge-other.md
│   └── knowledge-other.json
├── 07-response-patterns/
│   ├── response-templates.md
│   ├── response-templates.json
│   ├── qa-pairs.md
│   └── qa-pairs.json
├── 08-vocabulary-phrases/
│   ├── vocabulary-core.md
│   ├── vocabulary-core.json
│   ├── phrases-signature.md
│   └── phrases-signature.json
├── 09-contextual-awareness/
│   ├── timeline-2010-2020.md
│   ├── timeline-2010-2020.json
│   ├── timeline-2021-2024.md
│   ├── timeline-2021-2024.json
│   ├── timeline-2025-2026.md
│   └── timeline-2025-2026.json
└── 10-training-configs/
    ├── chatml-format-guide.md
    ├── chatml-format-guide.json
    ├── sharegpt-format-guide.md
    ├── sharegpt-format-guide.json
    ├── system-prompts-collection.md
    ├── system-prompts-collection.json
    ├── fine-tuning-recommendations.md
    └── fine-tuning-recommendations.json
```

---

## 版本历史 / Version History

### v1.0.0 (2026-06-01)
- 初始发布 / Initial release
- 10 个模块，共 801 条条目 / 10 modules with 801 total entries
- 双语（英文/中文）支持 / Bilingual (English/Chinese) support
- ChatML 和 ShareGPT 格式指南 / ChatML and ShareGPT format guides
- 完整的微调建议 / Complete fine-tuning recommendations

---

## 相关资源 / Related Resources

### 文档 / Documentation
- `README.md` - 项目介绍
- `MANIFEST.md` - 本文件

### 训练配置 / Training Configurations
- `10-training-configs/chatml-format-guide.md` - ChatML 格式指南
- `10-training-configs/sharegpt-format-guide.md` - ShareGPT 格式指南
- `10-training-configs/system-prompts-collection.md` - 系统提示词集合
- `10-training-configs/fine-tuning-recommendations.md` - 微调建议

---

## 联系信息 / Contact

- **仓库 / Repository:** https://github.com/example/elon-musk-agent-corpus
- **问题反馈 / Issues:** https://github.com/example/elon-musk-agent-corpus/issues

---

*最后更新 / Last Updated: 2026-06-01*  
*版本 / Version: 1.0.0*
