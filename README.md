# Great Minds Think Different

<p align="center">
  <img src="https://img.shields.io/badge/Minds-Steve%20Jobs%20%7C%20Tim%20Cook%20%7C%20Warren%20Buffett%20%7C%20Elon%20Musk-blue" alt="Minds">
  <img src="https://img.shields.io/badge/Total%20Entries-1050%2B-green" alt="Entries">
  <img src="https://img.shields.io/badge/Languages-English%20%7C%20中文-orange" alt="Languages">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

> **English** | [中文](#中文介绍)

## 📖 Introduction

**Great Minds Think Different** is an open-source corpus collection dedicated to preserving and sharing the wisdom of history's most influential thinkers, innovators, and leaders. Our mission is to build high-quality training datasets for AI agents that can embody the thinking patterns, communication styles, and values of these extraordinary individuals.

> *"Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round pegs in the square holes. The ones who see things differently."* — Steve Jobs

---

## 🧠 Featured Minds

### Currently Available

| Mind | Role | Era | Entries | Status |
|------|------|-----|---------|--------|
| **Steve Jobs** | Apple Co-founder | 1955-2011 | 75+ | ✅ Available |
| **Tim Cook** | Apple CEO | 2011-Present | 75 | ✅ Available |
| **Warren Buffett** | Berkshire Hathaway Chairman | 1930-Present | 100+ | ✅ Available |
| **Elon Musk** | Tesla/SpaceX/xAI CEO | 1971-Present | 801 | ✅ Available |

### Coming Soon

- Jeff Bezos (Amazon)
- Bill Gates (Microsoft)
- *And more...*

---

## 📁 Repository Structure

```
Great-Minds-Think-Different/
├── README.md                          # This file
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
│
├── steve-jobs/                        # Steve Jobs Corpus
│   ├── corpus/
│   │   ├── corpus.json               # Structured data (JSON)
│   │   └── corpus.md                 # Human-readable (Markdown)
│   ├── training/
│   │   └── system_prompt.md          # AI agent prompt template
│   └── sources/                      # Raw source materials
│
├── tim-cook/                          # Tim Cook Corpus
│   ├── corpus/
│   │   ├── corpus.json               # Structured data (JSON)
│   │   └── corpus.md                 # Human-readable (Markdown)
│   ├── training/
│   │   └── system_prompt.md          # AI agent prompt template
│   └── sources/                      # Raw source materials
│
├── warren-buffett/                    # Warren Buffett Corpus
│   ├── 01-core-identity/             # Persona & system prompt
│   ├── 02-thinking-frameworks/        # Value investing, business evaluation
│   ├── 03-behavioral-guidelines/     # Communication style, decision-making
│   ├── 04-shareholder-letters/       # 49 letters (1977-2025)
│   ├── 05-annual-meetings/           # 32 meetings (1994-2025)
│   ├── 06-interviews/                # CNBC interviews
│   ├── 07-quotes/                    # 53 quotes (investing, business, life)
│   ├── 08-few-shot-examples/          # Interaction examples
│   ├── 09-knowledge-base/           # Biography, Berkshire history
│   ├── 10-quality-control/           # Validation & anti-hallucination
│   ├── 11-embeddings/               # Vector embeddings (OpenAI)
│   ├── scripts/                      # Download & processing scripts
│   ├── MANIFEST.json                 # Corpus manifest
│   └── README.md                     # Corpus README
│
├── elon-musk/                         # 🆕 Elon Musk Corpus (v1.0)
│   ├── 01-core-identity/             # Persona definition & system prompt
│   ├── 02-thinking-frameworks/        # First principles, engineering, decision-making, risk, innovation, business
│   ├── 03-behavioral-guidelines/     # Communication style, humor/memes, leadership, response guidelines
│   ├── 04-tweets/                    # 400 high-engagement tweets (12 categories, 2010-2026)
│   ├── 05-interviews/                # 110 conversation segments (13 interviews)
│   ├── 06-quotes/                    # 245 classic quotes (10 categories)
│   ├── 07-few-shot-examples/          # 46 few-shot dialogues (13 scenarios)
│   ├── 08-knowledge-base/           # Biography, companies, Mars plan, DOGE, SpaceX-xAI merger, Grok, Neuralink, Robotaxi
│   ├── 09-quality-control/           # Validation, consistency, anti-hallucination, style metrics
│   ├── 10-training-configs/          # ChatML/ShareGPT format guides, system prompts, fine-tuning recommendations
│   ├── README.md                     # Corpus README
│   └── MANIFEST.json                 # Corpus manifest
│
└── templates/                         # Templates for new minds
    ├── corpus_template.json
    ├── system_prompt_template.md
    └── README_template.md
```

---

## 🎯 Quick Start

### Using the Corpus for AI Training

#### Python Example

```python
import json

# Load Elon Musk's tweets
with open('elon-musk/04-tweets/tweets-ai-tech.json', 'r', encoding='utf-8') as f:
    ai_tweets = json.load(f)

# Load few-shot examples for fine-tuning
with open('elon-musk/07-few-shot-examples/ai-safety-scenario.json', 'r', encoding='utf-8') as f:
    few_shot = json.load(f)

# Convert to ChatML format for OpenAI fine-tuning
messages = [
    {"role": "system", "content": "You are Elon Musk, CEO of Tesla, SpaceX, and xAI."},
]
for conv in few_shot['conversations']:
    messages.append({"role": conv['role'], "content": conv['en']})
```

#### Using System Prompts

Each mind includes a carefully crafted system prompt for AI agents:

```python
# Read Elon Musk's system prompt
with open('elon-musk/01-core-identity/system-prompt.json', 'r') as f:
    prompt_data = json.load(f)
    musk_prompt = prompt_data['system_prompt']['en']

# Use with your AI model
response = ai_model.generate(
    system_prompt=musk_prompt,
    user_message="What do you think about the future of AI?"
)
```

---

## 📊 Corpus Statistics

### Steve Jobs
- **Total Entries**: 75+
- **Categories**: Multiple
- **Time Span**: 1976-2011
- **Languages**: English & Chinese
- **Sources**: Keynotes, interviews, All Things D, Stanford speech

### Tim Cook
- **Total Entries**: 75
- **Categories**: 7 (Leadership, Innovation, Privacy, AI & Tech, Personal Growth, China Business, Steve Jobs Legacy)
- **Time Span**: 2015-2026
- **Languages**: English & Chinese
- **Sources**: Graduation speeches, interviews, privacy conference, retirement letter

### Warren Buffett
- **Total Entries**: 100+ (53 quotes, 49 shareholder letters, 32 meeting templates, 5 interviews)
- **Categories**: 8 (Value Investing, Business Analysis, Market Behavior, Portfolio Management, Economic Outlook, Corporate Governance, Life Philosophy, Berkshire Operations)
- **Time Span**: 1977-2025 (48 years of shareholder letters)
- **Languages**: English & Chinese (bilingual)
- **Sources**: Berkshire Hathaway Annual Letters, CNBC Interviews & Archive, Annual Meeting Transcripts
- **Special Features**: Vector embeddings (964 chunks), few-shot examples, anti-hallucination guide

### 🆕 Elon Musk (v1.0 — June 2026)
- **Total Entries**: 801 (400 tweets + 110 interview segments + 245 quotes + 46 few-shot dialogues)
- **Modules**: 10 (Core Identity, Thinking Frameworks, Behavioral Guidelines, Tweets, Interviews, Quotes, Few-Shot Examples, Knowledge Base, Quality Control, Training Configs)
- **Time Span**: 2010-2026 (up to May 2026)
- **Languages**: English & Chinese (bilingual, every entry)
- **Formats**: Markdown + JSON (dual format, 171 files)
- **Sources**: X/Twitter, Lex Fridman Podcast, Joe Rogan Experience, All-In Summit, Tesla Earnings Calls, Bloomberg, Forbes, TED, Starbase Speech
- **Key Topics**: AI/AGI (Grok 3/4/5), SpaceX (Starship, Mars, IPO), Tesla (FSD, Robotaxi), Neuralink (BCI, 10+ patients), DOGE (government efficiency), xAI-X merger, crypto/Dogecoin, first principles thinking, engineering philosophy
- **Special Features**: 2025-2026 latest events (DOGE, SpaceX-xAI $1.25T merger, Forbes 2026 interview), ChatML/ShareGPT conversion guides, LoRA/QLoRA fine-tuning recommendations, anti-hallucination guide, style transfer metrics

---

## 🏗️ Corpus Format

Each entry follows a standardized schema. Example from Elon Musk corpus:

```json
{
  "id": "tweet_ai_001",
  "source": {
    "type": "tweet",
    "date": "2024-03-15",
    "engagement": {"likes": 500000, "retweets": 50000}
  },
  "category": "AI",
  "tags": ["AI", "safety", "regulation"],
  "en": {
    "text": "I think AI safety is actually the most important thing...",
    "context": "Response to question about AI regulation"
  },
  "zh": {
    "text": "我认为AI安全实际上是文明当前最需要关注的事情...",
    "context": "关于AI监管问题的回应"
  },
  "style_markers": ["serious", "definitive"],
  "quality_score": 0.95
}
```

---

## 💡 Use Cases

### 1. AI Agent Training
Train AI models to emulate the thinking and speaking style of great minds:
- Chatbots that provide advice in the voice of Elon Musk, Tim Cook, or Steve Jobs
- Virtual mentors for leadership, innovation, and engineering
- Historical figure simulations for education

### 2. Research & Analysis
- Study communication patterns of successful leaders
- Analyze evolution of thinking over time
- Compare different approaches to similar challenges

### 3. Content Creation
- Generate quotes for presentations and articles
- Find inspiration for speeches and writing
- Create educational materials

### 4. Personal Development
- Learn from the wisdom of great minds
- Study decision-making frameworks
- Understand leadership philosophies

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Quotes
1. Fork the repository
2. Add entries to the appropriate corpus file
3. Ensure bilingual content (English + Chinese)
4. Include complete source information
5. Submit a pull request

### Adding New Minds
1. Use the templates in `/templates/`
2. Create a new directory: `great-mind-name/`
3. Follow the existing structure
4. Include at least 50 high-quality entries
5. Provide system prompt for AI training

### Quality Standards
- All entries must have verifiable sources
- Bilingual content preferred (English + Chinese)
- Include context and background information
- Tag appropriately for easy filtering
- Respect copyright and fair use

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

**Note**: The corpus content is collected from public speeches, interviews, and published materials for educational and research purposes. All content belongs to their respective copyright holders.

---

## 🙏 Acknowledgments

- Steve Jobs' wisdom continues to inspire millions worldwide
- Tim Cook for his leadership and commitment to privacy
- Warren Buffett for decades of investment wisdom
- Elon Musk for pushing the boundaries of technology and human potential
- All contributors who help expand this collection

---

## 📬 Contact

- GitHub Issues: For bug reports and feature requests
- Discussions: For general questions and ideas

---

<p align="center">
  <i>"Stay hungry, stay foolish." — Steve Jobs</i><br>
  <i>"Life is not about standing on the sidelines." — Tim Cook</i><br>
  <i>"When something is important enough, you do it even if the odds are not in your favor." — Elon Musk</i>
</p>

---

# 中文介绍

## 📖 项目介绍

**Great Minds Think Different（非凡思维）** 是一个开源语料库项目，致力于收集和分享历史上最具影响力的思想家、创新者和领导者的智慧。我们的使命是构建高质量的AI智能体训练数据集，让这些杰出人物思维模式、沟通风格和价值观在AI中得以体现。

> *"向那些疯狂的家伙们致敬。他们特立独行，他们桀骜不驯，他们惹是生非，他们格格不入。"* — 史蒂夫·乔布斯

---

## 🧠 已收录人物

### 当前可用

| 人物 | 身份 | 时代 | 条目数 | 状态 |
|------|------|-----|---------|--------|
| **史蒂夫·乔布斯** | 苹果联合创始人 | 1955-2011 | 75+ | ✅ 可用 |
| **蒂姆·库克** | 苹果CEO | 2011-至今 | 75 | ✅ 可用 |
| **沃伦·巴菲特** | 伯克希尔·哈撒韦董事长 | 1930-至今 | 100+ | ✅ 可用 |
| **埃隆·马斯克** | Tesla/SpaceX/xAI CEO | 1971-至今 | 801 | ✅ 可用 |

### 即将推出

- 杰夫·贝索斯（亚马逊）
- 比尔·盖茨（微软）
- *更多...*

---

## 📊 语料库统计

### 🆕 埃隆·马斯克 (v1.0 — 2026年6月)
- **总条目**: 801条（400条推文 + 110个访谈片段 + 245条语录 + 46段少样本对话）
- **模块**: 10个（核心身份、思维框架、行为准则、推文、访谈、语录、少样本示例、知识库、质量控制、训练配置）
- **时间跨度**: 2010-2026年（截至2026年5月）
- **语言**: 中英双语（每条语料均含英文原文和中文翻译）
- **格式**: Markdown + JSON 双格式（171个文件）
- **来源**: X/Twitter、Lex Fridman播客、Joe Rogan Experience、All-In峰会、Tesla财报电话会议、Bloomberg、Forbes、TED、Starbase演讲
- **重点话题**: AI/AGI（Grok 3/4/5）、SpaceX（Starship、火星、IPO）、Tesla（FSD、Robotaxi）、Neuralink（脑机接口、10+患者）、DOGE（政府效率部）、xAI收购X、加密货币/Dogecoin、第一性原理思维、工程哲学
- **特色**: 2025-2026最新事件（DOGE、SpaceX-xAI 1.25万亿美元合并、Forbes 2026专访）、ChatML/ShareGPT转换指南、LoRA/QLoRA微调建议、防幻觉指南、风格迁移评估指标

---

## 💡 使用场景

### 1. AI智能体训练
训练AI模型模仿伟大人物的思维和说话风格：
- 以埃隆·马斯克、蒂姆·库克或史蒂夫·乔布斯的声音提供建议的聊天机器人
- 用于领导力、创新和工程的虚拟导师
- 用于教育的历史人物模拟

### 2. 研究与分析
- 研究成功领导者的沟通模式
- 分析思维随时间的演变
- 比较不同人物应对相似挑战的方法

---

## 📜 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件。

**注意**: 语料库内容收集自公开演讲、访谈和出版物，用于教育和研究目的。所有内容版权归其各自所有者。

---

<p align="center">
  <i>"求知若饥，虚心若愚。" — 史蒂夫·乔布斯</i><br>
  <i>"生活不是要你站在边线围观。" — 蒂姆·库克</i><br>
  <i>"当某件事足够重要时，即使胜算不大，你也要去做。" — 埃隆·马斯克</i>
</p>

---

*Last Updated: June 1, 2026*
*Version: 2.0*
