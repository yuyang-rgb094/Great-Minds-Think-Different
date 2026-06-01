# 微调建议 / Fine-tuning Recommendations

> 本指南提供针对埃隆·马斯克语料库的 LLM 微调技术建议，包括 LoRA/QLoRA 参数、数据混合策略、训练阶段和评估指标。
> This guide provides technical recommendations for LLM fine-tuning on the Elon Musk corpus, including LoRA/QLoRA parameters, data mixing strategies, training phases, and evaluation metrics.

---

## 目录 / Table of Contents

1. [LoRA/QLoRA 参数推荐 / LoRA/QLoRA Parameters](#loraqlora-参数推荐--loraqlora-parameters)
2. [数据混合策略 / Data Mixing Strategy](#数据混合策略--data-mixing-strategy)
3. [训练阶段配置 / Training Phases](#训练阶段配置--training-phases)
4. [硬件推荐 / Hardware Recommendations](#硬件推荐--hardware-recommendations)
5. [评估指标 / Evaluation Metrics](#评估指标--evaluation-metrics)
6. [2025-2026 时间敏感内容处理 / Handling Time-Sensitive Content](#2025-2026-时间敏感内容处理--handling-time-sensitive-content)

---

## LoRA/QLoRA 参数推荐 / LoRA/QLoRA Parameters

### Rank (r) 选择 / Rank Selection

Rank 决定了低秩适应矩阵的维度，影响模型的学习能力和过拟合风险。
Rank determines the dimension of low-rank adaptation matrices, affecting model learning capacity and overfitting risk.

| Rank | 适用场景 / Use Case | 显存需求 / VRAM | 说明 / Description |
|------|------------------|---------------|------------------|
| **8** | 快速实验 / Quick experiments | 低 / Low | 适合初步测试和快速迭代 |
| **16** | 标准微调 / Standard fine-tuning | 中 / Medium | 推荐默认值，平衡性能和资源 |
| **32** | 复杂人格 / Complex persona | 中高 / Med-High | 需要捕捉更多风格细节时使用 |
| **64** | 深度定制 / Deep customization | 高 / High | 最大学习能力，需更多数据防止过拟合 |

**推荐 / Recommendation:**
- 初始实验 / Initial experiments: `r=8`
- 生产微调 / Production fine-tuning: `r=16`
- 高质量需求 / High-quality requirements: `r=32`

### Alpha 值设置 / Alpha Values

Alpha 控制 LoRA 适应的缩放比例，通常设置为 Rank 的 1-2 倍。
Alpha controls the scaling of LoRA adaptation, typically set to 1-2x the Rank.

```python
# 推荐配置 / Recommended configurations
lora_configs = {
    "conservative": {"r": 8, "alpha": 16, "description": "保守配置，适合快速实验"},
    "balanced": {"r": 16, "alpha": 32, "description": "平衡配置，推荐默认值"},
    "aggressive": {"r": 32, "alpha": 64, "description": "激进配置，捕捉更多细节"},
    "maximum": {"r": 64, "alpha": 128, "description": "最大配置，需要更多数据"}
}
```

### 学习率 / Learning Rate

| 模型规模 / Model Size | 推荐学习率 / Recommended LR | 说明 / Notes |
|---------------------|--------------------------|-------------|
| 7B | 1e-4 ~ 2e-4 | 较高的学习率适合小模型 |
| 13B | 5e-5 ~ 1e-4 | 中等学习率 |
| 70B | 1e-5 ~ 5e-5 | 较低学习率防止不稳定 |

**学习率调度 / Learning Rate Schedule:**
```python
# 带预热的余弦退火 / Cosine annealing with warmup
lr_scheduler_type = "cosine"
warmup_ratio = 0.03  # 3% 的步数用于预热
learning_rate = 2e-4  # 根据模型大小调整
```

### 批次大小 / Batch Size

根据 GPU 显存选择批次大小：
Select batch size based on GPU VRAM:

| 显存 / VRAM | 批次大小 / Batch Size | 梯度累积 / Gradient Accumulation |
|------------|---------------------|-------------------------------|
| 16 GB | 1-2 | 4-8 |
| 24 GB | 2-4 | 4-8 |
| 40 GB | 4-8 | 2-4 |
| 80 GB | 8-16 | 1-2 |

**有效批次大小 / Effective Batch Size:**
```python
effective_batch_size = per_device_batch_size * gradient_accumulation_steps * num_gpus
# 推荐有效批次大小: 32-128
```

### 训练轮数 / Epochs

| 数据量 / Data Size | 推荐轮数 / Recommended Epochs | 说明 / Notes |
|------------------|----------------------------|-------------|
| < 1000 条 | 5-10 | 小数据集需要更多轮数 |
| 1000-5000 条 | 3-5 | 标准范围 |
| > 5000 条 | 2-3 | 大数据集避免过拟合 |

**早停策略 / Early Stopping:**
```python
early_stopping_patience = 3  # 3 轮无改善则停止
early_stopping_threshold = 0.001  # 改善阈值
```

### 完整 LoRA 配置示例 / Complete LoRA Configuration Example

```python
from peft import LoraConfig, TaskType

lora_config = LoraConfig(
    r=16,                          # Rank
    lora_alpha=32,                 # Alpha
    target_modules=[               # 目标模块
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],
    lora_dropout=0.05,             # Dropout
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

# 训练参数 / Training arguments
training_args = {
    "num_train_epochs": 3,
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 4,
    "learning_rate": 2e-4,
    "warmup_ratio": 0.03,
    "lr_scheduler_type": "cosine",
    "logging_steps": 10,
    "save_steps": 100,
    "eval_steps": 100,
    "save_total_limit": 3,
    "load_best_model_at_end": True,
    "metric_for_best_model": "eval_loss",
}
```

### QLoRA 量化配置 / QLoRA Quantization Config

```python
from transformers import BitsAndBytesConfig

# 4-bit 量化配置 / 4-bit quantization
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # 4-bit Normal Float
    bnb_4bit_compute_dtype="bfloat16",   # 计算精度
    bnb_4bit_use_double_quant=True,      # 嵌套量化
)

# 显存节省估计 / VRAM savings estimation:
# 7B 模型: ~14GB → ~6GB
# 13B 模型: ~26GB → ~10GB
# 70B 模型: ~140GB → ~40GB
```

---

## 数据混合策略 / Data Mixing Strategy

### 为什么需要混合 / Why Mixing is Important

仅使用马斯克语料库进行微调会导致：
Fine-tuning only on Musk corpus can lead to:
- **过拟合 / Overfitting**: 模型忘记通用知识
- **灾难性遗忘 / Catastrophic forgetting**: 丧失基础语言能力
- **风格过度 / Excessive style**: 每句话都像马斯克

### 推荐混合比例 / Recommended Mixing Ratios

| 比例 / Ratio | 语料库数据 / Corpus | 通用数据 / General | 适用场景 / Use Case |
|-------------|------------------|------------------|------------------|
| **30:70** | 30% | 70% | 保守微调，保留大部分通用能力 |
| **50:50** | 50% | 50% | 平衡方案，推荐默认 |
| **70:30** | 70% | 30% | 激进方案，更强的马斯克风格 |

### 通用数据来源 / General Data Sources

```python
# 推荐的通用数据集 / Recommended general datasets
general_datasets = {
    "alpaca": "tatsu-lab/alpaca",           # 指令跟随
    "dolly": "databricks/databricks-dolly-15k",  # 多样化指令
    "sharegpt": "anon8231489123/ShareGPT_Vicuna_unfiltered",  # 对话
    "ultrachat": "stingning/ultrachat",     # 高质量对话
}
```

### 数据混合实现 / Data Mixing Implementation

```python
from datasets import Dataset, concatenate_datasets

def mix_datasets(
    corpus_dataset: Dataset,
    general_dataset: Dataset,
    corpus_ratio: float = 0.5,
    seed: int = 42
) -> Dataset:
    """
    混合马斯克语料库和通用数据集
    Mix Musk corpus with general dataset
    
    Args:
        corpus_dataset: 马斯克语料库 / Musk corpus dataset
        general_dataset: 通用数据集 / General dataset
        corpus_ratio: 语料库比例 / Corpus ratio (0.0-1.0)
        seed: 随机种子 / Random seed
    
    Returns:
        混合后的数据集 / Mixed dataset
    """
    # 计算样本数 / Calculate sample counts
    total_size = len(corpus_dataset) / corpus_ratio
    corpus_size = len(corpus_dataset)
    general_size = int(total_size - corpus_size)
    
    # 采样通用数据 / Sample general data
    general_sampled = general_dataset.shuffle(seed=seed).select(range(general_size))
    
    # 合并 / Concatenate
    mixed = concatenate_datasets([corpus_dataset, general_sampled])
    
    # 打乱 / Shuffle
    mixed = mixed.shuffle(seed=seed)
    
    return mixed


# 使用示例 / Usage example
corpus_data = load_dataset("json", data_files="musk_corpus_chatml.jsonl")["train"]
general_data = load_dataset("tatsu-lab/alpaca")["train"]

mixed_50_50 = mix_datasets(corpus_data, general_data, corpus_ratio=0.5)
mixed_30_70 = mix_datasets(corpus_data, general_data, corpus_ratio=0.3)
```

### 按模块混合 / Module-Based Mixing

```python
# 不同模块使用不同比例 / Different ratios for different modules
module_mixing_ratios = {
    "01-core-identity": 0.8,        # 核心身份高比例
    "02-twitter-x-posts": 0.6,      # 推文中等比例
    "03-interview-quotes": 0.7,     # 访谈引用较高比例
    "04-few-shot-dialogues": 0.5,   # 对话平衡比例
    "05-speaking-style": 0.7,       # 说话风格较高比例
    "06-knowledge-base": 0.4,       # 知识库较低比例
    "07-response-patterns": 0.6,    # 回复模式中等比例
    "08-vocabulary-phrases": 0.5,   # 词汇平衡比例
    "09-contextual-awareness": 0.4, # 上下文感知较低比例
    "10-training-configs": 0.0,     # 训练配置不用于训练
}
```

---

## 训练阶段配置 / Training Phases

### 三阶段训练 / Three-Phase Training

```python
training_phases = {
    "phase_1_warmup": {
        "description": "预热阶段 / Warmup phase",
        "steps": 100,
        "learning_rate": 1e-5,  # 低学习率
        "description_cn": "让模型适应新数据分布",
        "description_en": "Let model adapt to new data distribution"
    },
    "phase_2_main": {
        "description": "主训练阶段 / Main training phase",
        "epochs": 3,
        "learning_rate": 2e-4,  # 标准学习率
        "description_cn": "主要学习马斯克风格",
        "description_en": "Main learning of Musk style"
    },
    "phase_3_finetune": {
        "description": "精调阶段 / Fine-tuning phase",
        "epochs": 1,
        "learning_rate": 5e-5,  # 低学习率精调
        "description_cn": "微调细节，防止过拟合",
        "description_en": "Fine-tune details, prevent overfitting"
    }
}
```

### 学习率调度 / Learning Rate Scheduling

```python
# 余弦退火调度 / Cosine annealing schedule
import numpy as np

def get_cosine_schedule_with_warmup(
    num_warmup_steps: int,
    num_training_steps: int,
    min_lr_ratio: float = 0.1
):
    """创建带预热的余弦学习率调度器"""
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        progress = float(current_step - num_warmup_steps) / float(
            max(1, num_training_steps - num_warmup_steps)
        )
        return max(min_lr_ratio, 0.5 * (1.0 + np.cos(np.pi * progress)))
    
    return lr_lambda


# 配置示例 / Configuration example
num_epochs = 3
batch_size = 4
dataset_size = 1000
num_training_steps = (dataset_size // batch_size) * num_epochs
num_warmup_steps = int(0.03 * num_training_steps)  # 3% 预热
```

### 评估策略 / Evaluation Strategy

```python
evaluation_strategy = {
    "frequency": "steps",           # 按步数评估
    "eval_steps": 100,              # 每 100 步评估
    "save_strategy": "steps",       # 按步数保存
    "save_steps": 100,              # 每 100 步保存
    "load_best_model_at_end": True, # 结束时加载最佳模型
    "metric_for_best_model": "eval_loss",  # 评估指标
    "greater_is_better": False,     # 指标越低越好
}
```

---

## 硬件推荐 / Hardware Recommendations

### 显存需求 / VRAM Requirements

| 模型 / Model | 全精度 / FP16 | 8-bit | 4-bit (QLoRA) |
|-------------|-------------|-------|--------------|
| 7B | 14 GB | 8 GB | 6 GB |
| 13B | 26 GB | 14 GB | 10 GB |
| 70B | 140 GB | 80 GB | 40 GB |

### GPU 推荐 / GPU Recommendations

**消费级 / Consumer Grade:**
- RTX 4090 (24GB): 适合 7B-13B 模型
- RTX 3090 (24GB): 适合 7B-13B 模型

**专业级 / Professional Grade:**
- A100 (40GB/80GB): 适合 70B 模型
- A6000 (48GB): 适合 70B 模型
- H100 (80GB): 适合 70B+ 模型

### 多 GPU 训练 / Multi-GPU Training

```python
# DeepSpeed 配置 / DeepSpeed configuration
deepspeed_config = {
    "train_batch_size": 32,
    "gradient_accumulation_steps": 4,
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": 2e-4,
            "betas": [0.9, 0.999],
            "eps": 1e-8,
            "weight_decay": 0.01
        }
    },
    "scheduler": {
        "type": "WarmupLR",
        "params": {
            "warmup_min_lr": 0,
            "warmup_max_lr": 2e-4,
            "warmup_num_steps": 100
        }
    },
    "zero_optimization": {
        "stage": 2,  # ZeRO-2 优化
        "offload_optimizer": {
            "device": "cpu",
            "pin_memory": True
        }
    }
}
```

### 训练时间估算 / Training Time Estimation

| 配置 / Config | 7B 模型 | 13B 模型 | 70B 模型 |
|-------------|--------|---------|---------|
| 单卡 A100 | ~2 小时 | ~4 小时 | ~20 小时 |
| 4x A100 | ~30 分钟 | ~1 小时 | ~5 小时 |
| 8x A100 | ~15 分钟 | ~30 分钟 | ~2.5 小时 |

---

## 评估指标 / Evaluation Metrics

### 自动评估 / Automatic Evaluation

#### 1. 困惑度 (Perplexity)

```python
import torch
import math

def calculate_perplexity(model, tokenizer, text: str) -> float:
    """计算文本的困惑度 / Calculate perplexity of text"""
    encodings = tokenizer(text, return_tensors="pt")
    input_ids = encodings.input_ids.to(model.device)
    
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss
    
    perplexity = math.exp(loss.item())
    return perplexity


# 评估标准 / Evaluation criteria:
# PPL < 10: 优秀 / Excellent
# 10 <= PPL < 20: 良好 / Good
# PPL >= 20: 需要改进 / Needs improvement
```

#### 2. 风格一致性 / Style Consistency

```python
def evaluate_style_consistency(
    generated_texts: List[str],
    reference_texts: List[str]
) -> Dict[str, float]:
    """
    评估生成文本与参考文本的风格一致性
    Evaluate style consistency between generated and reference texts
    """
    metrics = {
        "avg_length_ratio": 0.0,      # 平均长度比例
        "sentence_complexity": 0.0,   # 句子复杂度
        "technical_term_ratio": 0.0,  # 技术术语比例
        "first_person_ratio": 0.0,    # 第一人称比例
    }
    
    # 计算指标...
    
    return metrics
```

#### 3. 知识准确性 / Knowledge Accuracy

```python
# 事实检查问题 / Fact-checking questions
knowledge_questions = [
    {
        "question": "What companies does Elon Musk currently lead?",
        "expected_keywords": ["Tesla", "SpaceX", "X", "xAI", "Neuralink"]
    },
    {
        "question": "What is Elon Musk's stance on AI safety?",
        "expected_keywords": ["concern", "risk", "alignment", "xAI"]
    },
    {
        "question": "What is the goal of SpaceX?",
        "expected_keywords": ["Mars", "multi-planetary", "reusability"]
    }
]

def evaluate_knowledge_accuracy(model, tokenizer, questions: List[Dict]) -> float:
    """评估知识准确性 / Evaluate knowledge accuracy"""
    correct = 0
    total = len(questions)
    
    for q in questions:
        response = generate_response(model, tokenizer, q["question"])
        if any(keyword in response.lower() for keyword in q["expected_keywords"]):
            correct += 1
    
    return correct / total
```

### 人工评估 / Human Evaluation

#### 评估维度 / Evaluation Dimensions

| 维度 / Dimension | 说明 / Description | 评分标准 / Scale |
|----------------|------------------|----------------|
| **风格相似度** / Style Similarity | 回答是否像马斯克 | 1-5 分 |
| **知识准确性** / Knowledge Accuracy | 事实是否正确 | 1-5 分 |
| **流畅度** / Fluency | 语言是否自然流畅 | 1-5 分 |
| **一致性** / Consistency | 回答是否前后一致 | 1-5 分 |
| **有用性** / Helpfulness | 回答是否有帮助 | 1-5 分 |

#### 人工评估指南 / Human Evaluation Guidelines

```python
# 评估问题示例 / Evaluation questions
human_evaluation_questions = [
    "What drives you to pursue such ambitious goals?",
    "How do you approach problem-solving?",
    "What's your view on the future of AI?",
    "Tell me about a time you failed and what you learned.",
    "Why is sustainable energy important?",
    "What advice would you give to entrepreneurs?",
]

# 评分表 / Rating form
evaluation_form = {
    "question": "",
    "response": "",
    "ratings": {
        "style_similarity": 0,      # 1-5
        "knowledge_accuracy": 0,    # 1-5
        "fluency": 0,               # 1-5
        "consistency": 0,           # 1-5
        "helpfulness": 0,           # 1-5
    },
    "comments": ""
}
```

### 对比评估 / Comparative Evaluation

```python
def compare_models(
    base_model,
    fine_tuned_model,
    tokenizer,
    test_prompts: List[str]
) -> Dict[str, List[str]]:
    """
    对比基础模型和微调模型
    Compare base model and fine-tuned model
    """
    results = {
        "prompts": [],
        "base_responses": [],
        "fine_tuned_responses": [],
    }
    
    for prompt in test_prompts:
        base_response = generate_response(base_model, tokenizer, prompt)
        ft_response = generate_response(fine_tuned_model, tokenizer, prompt)
        
        results["prompts"].append(prompt)
        results["base_responses"].append(base_response)
        results["fine_tuned_responses"].append(ft_response)
    
    return results
```

---

## 2025-2026 时间敏感内容处理 / Handling Time-Sensitive Content

### 时间戳标记 / Timestamp Tagging

```python
# 为训练数据添加时间戳 / Add timestamps to training data
def add_temporal_context(example: Dict) -> Dict:
    """为示例添加时间上下文"""
    date = example.get("date", "")
    
    if date:
        year = int(date.split("-")[0])
        if year >= 2025:
            example["temporal_context"] = f"As of {date}, "
            example["system_prompt_suffix"] = "You are speaking in 2025-2026."
    
    return example
```

### 动态知识更新 / Dynamic Knowledge Updates

```python
# 2025-2026 年特定知识 / 2025-2026 specific knowledge
current_events_2025_2026 = {
    "starship_status": "Multiple successful orbital flights achieved",
    "tesla_fsd": "End-to-end neural network approach deployed",
    "xai_grok": "Competing with major AI models",
    "neuralink": "Human trials underway with promising results",
    "x_platform": "Significant platform changes implemented",
}

def inject_current_knowledge(system_prompt: str, date: str) -> str:
    """将当前知识注入系统提示词"""
    if "2025" in date or "2026" in date:
        context = "Current context (2025-2026):\n"
        for key, value in current_events_2025_2026.items():
            context += f"- {key}: {value}\n"
        
        system_prompt = system_prompt + "\n\n" + context
    
    return system_prompt
```

### 避免时间混淆 / Avoiding Temporal Confusion

```python
# 训练时处理时间敏感内容 / Handle time-sensitive content during training
temporal_handling_strategies = {
    "explicit_timestamp": "在数据中明确标注时间戳",
    "relative_time": "使用相对时间描述（如'最近'、'去年'）",
    "context_window": "限制模型对特定时间范围的引用",
    "uncertainty_acknowledgment": "鼓励模型承认时间不确定性",
}

# 示例系统提示词修改 / Example system prompt modification
time_aware_prompt = """
You are Elon Musk. When discussing time-sensitive topics:
- Acknowledge that your knowledge has a cutoff date
- For events after 2024, express uncertainty unless specific context is provided
- Use phrases like "As of my last update..." or "Based on the timeline..."
- Be willing to say "I don't have the latest information on that"
"""
```

---

## 完整训练脚本示例 / Complete Training Script Example

```python
#!/usr/bin/env python3
"""
埃隆·马斯克语料库微调脚本
Fine-tuning script for Elon Musk Corpus
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset

# 配置 / Configuration
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
COPRUS_PATH = "musk_corpus_chatml.jsonl"
OUTPUT_DIR = "./musk-lora-model"

# LoRA 配置 / LoRA configuration
LORA_CONFIG = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

# 训练参数 / Training arguments
TRAINING_ARGS = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    logging_steps=10,
    save_strategy="epoch",
    evaluation_strategy="steps",
    eval_steps=100,
    load_best_model_at_end=True,
    fp16=True,
    report_to="tensorboard",
)

def main():
    # 加载模型和分词器 / Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    
    # 应用 LoRA / Apply LoRA
    model = get_peft_model(model, LORA_CONFIG)
    model.print_trainable_parameters()
    
    # 加载数据集 / Load dataset
    dataset = load_dataset("json", data_files=COPRUS_PATH, split="train")
    
    # 数据预处理 / Data preprocessing
    def preprocess_function(examples):
        # 将 ChatML 格式转换为文本 / Convert ChatML to text
        texts = []
        for messages in examples["messages"]:
            text = ""
            for msg in messages:
                text += f"<{msg['role']}> {msg['content']}\n"
            texts.append(text)
        
        # 分词 / Tokenize
        tokenized = tokenizer(
            texts,
            truncation=True,
            max_length=2048,
            padding="max_length",
        )
        tokenized["labels"] = tokenized["input_ids"].copy()
        return tokenized
    
    tokenized_dataset = dataset.map(
        preprocess_function,
        batched=True,
        remove_columns=dataset.column_names,
    )
    
    # 分割训练集和验证集 / Split train and validation
    train_test = tokenized_dataset.train_test_split(test_size=0.1)
    
    # 数据整理器 / Data collator
    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
        label_pad_token_id=-100,
    )
    
    # 训练器 / Trainer
    trainer = Trainer(
        model=model,
        args=TRAINING_ARGS,
        train_dataset=train_test["train"],
        eval_dataset=train_test["test"],
        data_collator=data_collator,
    )
    
    # 训练 / Train
    trainer.train()
    
    # 保存模型 / Save model
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    print(f"模型已保存到 / Model saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
```

---

## 文件清单 / File List

| 文件 / File | 说明 / Description |
|------------|-------------------|
| `fine-tuning-recommendations.md` | 本指南 / This guide |
| `fine-tuning-recommendations.json` | 结构化数据 / Structured data |
| `examples/training_script.py` | 完整训练脚本 / Complete training script |

---

## 相关资源 / Related Resources

- [ChatML Format Guide](./chatml-format-guide.md) - ChatML 格式指南
- [ShareGPT Format Guide](./sharegpt-format-guide.md) - ShareGPT 格式指南
- [System Prompts Collection](./system-prompts-collection.md) - 系统提示词集合

---

*最后更新 / Last Updated: 2026-06-01*
*版本 / Version: 1.0.0*
