# 竞品分析知识 Schema

本 Schema 定义了竞品分析报告的数据结构，确保每条分析结论均可溯源。

## 核心概念

### 1. Source (信息来源)
每条分析结论必须标注来源，包括：
- source_id: 唯一标识符 (格式: src_001)
- url: 来源URL
- title: 来源标题
- credibility: 可信度等级 (high/medium/low)
- collected_at: 采集时间

### 2. Finding (分析结论)
每个分析结论必须包含：
- content: 具体分析内容
- source_ids: 来源ID列表（支持多个来源）
- confidence: 置信度 (0-1)
- category: 分类 (product/feature/pricing/market/tech)

### 3. ProductProfile (产品画像)
- name: 产品名称
- positioning: 产品定位
- target_users: 目标用户群体
- website: 官网地址

### 4. FeatureComparison (功能对比)
针对每个产品记录：
- 核心功能列表
- 功能描述
- 与竞品对比的优劣势

### 5. PricingStrategy (定价策略)
- pricing_model: 定价模式 (freemium/subscription/one-time/usage-based)
- price_range: 价格区间
- free_tier: 免费套餐说明

### 6. MarketAnalysis (市场分析)
- market_share: 市场份额
- user_feedback: 用户评价摘要

### 7. TechnologyAnalysis (技术架构)
- tech_stack: 技术栈
- innovation_points: 创新点

### 8. SWOTAnalysis (SWOT分析)
- strengths: 优势
- weaknesses: 劣势
- opportunities: 机会
- threats: 威胁

### 9. TraceabilityLog (溯源日志)
每个 Agent 的执行记录：
- agent: 执行Agent名称
- action: 执行动作
- inputs: 输入内容
- outputs: 输出内容
- timestamp: 执行时间

## 溯源要求

1. **每结论必标源**: 每个 Finding 必须关联至少一个 Source
2. **源信息完整**: URL、标题、可信度、采集时间缺一不可
3. **决策可追溯**: 每个 Agent 的中间产物必须记录到 TraceabilityLog
4. **交叉验证**: 重要结论应有多个独立来源支持

## 输出格式

最终报告包含：
1. `competitive_report.json` - 结构化JSON，含完整溯源信息
2. `competitive_report.md` - Markdown报告，含来源标注