import os
from src.competitive_crew import CompetitiveCrew

os.makedirs('output', exist_ok=True)


def run():
    """默认运行竞品分析（使用默认参数）"""
    result = CompetitiveCrew().crew().kickoff(inputs={
        'competitors': [],
        'industry': '协同办公'
    })
    return result


def run_competitive_analysis(competitors: list, industry: str) -> dict:
    """
    运行竞品分析

    Args:
        competitors: 竞品名称列表，如果为空则根据 industry 自动发现
        industry: 行业/产品领域关键词

    Returns:
        分析结果
    """
    print(f"\n{'='*60}")
    print(f"开始竞品分析")
    print(f"竞品: {competitors if competitors else '自动发现'}")
    print(f"行业: {industry}")
    print(f"{'='*60}\n")

    result = CompetitiveCrew().crew().kickoff(inputs={
        'competitors': competitors,
        'industry': industry
    })

    print(f"\n{'='*60}")
    print(f"竞品分析完成")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Competitive Analysis Crew')
    parser.add_argument('--competitors', type=str, default='',
                       help='竞品列表，逗号分隔，如 "飞书,钉钉,企业微信"')
    parser.add_argument('--industry', type=str, required=True,
                       help='行业/产品领域关键词')

    args = parser.parse_args(sys.argv[1:])

    competitors = [c.strip() for c in args.competitors.split(',') if c.strip()] if args.competitors else []

    run_competitive_analysis(competitors, args.industry)