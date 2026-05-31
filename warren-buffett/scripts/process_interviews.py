#!/usr/bin/env python3
"""
CNBC Interviews Processor

处理CNBC访谈内容
"""

import json
from pathlib import Path
from datetime import datetime

# 目录配置
BASE_DIR = Path("/sessions/6a1c46e4f6fd57d3a2670a81/workspace/warren-buffett-corpus/06-interviews")
RAW_DIR = BASE_DIR / "raw"
PARSED_DIR = BASE_DIR / "parsed"


# 已知的关键访谈
KNOWN_INTERVIEWS = [
    {
        "id": "interview-2023-11-14",
        "date": "2023-11-14",
        "title": "Charlie Munger Final Interview",
        "description": "Tribute to Charlie Munger following his passing",
        "interviewer": "Becky Quick",
        "duration": "1:44:37",
        "cnbc_url": "https://buffett.cnbc.com/video/2023/11/29/buffett-on-charlie-munger-he-was-the-architect-of-berkshire.html",
        "key_topics": ["charlie_munger", "tribute", "partnership"],
        "notable": True
    },
    {
        "id": "interview-2023-04-12",
        "date": "2023-04-12",
        "title": "Buffett: More banks may fail but U.S. depositors will be OK",
        "description": "Comments on banking crisis and deposit safety",
        "interviewer": "Becky Quick",
        "duration": "2:29:30",
        "cnbc_url": "https://buffett.cnbc.com/video/2023/04/17/buffett-more-banks-may-fail-but-us-depositors-will-be-ok.html",
        "key_topics": ["banking_crisis", "deposits", "regulation"],
        "notable": True
    },
    {
        "id": "interview-2020-02-24",
        "date": "2020-02-24",
        "title": "Buffett on Market Volatility and Investment Strategy",
        "description": "Market advice during early COVID period",
        "interviewer": "Becky Quick",
        "duration": "2:04:31",
        "cnbc_url": "https://buffett.cnbc.com/video/2020/02/24/buffett-on-market-volatility-and-investment-strategy.html",
        "key_topics": ["covid", "market_volatility", "investment"],
        "notable": True
    },
    {
        "id": "interview-2018-05-07",
        "date": "2018-05-07",
        "title": "Buffett on Bitcoin and Cryptocurrency",
        "description": "Famous criticism of cryptocurrency",
        "interviewer": "Becky Quick",
        "duration": "2:10:19",
        "cnbc_url": "https://buffett.cnbc.com/video/2018/05/07/buffett-on-bitcoin-and-cryptocurrency.html",
        "key_topics": ["bitcoin", "cryptocurrency", "speculation"],
        "notable": True,
        "key_quote": "Bitcoin is probably rat poison squared."
    },
    {
        "id": "interview-2017-05-08",
        "date": "2017-05-08",
        "title": "Buffett on Apple and IBM",
        "description": "Discussing Apple investment and IBM sale",
        "interviewer": "Becky Quick",
        "duration": "2:10:19",
        "cnbc_url": "https://buffett.cnbc.com/video/2017/05/08/buffett-on-apple-and-ibm.html",
        "key_topics": ["apple", "ibm", "technology_investment"],
        "notable": True
    }
]


def create_interview_structure():
    """创建访谈结构"""
    interviews = []
    
    for interview in KNOWN_INTERVIEWS:
        interview_data = {
            **interview,
            "type": "cnbc_interview",
            "source": {
                "cnbc_url": interview["cnbc_url"],
                "transcript_available": False,
                "video_available": True
            },
            "transcript": [],
            "key_quotes": [],
            "metadata": {
                "processed_at": datetime.now().isoformat(),
                "notes": "Transcript to be added"
            }
        }
        
        # 如果有key_quote，添加到key_quotes
        if "key_quote" in interview:
            interview_data["key_quotes"].append({
                "quote": interview["key_quote"],
                "context": interview["description"]
            })
        
        interviews.append(interview_data)
        
        # 保存单个文件
        output_path = PARSED_DIR / f"{interview['id']}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(interview_data, f, indent=2, ensure_ascii=False)
    
    return interviews


def create_index(interviews: list):
    """创建索引"""
    index = {
        "description": "Warren Buffett CNBC Interviews Index",
        "total_interviews": len(interviews),
        "notable_interviews": sum(1 for i in interviews if i.get("notable")),
        "interviews": [
            {
                "id": i["id"],
                "date": i["date"],
                "title": i["title"],
                "key_topics": i["key_topics"]
            }
            for i in interviews
        ]
    }
    
    index_path = BASE_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return index


def create_statistics(interviews: list):
    """创建统计"""
    # 收集所有主题
    all_topics = []
    for i in interviews:
        all_topics.extend(i.get("key_topics", []))
    
    stats = {
        "total_interviews": len(interviews),
        "notable_interviews": sum(1 for i in interviews if i.get("notable")),
        "total_topics": len(set(all_topics)),
        "topics_found": list(set(all_topics)),
        "date_range": {
            "earliest": min(i["date"] for i in interviews),
            "latest": max(i["date"] for i in interviews)
        }
    }
    
    stats_path = BASE_DIR / "statistics.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    return stats


def main():
    print("=" * 60)
    print("CNBC 访谈处理器")
    print("=" * 60)
    
    # 创建目录
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)
    
    # 创建访谈结构
    print("\n创建访谈结构...")
    interviews = create_interview_structure()
    print(f"  创建了 {len(interviews)} 个访谈记录")
    
    # 创建索引
    print("\n创建索引...")
    index = create_index(interviews)
    
    # 创建统计
    print("\n创建统计...")
    stats = create_statistics(interviews)
    
    print("\n" + "=" * 60)
    print("完成!")
    print(f"  访谈记录: {stats['total_interviews']} 个")
    print(f"  重要访谈: {stats['notable_interviews']} 个")
    print(f"  主题数量: {stats['total_topics']} 个")
    print("=" * 60)


if __name__ == "__main__":
    main()
