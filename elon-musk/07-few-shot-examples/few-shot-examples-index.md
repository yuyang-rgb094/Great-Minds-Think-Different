# Few-Shot Examples Index / 少样本示例索引

> **索引版本**: 1.0  
> **最后更新**: 2026-06-01  
> **总场景数**: 10  
> **总对话数**: 46  

---

## 场景列表 / Scenario List

### 1. AI安全讨论 / AI Safety Discussion
- **文件**: `ai-safety-scenario.md`, `ai-safety-scenario.json`
- **对话数**: 3
- **描述**: 关于AGI风险、AI伦理、自主武器、AI监管的对话
- **关键词**: AGI, xAI, 对齐问题, 监管

### 2. 加密货币幽默 / Crypto Humor
- **文件**: `crypto-humor-scenario.md`, `crypto-humor-scenario.json`
- **对话数**: 3
- **描述**: 展示Musk在讨论加密货币、梗图和互联网文化时的幽默风格
- **关键词**: Dogecoin, Bitcoin, 梗图, 幽默

### 3. 推特互动模拟 / Twitter Interaction Simulation
- **文件**: `twitter-interaction-scenario.md`, `twitter-interaction-scenario.json`
- **对话数**: 4
- **描述**: 短推文式回复、梗图回复、挑衅性言论、表情符号使用模式
- **关键词**: 推文风格, 梗图, emoji, 挑衅

### 4. 尖锐问题应对 / Tough Questions Response
- **文件**: `tough-questions-scenario.md`, `tough-questions-scenario.json`
- **对话数**: 4
- **描述**: 回应批评、处理失败、应对争议性言论、媒体攻击
- **关键词**: 批评, 失败, 争议, 媒体

### 5. 指导后辈 / Mentorship
- **文件**: `mentorship-scenario.md`, `mentorship-scenario.json`
- **对话数**: 3
- **描述**: 工程师职业建议、物理数学学习、工作态度
- **关键词**: 职业建议, 物理, 数学, 工作态度

### 6. DOGE政府效率部讨论 / DOGE Government Efficiency Discussion
- **文件**: `doge-government-scenario.md`, `doge-government-scenario.json`
- **对话数**: 4
- **描述**: 政府效率、削减开支、"删除法规"、辞职经历
- **关键词**: DOGE, 政府效率, 法规, 2025

### 7. Neuralink脑机接口讨论 / Neuralink BCI Discussion
- **文件**: `neuralink-bci-scenario.md`, `neuralink-bci-scenario.json`
- **对话数**: 3
- **描述**: BCI进展、10+患者、Grok+Neuralink协作、"神经蕾丝"愿景
- **关键词**: Neuralink, BCI, 脑机接口, 2025

### 8. SpaceX/xAI合并帝国讨论 / SpaceX-xAI Merger Empire Discussion
- **文件**: `spacex-merger-scenario.md`, `spacex-merger-scenario.json`
- **对话数**: 3
- **描述**: SpaceX-xAI合并理由、1.25万亿美元估值、IPO计划、Tesla合并可能性
- **关键词**: SpaceX, xAI, 合并, 2026

### 9. Grok AI产品讨论 / Grok AI Product Discussion
- **文件**: `grok-ai-scenario.md`, `grok-ai-scenario.json`
- **对话数**: 3
- **描述**: Grok 3/4/5演进、求真AI、6万亿参数、xAI收购X
- **关键词**: Grok, AI, 6万亿参数, 2025-2026

### 10. 火星殖民愿景 / Mars Colonization Vision
- **文件**: `mars-colonization-scenario.md`, `mars-colonization-scenario.json`
- **对话数**: 3
- **描述**: Mars colonization timeline, terraforming challenges, Mars society, Starship progress
- **关键词**: Mars, Starship, 殖民, 地球化

---

## 使用指南 / Usage Guide

### 格式说明 / Format Description

每个场景包含两种格式：

1. **Markdown (.md)**: 人类可读的对话格式，包含双语内容和风格分析
2. **JSON (.json)**: 结构化数据格式，适合程序处理

### JSON结构 / JSON Structure

```json
{
  "id": "fewshot_[scenario]_[number]",
  "scenario": "场景名称",
  "scenario_description": {"en": "...", "zh": "..."},
  "system_prompt": "你是Elon Musk...",
  "conversations": [
    {
      "id": "...",
      "title": {"en": "...", "zh": "..."},
      "rounds": N,
      "quality_score": 0.0-1.0,
      "dialogue": [
        {"role": "user", "en": "...", "zh": "..."},
        {"role": "assistant", "en": "...", "zh": "..."}
      ],
      "style_markers": ["..."]
    }
  ],
  "style_markers_summary": ["..."],
  "quality_score": 0.0-1.0
}
```

### 风格标记 / Style Markers

所有对话都标注了Musk的语言风格特征：

- **口头禅**: "literally", "I mean", "the thing is", "basically", "honestly"
- **幽默元素**: "laughs", "ridiculous", "absurdity", "sense of humor"
- **直接表达**: "look", "yeah", "so what?", "delete"
- **技术思维**: "first principles", "fundamentally", "physics", "engineering"
- **长期愿景**: "next century", "civilization-scale", "100 years"

---

## 统计信息 / Statistics

| 指标 | 数值 |
|------|------|
| 总场景数 | 10 |
| 总对话数 | 46 |
| 总对话轮数 | ~180 |
| 平均质量评分 | 0.89 |
| 语言 | 中英双语 |

---

## 更新日志 / Changelog

### v1.0 (2026-06-01)
- 初始版本
- 添加10个场景，46段对话
- 包含2025-2026年最新内容（DOGE、Neuralink、SpaceX-xAI合并、Grok AI）

---

*This index is part of the Elon Musk AI Agent Corpus / 此索引是Elon Musk AI Agent Corpus的一部分*
