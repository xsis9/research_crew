#!/bin/bash
# 竞品分析运行脚本

# 获取脚本所在目录的父目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

# 激活虚拟环境
source .venv/bin/activate

# 设置 PYTHONPATH
export PYTHONPATH="$PROJECT_DIR/src:$PYTHONPATH"

# 解析命令行参数
COMPETITORS=""
INDUSTRY=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --competitors)
            COMPETITORS="$2"
            shift 2
            ;;
        --industry)
            INDUSTRY="$2"
            shift 2
            ;;
        *)
            echo "未知参数: $1"
            echo "用法: $0 --competitors '飞书,钉钉,企业微信' --industry '协同办公'"
            exit 1
            ;;
    esac
done

if [[ -z "$INDUSTRY" ]]; then
    echo "错误: --industry 参数必填"
    echo "用法: $0 --competitors '飞书,钉钉,企业微信' --industry '协同办公'"
    exit 1
fi

echo "开始竞品分析..."
echo "行业: $INDUSTRY"
if [[ -n "$COMPETITORS" ]]; then
    echo "竞品: $COMPETITORS"
fi

cd src
python -c "
import sys
sys.path.insert(0, '.')
from main import run_competitive_analysis

competitors = []
if '$COMPETITORS':
    competitors = [c.strip() for c in '$COMPETITORS'.split(',')]

run_competitive_analysis(competitors, '$INDUSTRY')
"