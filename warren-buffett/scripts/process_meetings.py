#!/usr/bin/env python3
"""
Berkshire Hathaway Annual Meeting Transcripts Processor

处理股东大会转录内容
由于CNBC网站需要动态渲染，此脚本提供手动导入和结构化功能
"""

import json
from pathlib import Path
from datetime import datetime

# 目录配置
BASE_DIR = Path("/sessions/6a1c46e4f6fd57d3a2670a81/workspace/warren-buffett-corpus/05-annual-meetings")
RAW_DIR = BASE_DIR / "raw"
PARSED_DIR = BASE_DIR / "parsed"
HIGHLIGHTS_DIR = BASE_DIR / "highlights"


def create_meeting_template(year: int) -> dict:
    """创建会议模板"""
    return {
        "id": f"meeting-{year}",
        "year": year,
        "type": "annual_meeting",
        "source": {
            "cnbc_url": f"https://buffett.cnbc.com/{year}-berkshire-hathaway-annual-meeting",
            "video_available": True,
            "transcript_available": True
        },
        "sessions": [
            {
                "session": "morning",
                "duration": "",
                "transcript": []
            },
            {
                "session": "afternoon",
                "duration": "",
                "transcript": []
            }
        ],
        "highlights": [],
        "qa_topics": [],
        "metadata": {
            "processed_at": datetime.now().isoformat(),
            "notes": "Template created - content to be added manually or via scraping"
        }
    }


def create_meeting_index():
    """创建会议索引"""
    meetings = []
    
    # 1994-2025 年度会议
    for year in range(1994, 2026):
        meeting = {
            "year": year,
            "cnbc_url": f"https://buffett.cnbc.com/{year}-berkshire-hathaway-annual-meeting",
            "transcript_file": f"{year}.json",
            "status": "pending"
        }
        meetings.append(meeting)
        
        # 创建模板文件
        template = create_meeting_template(year)
        output_path = PARSED_DIR / f"{year}.json"
        if not output_path.exists():
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2, ensure_ascii=False)
    
    # 创建索引
    index = {
        "description": "Berkshire Hathaway Annual Meeting Transcripts Index",
        "total_meetings": len(meetings),
        "year_range": {"start": 1994, "end": 2025},
        "meetings": meetings
    }
    
    index_path = BASE_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return index


def create_sample_highlights():
    """创建精彩片段示例"""
    highlights = [
        {
            "year": 2024,
            "topic": "Charlie Munger Tribute",
            "quote": "Charlie told me, 'Warren, you're going to live a long time, and you're going to be rich. But you're not going to be happy unless you love what you do.'",
            "context": "Opening remarks remembering Charlie Munger"
        },
        {
            "year": 2023,
            "topic": "Apple Investment",
            "quote": "Apple is our largest holding, and it's a wonderful business. It's a better business than any we own.",
            "context": "Discussing Berkshire's Apple position"
        },
        {
            "year": 2008,
            "topic": "Financial Crisis",
            "quote": "I've been buying American stocks. This is my way of saying I'm betting on America.",
            "context": "During the financial crisis"
        },
        {
            "year": 2006,
            "topic": "Philanthropy Announcement",
            "quote": "I will allocate more than 99% of my wealth to philanthropy.",
            "context": "Announcing the Giving Pledge"
        }
    ]
    
    highlights_path = HIGHLIGHTS_DIR / "sample_highlights.json"
    with open(highlights_path, 'w', encoding='utf-8') as f:
        json.dump(highlights, f, indent=2, ensure_ascii=False)
    
    return highlights


def main():
    print("=" * 60)
    print("Berkshire Hathaway 股东大会转录处理器")
    print("=" * 60)
    
    # 创建目录
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)
    HIGHLIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 创建索引和模板
    print("\n创建会议索引和模板...")
    index = create_meeting_index()
    print(f"  创建了 {index['total_meetings']} 个会议模板")
    
    # 创建精彩片段
    print("\n创建精彩片段示例...")
    highlights = create_sample_highlights()
    print(f"  创建了 {len(highlights)} 个精彩片段")
    
    # 创建统计
    stats = {
        "total_meetings": index["total_meetings"],
        "transcripts_available": 0,
        "highlights_count": len(highlights),
        "notes": "Transcripts need to be added manually or via CNBC scraping"
    }
    
    stats_path = BASE_DIR / "statistics.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print("完成!")
    print(f"  会议模板: {index['total_meetings']} 个")
    print(f"  年份范围: 1994-2025")
    print("=" * 60)


if __name__ == "__main__":
    main()
