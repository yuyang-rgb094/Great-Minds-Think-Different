# Contributing to Great Minds Think Different

Thank you for your interest in contributing to **Great Minds Think Different**! This document provides guidelines and instructions for contributing to this project.

## 🎯 Ways to Contribute

### 1. Adding New Quotes
Help expand existing corpora by adding verified quotes from public speeches, interviews, and publications.

### 2. Adding New Minds
Contribute entirely new corpora for influential thinkers not yet included in the project.

### 3. Improving Documentation
Help improve README files, documentation, and translations.

### 4. Reporting Issues
Report bugs, suggest improvements, or request new features via GitHub Issues.

---

## 📝 Guidelines for Adding Quotes

### Quality Standards

1. **Verifiable Sources**
   - All quotes must have verifiable sources
   - Include: event name, date, location, and URL when available
   - Prefer primary sources (speeches, interviews) over secondary sources

2. **Bilingual Content**
   - Provide both English and Chinese translations
   - Ensure translations are accurate and natural
   - Maintain the original tone and style

3. **Context Matters**
   - Include background information about when/where the quote was said
   - Explain the circumstances that led to this statement
   - Add relevant tags for easy categorization

4. **Categorization**
   - Assign appropriate category from the predefined list
   - Add 3-5 relevant tags
   - Indicate sentiment (positive/neutral/reflective)

### Entry Format

```json
{
  "id": "TC001",
  "category": "leadership",
  "type": "quote",
  "content_zh": "中文内容",
  "content_en": "English content",
  "context": "Background information",
  "source": {
    "title": "Source Title",
    "event": "Event Name",
    "date": "YYYY-MM-DD",
    "location": "Location",
    "url": "https://..."
  },
  "tags": ["tag1", "tag2"],
  "sentiment": "positive",
  "usage_scenarios": ["scenario1", "scenario2"]
}
```

### Categories

- `leadership` - Leadership & Management
- `innovation` - Innovation & Product
- `philosophy` - Philosophy & Values
- `personal_growth` - Personal Growth
- `business` - Business & Strategy
- `technology` - Technology & Future
- `privacy` - Privacy & Ethics

---

## 🧠 Guidelines for Adding New Minds

### Minimum Requirements

1. **At least 50 high-quality entries**
2. **Complete bilingual content** (English + Chinese)
3. **System prompt for AI training**
4. **Comprehensive README** following the template

### Directory Structure

```
great-mind-name/
├── corpus/
│   ├── corpus.json          # Structured data
│   └── corpus.md            # Human-readable version
├── training/
│   └── system_prompt.md     # AI agent system prompt
└── sources/                 # Raw source materials (optional)
```

### System Prompt Requirements

The system prompt should capture:
1. **Core personality traits**
2. **Communication style**
3. **Key values and beliefs**
4. **Common expressions and phrases**
5. **Response patterns for different topics**

See existing examples in `tim-cook/training/system_prompt.md` for reference.

---

## 🔄 Contribution Workflow

### Step 1: Fork the Repository
```bash
git clone https://github.com/your-username/Great-Minds-Think-Different.git
cd Great-Minds-Think-Different
```

### Step 2: Create a Branch
```bash
git checkout -b feature/add-tim-cook-quotes
# or
git checkout -b feature/add-elon-musk
```

### Step 3: Make Your Changes
- Add entries to appropriate corpus files
- Update metadata (total_entries, last_updated)
- Validate JSON syntax

### Step 4: Test Your Changes
```bash
# Validate JSON
python3 -c "import json; json.load(open('tim-cook/corpus/corpus.json'))"

# Check statistics
python3 scripts/corpus_stats.py
```

### Step 5: Commit and Push
```bash
git add .
git commit -m "Add X new quotes to Tim Cook corpus"
git push origin feature/add-tim-cook-quotes
```

### Step 6: Create Pull Request
- Provide clear description of changes
- List all new entries added
- Include source verification

---

## ✅ Review Criteria

Pull requests will be reviewed based on:

1. **Accuracy** - Are the quotes and translations accurate?
2. **Completeness** - Is all required information provided?
3. **Quality** - Do the entries meet quality standards?
4. **Originality** - Are the quotes from verifiable sources?
5. **Formatting** - Is the JSON valid and properly formatted?

---

## 🚫 What NOT to Include

1. **Unverified quotes** - Must have credible sources
2. **Copyrighted material** - Respect intellectual property
3. **Offensive content** - Keep it professional and respectful
4. **Duplicate entries** - Check existing corpus first
5. **Personal opinions** - Stick to documented statements

---

## 📞 Questions?

- Open a GitHub Issue for questions
- Join discussions in the GitHub Discussions tab
- Contact maintainers via email

---

## 🙏 Thank You!

Your contributions help preserve and share the wisdom of great minds for future generations. Thank you for being part of this project!

---

*Last Updated: May 31, 2025*
