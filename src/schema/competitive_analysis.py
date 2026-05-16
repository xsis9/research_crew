from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class Source(BaseModel):
    """信息源追溯模型"""
    source_id: str = Field(..., description="唯一标识符，格式: src_001")
    url: str = Field(..., description="来源URL")
    title: str = Field(..., description="来源标题")
    credibility: str = Field(..., description="可信度: high/medium/low")
    collected_at: str = Field(default_factory=lambda: datetime.now().isoformat(), description="采集时间")


class Finding(BaseModel):
    """分析结论模型，包含溯源信息"""
    content: str = Field(..., description="具体分析内容")
    source_ids: List[str] = Field(..., description="来源ID列表")
    confidence: float = Field(..., ge=0.0, le=1.0, description="置信度 0-1")
    category: str = Field(..., description="分类: product/feature/pricing/market/tech")


class ProductProfile(BaseModel):
    """产品画像"""
    name: str = Field(..., description="产品名称")
    positioning: str = Field(..., description="产品定位")
    target_users: List[str] = Field(..., description="目标用户群体")
    website: Optional[str] = Field(None, description="官网地址")
    source_ids: List[str] = Field(default_factory=list, description="来源ID列表")


class FeatureComparison(BaseModel):
    """功能对比"""
    product: str = Field(..., description="产品名称")
    features: List[Dict[str, Any]] = Field(..., description="功能列表，包含名称、描述、优缺点")
    source_ids: List[str] = Field(default_factory=list)


class PricingStrategy(BaseModel):
    """定价策略"""
    product: str = Field(..., description="产品名称")
    pricing_model: str = Field(..., description="定价模式: freemium/subscription/one-time/usage-based")
    price_range: Optional[str] = Field(None, description="价格区间")
    free_tier: Optional[str] = Field(None, description="免费套餐说明")
    source_ids: List[str] = Field(default_factory=list)


class MarketAnalysis(BaseModel):
    """市场分析"""
    product: str = Field(..., description="产品名称")
    market_share: Optional[str] = Field(None, description="市场份额估计")
    user_feedback: List[Dict[str, str]] = Field(default_factory=list, description="用户评价摘要")
    source_ids: List[str] = Field(default_factory=list)


class TechnologyAnalysis(BaseModel):
    """技术架构分析"""
    product: str = Field(..., description="产品名称")
    tech_stack: List[str] = Field(default_factory=list, description="技术栈列表")
    innovation_points: List[str] = Field(default_factory=list, description="创新点")
    source_ids: List[str] = Field(default_factory=list)


class SWOTItem(BaseModel):
    """SWOT 分析项"""
    content: str = Field(..., description="具体描述")
    source_ids: List[str] = Field(default_factory=list, description="来源ID列表")


class SWOTAnalysis(BaseModel):
    """SWOT 分析"""
    strengths: List[SWOTItem] = Field(default_factory=list)
    weaknesses: List[SWOTItem] = Field(default_factory=list)
    opportunities: List[SWOTItem] = Field(default_factory=list)
    threats: List[SWOTItem] = Field(default_factory=list)


class TraceabilityLog(BaseModel):
    """溯源日志"""
    agent: str = Field(..., description="执行 Agent")
    action: str = Field(..., description="执行动作")
    inputs: List[str] = Field(default_factory=list, description="输入内容")
    outputs: List[str] = Field(default_factory=list, description="输出内容")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class CompetitiveAnalysisReport(BaseModel):
    """竞品分析报告完整模型"""
    report_id: str = Field(..., description="报告唯一ID")
    industry: str = Field(..., description="行业领域")
    competitors: List[str] = Field(..., description="分析的竞品列表")
    products: List[ProductProfile] = Field(default_factory=list)
    feature_comparisons: List[FeatureComparison] = Field(default_factory=list)
    pricing_strategies: List[PricingStrategy] = Field(default_factory=list)
    market_analyses: List[MarketAnalysis] = Field(default_factory=list)
    tech_analyses: List[TechnologyAnalysis] = Field(default_factory=list)
    swot: SWOTAnalysis = Field(default_factory=lambda: SWOTAnalysis())
    sources: Dict[str, Source] = Field(default_factory=dict, description="所有来源信息字典")
    findings: List[Finding] = Field(default_factory=list, description="所有分析结论")
    traceability_logs: List[TraceabilityLog] = Field(default_factory=list)
    generated_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    approved: bool = Field(default=False, description="QA是否批准")
    qa_feedback: Optional[str] = Field(None, description="QA反馈意见")