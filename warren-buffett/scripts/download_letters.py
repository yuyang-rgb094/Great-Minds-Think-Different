#!/usr/bin/env python3
"""
Berkshire Hathaway Shareholder Letters Downloader

下载1977-2025年巴菲特致股东信
- 1977-2003: HTML格式
- 2004-2025: PDF格式
"""

import os
import time
import requests
from pathlib import Path
from urllib.parse import urljoin
import json

# 配置
BASE_URL = "https://www.berkshirehathaway.com/letters/"
HTML_YEARS = range(1977, 2004)  # 1977-2003
PDF_YEARS = range(2004, 2026)   # 2004-2025

# 输出目录
OUTPUT_DIR = Path("/sessions/6a1c46e4f6fd57d3a2670a81/workspace/warren-buffett-corpus/04-shareholder-letters")
HTML_DIR = OUTPUT_DIR / "raw" / "html"
PDF_DIR = OUTPUT_DIR / "raw" / "pdf"

# 请求配置
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2


def download_file(url: str, output_path: Path, description: str = "") -> bool:
    """下载文件，带重试机制"""
    for attempt in range(MAX_RETRIES):
        try:
            print(f"  下载: {description} (尝试 {attempt + 1}/{MAX_RETRIES})")
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"  ✓ 成功: {output_path.name}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ 失败: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
    
    return False


def download_html_letters():
    """下载HTML格式信函 (1977-2003)"""
    print("\n=== 下载HTML格式信函 (1977-2003) ===")
    results = []
    
    for year in HTML_YEARS:
        url = f"{BASE_URL}{year}.html"
        output_path = HTML_DIR / f"{year}.html"
        
        success = download_file(url, output_path, f"{year}年信函")
        results.append({
            "year": year,
            "format": "html",
            "url": url,
            "success": success,
            "file": str(output_path) if success else None
        })
        
        time.sleep(0.5)  # 避免请求过快
    
    return results


def download_pdf_letters():
    """下载PDF格式信函 (2004-2025)"""
    print("\n=== 下载PDF格式信函 (2004-2025) ===")
    results = []
    
    for year in PDF_YEARS:
        url = f"{BASE_URL}{year}ltr.pdf"
        output_path = PDF_DIR / f"{year}ltr.pdf"
        
        success = download_file(url, output_path, f"{year}年信函")
        results.append({
            "year": year,
            "format": "pdf",
            "url": url,
            "success": success,
            "file": str(output_path) if success else None
        })
        
        time.sleep(0.5)  # 避免请求过快
    
    return results


def generate_index(html_results: list, pdf_results: list):
    """生成索引文件"""
    all_results = html_results + pdf_results
    
    index = {
        "description": "Berkshire Hathaway Shareholder Letters Index",
        "total_letters": len(all_results),
        "successful": sum(1 for r in all_results if r["success"]),
        "failed": sum(1 for r in all_results if not r["success"]),
        "years": {
            "html": list(HTML_YEARS),
            "pdf": list(PDF_YEARS)
        },
        "letters": all_results
    }
    
    index_path = OUTPUT_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"\n索引文件已生成: {index_path}")
    return index


def generate_statistics(index: dict):
    """生成统计文件"""
    stats = {
        "total_letters": index["total_letters"],
        "successful_downloads": index["successful"],
        "failed_downloads": index["failed"],
        "html_letters": len(index["years"]["html"]),
        "pdf_letters": len(index["years"]["pdf"]),
        "year_range": {
            "start": 1977,
            "end": 2025
        },
        "file_sizes": {}
    }
    
    # 计算文件大小
    for letter in index["letters"]:
        if letter["success"] and letter["file"]:
            file_path = Path(letter["file"])
            if file_path.exists():
                stats["file_sizes"][letter["year"]] = file_path.stat().st_size
    
    stats_path = OUTPUT_DIR / "statistics.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"统计文件已生成: {stats_path}")


def main():
    print("=" * 60)
    print("Berkshire Hathaway 股东信下载器")
    print("=" * 60)
    
    # 创建输出目录
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    
    # 下载HTML格式信函
    html_results = download_html_letters()
    
    # 下载PDF格式信函
    pdf_results = download_pdf_letters()
    
    # 生成索引和统计
    index = generate_index(html_results, pdf_results)
    generate_statistics(index)
    
    # 总结
    print("\n" + "=" * 60)
    print("下载完成!")
    print(f"  总计: {index['total_letters']} 封信函")
    print(f"  成功: {index['successful']} 封")
    print(f"  失败: {index['failed']} 封")
    print("=" * 60)


if __name__ == "__main__":
    main()
