#!/usr/bin/env python3
"""
Berkshire Hathaway Shareholder Letters Parser

解析下载的股东信，提取文本内容并结构化
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

# 尝试导入PDF解析库
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    print("警告: PyMuPDF未安装，PDF解析功能不可用")

# 尝试导入HTML解析库
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    print("警告: BeautifulSoup未安装，HTML解析功能不可用")

# 目录配置
BASE_DIR = Path("/sessions/6a1c46e4f6fd57d3a2670a81/workspace/warren-buffett-corpus/04-shareholder-letters")
HTML_DIR = BASE_DIR / "raw" / "html"
PDF_DIR = BASE_DIR / "raw" / "pdf"
PARSED_DIR = BASE_DIR / "parsed"


def parse_html_letter(file_path: Path) -> dict:
    """解析HTML格式信函"""
    if not HAS_BS4:
        return {"error": "BeautifulSoup未安装"}
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 提取标题
    title = soup.title.string if soup.title else ""
    
    # 提取正文
    # Berkshire的HTML信函结构相对简单
    body = soup.find('body')
    if body:
        # 移除脚本和样式
        for script in body(['script', 'style']):
            script.decompose()
        
        # 提取文本
        text = body.get_text(separator='\n', strip=True)
        
        # 清理多余空行
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        text = '\n'.join(lines)
    else:
        text = soup.get_text(separator='\n', strip=True)
    
    return {
        "title": title,
        "full_text": text,
        "word_count": len(text.split()),
        "char_count": len(text)
    }


def parse_pdf_letter(file_path: Path) -> dict:
    """解析PDF格式信函"""
    if not HAS_PYMUPDF:
        return {"error": "PyMuPDF未安装"}
    
    doc = fitz.open(file_path)
    
    full_text = []
    pages_content = []
    
    for page_num, page in enumerate(doc):
        # 提取文本
        text = page.get_text("text")
        
        # 清理文本
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        clean_text = '\n'.join(lines)
        
        pages_content.append({
            "page": page_num + 1,
            "text": clean_text,
            "char_count": len(clean_text)
        })
        
        full_text.append(clean_text)
    
    doc.close()
    
    combined_text = '\n\n'.join(full_text)
    
    return {
        "title": f"Berkshire Hathaway Annual Letter",
        "full_text": combined_text,
        "pages": pages_content,
        "page_count": len(pages_content),
        "word_count": len(combined_text.split()),
        "char_count": len(combined_text)
    }


def extract_sections(text: str) -> list:
    """尝试识别信函的章节结构"""
    sections = []
    
    # 常见的章节标题模式
    patterns = [
        r'^[A-Z][A-Z\s]+$',  # 全大写标题
        r'^\d+\.\s+[A-Z]',   # 数字编号标题
        r'^To the Shareholders',  # 开头
    ]
    
    lines = text.split('\n')
    current_section = {"title": "Introduction", "content": []}
    
    for line in lines:
        is_header = False
        for pattern in patterns:
            if re.match(pattern, line) and len(line) < 100:
                if current_section["content"]:
                    sections.append({
                        "title": current_section["title"],
                        "content": '\n'.join(current_section["content"])
                    })
                current_section = {"title": line, "content": []}
                is_header = True
                break
        
        if not is_header:
            current_section["content"].append(line)
    
    # 添加最后一个章节
    if current_section["content"]:
        sections.append({
            "title": current_section["title"],
            "content": '\n'.join(current_section["content"])
        })
    
    return sections


def extract_key_quotes(text: str) -> list:
    """提取关键引用（简化版）"""
    quotes = []
    
    # 查找可能的引用模式
    # 巴菲特常用的一些表达模式
    patterns = [
        r'"([^"]{50,500})"',  # 双引号引用
        r'"([^"]{50,500})"',  # 中文引号
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if len(match.split()) > 10:  # 至少10个词
                quotes.append(match.strip())
    
    return quotes[:20]  # 最多返回20条


def identify_themes(text: str) -> list:
    """识别主题标签"""
    themes = []
    
    theme_keywords = {
        "insurance": ["insurance", "GEICO", "float", "underwriting"],
        "investments": ["investment", "stock", "bond", "portfolio"],
        "acquisitions": ["acquisition", "purchase", "buy", "deal"],
        "performance": ["earnings", "book value", "return", "performance"],
        "management": ["manager", "management", "CEO", "capital allocation"],
        "economics": ["economy", "GDP", "inflation", "interest rate"],
        "philosophy": ["principle", "philosophy", "think", "believe"],
        "mistakes": ["mistake", "error", "wrong", "lesson"],
        "charlie_munger": ["Charlie", "Munger", "partner"]
    }
    
    text_lower = text.lower()
    
    for theme, keywords in theme_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                themes.append(theme)
                break
    
    return list(set(themes))


def process_letter(year: int, format_type: str, file_path: Path) -> dict:
    """处理单个信函"""
    print(f"  处理: {year}年 ({format_type})")
    
    # 解析内容
    if format_type == "html":
        parsed = parse_html_letter(file_path)
    else:
        parsed = parse_pdf_letter(file_path)
    
    if "error" in parsed:
        return {"year": year, "error": parsed["error"]}
    
    # 提取结构化信息
    text = parsed["full_text"]
    
    result = {
        "id": f"letter-{year}",
        "year": year,
        "type": "shareholder_letter",
        "source": {
            "url": f"https://www.berkshirehathaway.com/letters/{year}.html" if format_type == "html" else f"https://www.berkshirehathaway.com/letters/{year}ltr.pdf",
            "format": format_type,
            "file": str(file_path.name)
        },
        "content": {
            "full_text": text,
            "sections": extract_sections(text)[:10]  # 最多10个章节
        },
        "metadata": {
            "word_count": parsed["word_count"],
            "char_count": parsed["char_count"],
            "page_count": parsed.get("page_count", 1),
            "themes": identify_themes(text),
            "key_quotes_count": len(extract_key_quotes(text))
        },
        "extraction": {
            "key_quotes": extract_key_quotes(text),
            "processed_at": datetime.now().isoformat()
        }
    }
    
    return result


def main():
    print("=" * 60)
    print("Berkshire Hathaway 股东信解析器")
    print("=" * 60)
    
    PARSED_DIR.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    # 处理HTML信函
    print("\n=== 解析HTML格式信函 ===")
    if HTML_DIR.exists():
        for html_file in sorted(HTML_DIR.glob("*.html")):
            year = int(html_file.stem)
            result = process_letter(year, "html", html_file)
            results.append(result)
            
            # 保存单个解析结果
            output_path = PARSED_DIR / f"{year}.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
    
    # 处理PDF信函
    print("\n=== 解析PDF格式信函 ===")
    if PDF_DIR.exists() and HAS_PYMUPDF:
        for pdf_file in sorted(PDF_DIR.glob("*.pdf")):
            # 从文件名提取年份 (如 2024ltr.pdf -> 2024)
            year = int(pdf_file.stem.replace("ltr", ""))
            result = process_letter(year, "pdf", pdf_file)
            results.append(result)
            
            # 保存单个解析结果
            output_path = PARSED_DIR / f"{year}.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
    
    # 生成汇总统计
    stats = {
        "total_letters": len(results),
        "total_words": sum(r.get("metadata", {}).get("word_count", 0) for r in results),
        "total_chars": sum(r.get("metadata", {}).get("char_count", 0) for r in results),
        "years_processed": sorted([r["year"] for r in results]),
        "themes_found": list(set(theme for r in results for theme in r.get("metadata", {}).get("themes", [])))
    }
    
    stats_path = BASE_DIR / "parsing_stats.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print("解析完成!")
    print(f"  处理信函: {stats['total_letters']} 封")
    print(f"  总字数: {stats['total_words']:,}")
    print(f"  总字符: {stats['total_chars']:,}")
    print("=" * 60)


if __name__ == "__main__":
    main()
