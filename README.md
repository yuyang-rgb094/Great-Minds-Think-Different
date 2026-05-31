# Great Minds Think Different

<p align="center">
  <img src="https://img.shields.io/badge/Minds-Steve%20Jobs%20%7C%20Tim%20Cook-blue" alt="Minds">
  <img src="https://img.shields.io/badge/Total%20Entries-150%2B-green" alt="Entries">
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

### Coming Soon

- Elon Musk (Tesla, SpaceX, X)
- Jeff Bezos (Amazon)
- Bill Gates (Microsoft)
- Warren Buffett (Berkshire Hathaway)
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

# Load Tim Cook's corpus
with open('tim-cook/corpus/corpus.json', 'r', encoding='utf-8') as f:
    tim_cook_corpus = json.load(f)

# Filter by category
leadership_quotes = [
    entry for entry in tim_cook_corpus['entries']
    if entry['category'] == 'leadership'
]

# Filter by sentiment
positive_quotes = [
    entry for entry in tim_cook_corpus['entries']
    if entry['sentiment'] == 'positive'
]

print(f"Total entries: {len(tim_cook_corpus['entries'])}")
print(f"Leadership quotes: {len(leadership_quotes)}")
```

#### Using System Prompts

Each mind includes a carefully crafted system prompt for AI agents:

```python
# Read Tim Cook's system prompt
with open('tim-cook/training/system_prompt.md', 'r') as f:
    tim_cook_prompt = f.read()

# Use with your AI model
response = ai_model.generate(
    system_prompt=tim_cook_prompt,
    user_message="What makes a great leader?"
)
```

---

## 📊 Corpus Statistics

### Tim Cook
- **Total Entries**: 75
- **Categories**: 7 (Leadership, Innovation, Privacy, AI & Tech, Personal Growth, China Business, Steve Jobs Legacy)
- **Time Span**: 2015-2026
- **Languages**: English & Chinese (bilingual)
- **Sources**: Graduation speeches, interviews, privacy conference, retirement letter

### Steve Jobs
- **Total Entries**: 75+
- **Categories**: Multiple
- **Time Span**: 1976-2011
- **Languages**: English & Chinese
- **Sources**: Keynotes, interviews, All Things D, Stanford speech

---

## 🏗️ Corpus Format

Each entry follows a standardized schema:

```json
{
  "id": "TC001",
  "category": "leadership",
  "type": "quote",
  "content_zh": "生活不是要你站在边线围观...",
  "content_en": "Life is not about standing on the sidelines...",
  "context": "2015 GWU Commencement Speech",
  "source": {
    "title": "Tim Cook's 2015 GWU Speech",
    "event": "George Washington University Commencement",
    "date": "2015-05-17",
    "location": "Washington D.C.",
    "url": "..."
  },
  "tags": ["participation", "action", "life attitude"],
  "sentiment": "positive",
  "usage_scenarios": ["motivation", "commencement"]
}
```

### Categories

| ID | Name | Description |
|----|------|-------------|
| leadership | Leadership & Management | Team leadership, decision-making |
| innovation | Innovation & Product | Product design, user experience |
| privacy | Privacy & Values | Privacy protection, social responsibility |
| ai_technology | AI & Technology | Artificial intelligence, tech trends |
| personal_growth | Personal Growth | Career advice, life philosophy |
| china_business | China Market | China market, supply chain |
| steve_jobs | Steve Jobs Legacy | Jobs' influence, Apple history |

---

## 💡 Use Cases

### 1. AI Agent Training
Train AI models to emulate the thinking and speaking style of great minds:
- Chatbots that provide advice in the voice of Tim Cook or Steve Jobs
- Virtual mentors for leadership and innovation
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
2. Add entries to the appropriate `corpus.json` file
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
- Apple Inc. for changing the way we think about technology
- All contributors who help expand this collection

---

## 📬 Contact

- GitHub Issues: For bug reports and feature requests
- Discussions: For general questions and ideas
- Email: [Your contact email]

---

<p align="center">
  <i>"Stay hungry, stay foolish." — Steve Jobs</i><br>
  <i>"Life is not about standing on the sidelines." — Tim Cook</i>
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

### 即将推出

- 埃隆·马斯克（特斯拉、SpaceX、X）
- 杰夫·贝索斯（亚马逊）
- 比尔·盖茨（微软）
- 沃伦·巴菲特（伯克希尔·哈撒韦）
- *更多...*

---

## 📁 仓库结构

```
Great-Minds-Think-Different/
├── README.md                          # 本文件
├── CONTRIBUTING.md                    # 贡献指南
├── LICENSE                            # MIT许可证
│
├── steve-jobs/                        # 乔布斯语料
│   ├── corpus/
│   │   ├── corpus.json               # 结构化数据
│   │   └── corpus.md                 # 可读版本
│   ├── training/
│   │   └── system_prompt.md          # AI智能体提示词
│   └── sources/                      # 原始资料
│
├── tim-cook/                          # 库克语料
│   ├── corpus/
│   │   ├── corpus.json               # 结构化数据
│   │   └── corpus.md                 # 可读版本
│   ├── training/
│   │   └── system_prompt.md          # AI智能体提示词
│   └── sources/                      # 原始资料
│
└── templates/                         # 新人物模板
    ├── corpus_template.json
    ├── system_prompt_template.md
    └── README_template.md
