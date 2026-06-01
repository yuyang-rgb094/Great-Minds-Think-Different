# Elon Musk 推文语料库 — 推文索引 (Tweet Index)

> **总推文数量**: 400 | **分类数量**: 12 | **时间范围**: 2022-07 – 2026-05
> **说明**: 本索引列出所有推文分类、数量、时间范围和文件位置。

---

## 分类概览

| # | 分类 | 英文名 | 推文数量 | 时间范围 | 文件 |
|---|------|--------|----------|----------|------|
| 1 | AI与科技 | AI & Technology | 50 | 2022-07 – 2026-05 | `tweets-ai-tech` |
| 2 | 太空探索 | Space Exploration | 40 | 2022-08 – 2026-05 | `tweets-space-exploration` |
| 3 | 电动车 | Tesla / Electric Vehicles | 40 | 2022-09 – 2026-05 | `tweets-tesla-ev` |
| 4 | 能源 | Energy | 25 | 2022-10 – 2026-04 | `tweets-energy` |
| 5 | 加密货币/狗狗币 | Crypto / Dogecoin | 30 | 2022-10 – 2026-04 | `tweets-crypto-doge` |
| 6 | 言论自由 | Free Speech | 25 | 2022-10 – 2026-03 | `tweets-free-speech` |
| 7 | DOGE政府效率部 | DOGE Government Efficiency | 30 | 2025-01 – 2025-05 | `tweets-doge-government` |
| 8 | 幽默/梗 | Humor / Memes | 30 | 2022-10 – 2026-03 | `tweets-humor-memes` |
| 9 | 人生哲学 | Philosophy / Life | 25 | 2022-11 – 2026-03 | `tweets-philosophy-life` |
| 10 | 商业建议 | Business Advice | 20 | 2022-11 – 2026-01 | `tweets-business-advice` |
| 11 | xAI收购X | xAI Acquisition of X | 20 | 2025-03 – 2026-05 | `tweets-xai-acquisition` |
| 12 | SpaceX IPO | SpaceX IPO | 15 | 2026-01 – 2026-05 | `tweets-spacex-ipo` |

---

## 按时间分布

| 年份 | 推文数量 | 主要主题 |
|------|----------|----------|
| 2022 | ~45 | AI安全、SpaceX、Tesla、言论自由 |
| 2023 | ~95 | Grok发布、Starship测试、Cybertruck、FSD、DOGE |
| 2024 | ~110 | Grok 2/3、Robotaxi、SpaceX着陆、言论自由、加密货币 |
| 2025 | ~120 | Grok 3/4、DOGE政府效率部、xAI收购X、Robotaxi测试、火星任务 |
| 2026 | ~30 | Grok 5、SpaceX IPO、xAI-SpaceX合并、火星货运任务 |

---

## 高互动推文 (>100M views)

| 排名 | 分类 | 推文 | 浏览量 | 日期 |
|------|------|------|--------|------|
| 1 | 言论自由 | "The bird is freed." | 125M | 2022-10-27 |
| 2 | DOGE政府效率部 | DOGE任命声明 | 140M | 2025-01-20 |
| 3 | SpaceX IPO | "SpaceX is going public." | 140M | 2026-01-15 |
| 4 | AI与科技 | AGI预测 (All-In Podcast) | 120M | 2023-03-04 |
| 5 | 电动车 | Cybertruck首批交付 | 120M | 2023-11-30 |
| 6 | 太空探索 | Starship助推器首次捕获 | 125M | 2024-03-05 |
| 7 | AI与科技 | Grok 3发布 | 115M | 2025-01-15 |
| 8 | 加密货币/狗狗币 | 420日庆祝 | 108M | 2023-04-20 |
| 9 | 言论自由 | "Free speech is the bedrock" | 108M | 2022-11-05 |
| 10 | SpaceX IPO | STAR首日交易 | 120M | 2026-03-16 |

---

## 风格标记分布

| 风格标记 | 出现频率 | 主要分类 |
|----------|----------|----------|
| visionary | 高 | AI、太空、能源 |
| proud | 高 | Tesla、SpaceX、xAI |
| humorous | 中 | 加密货币、幽默/梗 |
| provocative | 中 | AI、言论自由、DOGE政府 |
| philosophical | 中 | 人生哲学、言论自由 |
| announcement | 高 | 所有分类 |
| technical | 中 | AI、太空、Tesla |
| self-deprecating | 低 | 幽默/梗、加密货币 |

---

## 数据格式说明

每个分类包含两个文件：
- **`.md`** — Markdown格式，适合人类阅读
- **`.json`** — JSON格式，适合程序化处理

每条推文包含：
- 英文原文和中文翻译
- 发布日期和互动数据（点赞、转发、回复、浏览量）
- 上下文说明
- 风格标记（用于AI训练的风格特征）
- 质量评分（0.0-1.0，基于真实性和代表性）

---

> **语料库版本**: 1.0 | **最后更新**: 2026-06-01
> **维护者**: Elon Musk AI Agent Corpus Project
