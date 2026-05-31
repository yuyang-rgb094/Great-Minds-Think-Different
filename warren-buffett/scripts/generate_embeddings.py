#!/usr/bin/env python3
"""
Embeddings Generator for Warren Buffett Corpus

使用OpenAI text-embedding-3-large生成向量嵌入
存储到ChromaDB
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime

# 目录配置
CORPUS_DIR = Path("/sessions/6a1c46e4f6fd57d3a2670a81/workspace/warren-buffett-corpus")
EMBEDDINGS_DIR = CORPUS_DIR / "11-embeddings"

# 嵌入配置
EMBEDDING_CONFIG = {
    "model": {
        "name": "text-embedding-3-large",
        "provider": "openai",
        "dimensions": 3072,
        "max_tokens": 8191
    },
    "chunking": {
        "strategy": "semantic",
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "min_chunk_size": 100
    }
}


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """简单文本分块"""
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        # 尝试在句子边界分割
        if end < len(text):
            # 查找最后一个句号
            last_period = chunk.rfind('.')
            if last_period > chunk_size * 0.5:
                chunk = chunk[:last_period + 1]
                end = start + last_period + 1
        
        chunks.append(chunk.strip())
        start = end - overlap
    
    return chunks


def generate_chunk_id(text: str, source_id: str, index: int) -> str:
    """生成chunk ID"""
    hash_input = f"{source_id}_{index}_{text[:50]}"
    return hashlib.md5(hash_input.encode()).hexdigest()[:16]


def load_corpus_content() -> list:
    """加载语料库内容"""
    documents = []
    
    # 加载股东信
    letters_dir = CORPUS_DIR / "04-shareholder-letters" / "parsed"
    if letters_dir.exists():
        for letter_file in letters_dir.glob("*.json"):
            with open(letter_file, 'r', encoding='utf-8') as f:
                letter = json.load(f)
                if "content" in letter and "full_text" in letter["content"]:
                    documents.append({
                        "id": letter["id"],
                        "type": "shareholder_letter",
                        "year": letter["year"],
                        "text": letter["content"]["full_text"],
                        "metadata": letter.get("metadata", {})
                    })
    
    # 加载语录
    quotes_dir = CORPUS_DIR / "07-quotes"
    if quotes_dir.exists():
        for quotes_file in quotes_dir.glob("*.json"):
            with open(quotes_file, 'r', encoding='utf-8') as f:
                quotes_data = json.load(f)
                for quote in quotes_data.get("quotes", []):
                    content = quote.get("content", {})
                    text = content.get("en", "")
                    if text:
                        documents.append({
                            "id": quote["id"],
                            "type": "quote",
                            "category": quotes_data["id"],
                            "text": text,
                            "text_zh": content.get("zh", ""),
                            "metadata": {
                                "source": quote.get("source", ""),
                                "themes": quote.get("themes", []),
                                "wisdom_score": quote.get("wisdom_score", 0)
                            }
                        })
    
    # 加载思维框架
    frameworks_dir = CORPUS_DIR / "02-thinking-frameworks"
    if frameworks_dir.exists():
        for framework_file in frameworks_dir.glob("*.json"):
            with open(framework_file, 'r', encoding='utf-8') as f:
                framework = json.load(f)
                # 提取框架中的关键文本
                text_parts = []
                if "description" in framework:
                    desc = framework["description"]
                    if isinstance(desc, dict):
                        text_parts.append(desc.get("en", ""))
                    else:
                        text_parts.append(str(desc))
                
                # 提取原则和引用
                for key in ["core_principles", "principles", "factors"]:
                    if key in framework:
                        for item in framework[key]:
                            if isinstance(item, dict):
                                if "buffett_quote" in item:
                                    quote = item["buffett_quote"]
                                    if isinstance(quote, dict):
                                        text_parts.append(quote.get("en", ""))
                
                if text_parts:
                    documents.append({
                        "id": framework["id"],
                        "type": "thinking_framework",
                        "text": "\n\n".join(text_parts),
                        "metadata": {"title": framework.get("title", {})}
                    })
    
    return documents


def prepare_chunks(documents: list) -> list:
    """准备嵌入分块"""
    chunks = []
    chunk_config = EMBEDDING_CONFIG["chunking"]
    
    for doc in documents:
        text = doc["text"]
        
        if len(text) <= chunk_config["chunk_size"]:
            # 小文档不分块
            chunks.append({
                "id": generate_chunk_id(text, doc["id"], 0),
                "source_id": doc["id"],
                "text": text,
                "metadata": {
                    "type": doc["type"],
                    **doc.get("metadata", {})
                }
            })
        else:
            # 大文档分块
            doc_chunks = chunk_text(
                text,
                chunk_config["chunk_size"],
                chunk_config["chunk_overlap"]
            )
            
            for i, chunk_text_item in enumerate(doc_chunks):
                chunks.append({
                    "id": generate_chunk_id(chunk_text_item, doc["id"], i),
                    "source_id": doc["id"],
                    "text": chunk_text_item,
                    "metadata": {
                        "type": doc["type"],
                        "chunk_index": i,
                        "total_chunks": len(doc_chunks),
                        **doc.get("metadata", {})
                    }
                })
    
    return chunks


def create_embedding_config(chunks: list):
    """创建嵌入配置文件"""
    config = {
        **EMBEDDING_CONFIG,
        "created_at": datetime.now().isoformat(),
        "statistics": {
            "total_chunks": len(chunks),
            "total_characters": sum(len(c["text"]) for c in chunks),
            "source_types": list(set(c["metadata"]["type"] for c in chunks))
        }
    }
    
    config_path = EMBEDDINGS_DIR / "embedding_config.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    return config


def create_chunk_statistics(chunks: list):
    """创建分块统计"""
    # 按类型统计
    type_counts = {}
    for chunk in chunks:
        chunk_type = chunk["metadata"]["type"]
        type_counts[chunk_type] = type_counts.get(chunk_type, 0) + 1
    
    stats = {
        "total_chunks": len(chunks),
        "total_characters": sum(len(c["text"]) for c in chunks),
        "average_chunk_size": sum(len(c["text"]) for c in chunks) // len(chunks) if chunks else 0,
        "by_type": type_counts,
        "created_at": datetime.now().isoformat()
    }
    
    stats_path = EMBEDDINGS_DIR / "chunk_statistics.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    return stats


def create_search_examples():
    """创建搜索示例"""
    examples = [
        {
            "query": "What is margin of safety?",
            "expected_topics": ["value_investing", "margin_of_safety"],
            "description": "Search for margin of safety concept"
        },
        {
            "query": "How does Buffett think about market timing?",
            "expected_topics": ["market_psychology", "mr_market"],
            "description": "Search for market timing views"
        },
        {
            "query": "What makes a good business?",
            "expected_topics": ["business_evaluation", "economic_moat"],
            "description": "Search for business quality criteria"
        },
        {
            "query": "Buffett's advice on diversification",
            "expected_topics": ["portfolio_strategy", "concentration"],
            "description": "Search for diversification views"
        }
    ]
    
    examples_path = EMBEDDINGS_DIR / "search_examples.json"
    with open(examples_path, 'w', encoding='utf-8') as f:
        json.dump(examples, f, indent=2, ensure_ascii=False)
    
    return examples


def main():
    print("=" * 60)
    print("Warren Buffett 语料库嵌入生成器")
    print("=" * 60)
    
    # 创建目录
    EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)
    (EMBEDDINGS_DIR / "chroma_db").mkdir(parents=True, exist_ok=True)
    
    # 加载语料库内容
    print("\n加载语料库内容...")
    documents = load_corpus_content()
    print(f"  加载了 {len(documents)} 个文档")
    
    # 准备分块
    print("\n准备嵌入分块...")
    chunks = prepare_chunks(documents)
    print(f"  生成了 {len(chunks)} 个分块")
    
    # 创建配置和统计
    print("\n创建配置文件...")
    config = create_embedding_config(chunks)
    
    print("\n创建分块统计...")
    stats = create_chunk_statistics(chunks)
    
    print("\n创建搜索示例...")
    examples = create_search_examples()
    
    # 保存分块数据（供后续嵌入使用）
    chunks_path = EMBEDDINGS_DIR / "chunks_data.json"
    with open(chunks_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print("完成!")
    print(f"  文档数: {len(documents)}")
    print(f"  分块数: {stats['total_chunks']}")
    print(f"  总字符: {stats['total_characters']:,}")
    print(f"  平均分块大小: {stats['average_chunk_size']}")
    print("\n注意: 需要安装chromadb和openai包并配置API密钥")
    print("      才能生成实际的向量嵌入")
    print("=" * 60)


if __name__ == "__main__":
    main()