```

---

## 🎯 快速开始

### 使用语料库进行AI训练

#### Python示例

```python
import json

# 加载库克语料库
with open('tim-cook/corpus/corpus.json', 'r', encoding='utf-8') as f:
    tim_cook_corpus = json.load(f)

# 按分类筛选
leadership_quotes = [
    entry for entry in tim_cook_corpus['entries']
    if entry['category'] == 'leadership'
]

# 按情感筛选
positive_quotes = [
    entry for entry in tim_cook_corpus['entries']
    if entry['sentiment'] == 'positive'
]

print(f"总条目数: {len(tim_cook_corpus['entries'])}")
print(f"领导力语录: {len(leadership_quotes)}")
```

#### 使用系统提示词

每个人物都包含精心设计的AI智能体系统提示词：

```python
# 读取库克的系统提示词
with open('tim-cook/training/system_prompt.md', 'r') as f:
    tim_cook_prompt = f.read()

# 用于你的AI模型
response = ai_model.generate(
    system_prompt=tim_cook_prompt,
    user_message="什么造就伟大的领导者？"
)
```

---

## 📊 语料库统计

### 蒂姆·库克
- **总条目**: 75条
- **分类**: 7大类（领导力、创新、隐私、AI与技术、个人成长、中国市场、乔布斯传承）
- **时间跨度**: 2015-2026年
- **语言**: 中英双语
- **来源**: 毕业演讲、访谈、隐私会议、卸任信

### 史蒂夫·乔布斯
- **总条目**: 75+条
- **分类**: 多个类别
- **时间跨度**: 1976-2011年
- **语言**: 中英双语
- **来源**: 发布会、访谈、D大会、斯坦福演讲

---

## 🏗️ 语料格式

每个条目遵循标准化结构：

```json
{
  "id": "TC001",
  "category": "leadership",
  "type": "quote",
  "content_zh": "生活不是要你站在边线围观...",
  "content_en": "Life is not about standing on the sidelines...",
  "context": "2015年乔治华盛顿大学毕业演讲",
  "source": {
    "title": "蒂姆·库克2015年演讲",
    "event": "乔治华盛顿大学毕业典礼",
    "date": "2015-05-17",
    "location": "华盛顿特区",
    "url": "..."
  },
  "tags": ["参与", "行动", "人生态度"],
  "sentiment": "positive",
  "usage_scenarios": ["激励", "毕业演讲"]
}
```

### 分类说明

| ID | 名称 | 描述 |
|----|------|-------------|
| leadership | 领导力与管理 | 团队领导、决策制定 |
| innovation | 创新与产品 | 产品设计、用户体验 |
| privacy | 隐私与价值观 | 隐私保护、社会责任 |
| ai_technology | AI与技术 | 人工智能、技术趋势 |
| personal_growth | 个人成长 | 职业建议、人生哲学 |
| china_business | 中国市场 | 中国市场、供应链 |
| steve_jobs | 乔布斯传承 | 乔布斯影响、苹果历史 |

---

## 💡 使用场景

### 1. AI智能体训练
训练AI模型模仿伟大人物的思维和说话风格：
- 以蒂姆·库克或史蒂夫·乔布斯的声音提供建议的聊天机器人
- 用于领导力与创新的虚拟导师
- 用于教育的历史人物模拟

### 2. 研究与分析
- 研究成功领导者的沟通模式
- 分析思维随时间的演变
- 比较不同人物应对相似挑战的方法

### 3. 内容创作
- 为演讲和文章生成引用
- 寻找演讲和写作的灵感
- 创建教育材料

### 4. 个人发展
- 向伟大人物的智慧学习
- 理解决策框架
- 学习领导哲学

---

## 🤝 贡献指南

我们欢迎贡献！你可以通过以下方式帮助：

### 添加新语录
1. Fork本仓库
2. 添加条目到相应的`corpus.json`文件
3. 确保双语内容（英文+中文）
4. 包含完整的来源信息
5. 提交Pull Request

### 添加新人物
1. 使用`/templates/`中的模板
2. 创建新目录：`great-mind-name/`
3. 遵循现有结构
4. 至少包含50条高质量条目
5. 提供AI训练用的系统提示词

### 质量标准
- 所有条目必须有可验证的来源
- 优先双语内容（英文+中文）
- 包含上下文和背景信息
- 适当标签以便筛选
- 尊重版权和合理使用

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📜 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件。

**注意**: 语料库内容收集自公开演讲、访谈和出版物，用于教育和研究目的。所有内容版权归其各自所有者。

---

## 🙏 致谢

- 史蒂夫·乔布斯的智慧继续激励着全世界数百万人
- 蒂姆·库克的领导力和对隐私的承诺
- 苹果公司改变了我们对技术的思考方式
- 所有帮助扩展这个收藏的 Contributors

---

<p align="center">
  <i>"求知若饥，虚心若愚。" — 史蒂夫·乔布斯</i><br>
  <i>"生活不是要你站在边线围观。" — 蒂姆·库克</i>
</p>

---

*Last Updated: May 31, 2025*  
*Version: 1.0*
