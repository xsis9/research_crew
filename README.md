# 竞品分析 Agent 协作系统

基于 crewAI 的 AI 驱动竞品分析系统，模拟真实的数字调研小组，通过多个专职 Agent 的协同，自动完成从公开信息采集到结构化竞品报告输出的全链路工作。

## 功能特点

- **多 Agent 协作**: 采集、分析、撰写、质检四个专职 Agent 协同工作
- **DAG 任务流**: 基于上下文依赖的任务编排，确保数据流转清晰
- **溯源能力**: 每条分析结论均标注来源，支持 traceability_log 全链路追溯
- **可观测性**: 完整的执行日志和中间产物记录
- **自动/手动**: 支持自动发现竞品或手动指定竞品列表

## 目录结构

```
research_crew/
├── src/
│   ├── __init__.py
│   ├── main.py              # 入口文件
│   ├── competitive_crew.py  # Crew 定义
│   ├── config/
│   │   ├── agents.yaml      # Agent 配置
│   │   └── tasks.yaml       # Task 配置
│   ├── schema/
│   │   └── competitive_analysis.py  # 数据模型
│   └── tools/
│       └── source_tracker.py        # 来源追踪工具
├── scripts/
│   └── run_competitive_analysis.sh  # 运行脚本
├── knowledge/
│   └── competitive_schema.md        # Schema 文档
├── output/                          # 输出目录
└── pyproject.toml
```

## 环境要求

- Python 3.12
- UV (包管理工具)

## 依赖安装

```bash
# 安装 uv (如果没有)
pip install uv

# 创建虚拟环境并安装依赖
uv venv .venv
source .venv/bin/activate
uv pip install -e .
```

## 运行命令

### 方式一：使用运行脚本（推荐）

```bash
# 自动发现竞品（分析协同办公行业）
./scripts/run_competitive_analysis.sh --industry "协同办公"

# 指定竞品
./scripts/run_competitive_analysis.sh --competitors "飞书,钉钉,企业微信" --industry "协同办公"

# 其他行业
./scripts/run_competitive_analysis.sh --industry "电商平台"
./scripts/run_competitive_analysis.sh --industry "在线教育"
```

### 方式二：使用 Python 直接运行

```bash
cd src
PYTHONPATH=src python -c "
from main import run_competitive_analysis
run_competitive_analysis(['飞书', '钉钉', '企业微信'], '协同办公')
"
```

### 方式三：使用 crewai 命令

```bash
crewai run
```

## Agent 角色说明

| Agent | 角色 | 职责 |
|-------|------|------|
| Collector | 采集专家 | 从公开信息源采集竞品数据，标注来源 |
| Analyzer | 分析专家 | 基于 Schema 对数据进行结构化分析 |
| Writer | 撰写专家 | 撰写完整的竞品分析报告 |
| QA | 质检专家 | 审查报告质量和溯源能力 |

## 输出

- `output/competitive_report.md` - Markdown 格式报告
- `output/competitive_report.json` - JSON 格式数据（含溯源信息）

## 配置

在 `.env` 文件中配置 API Key：

```bash
ANTHROPIC_API_KEY=your_api_key
ANTHROPIC_BASE_URL=https://api.minimaxi.com/anthropic
MODEL=MiniMax-M2.7
SERPER_API_KEY=your_serper_key  # 可选，用于网络搜索
```

## License

MIT