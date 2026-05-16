#!/bin/bash
# 竞品分析运行脚本

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 激活虚拟环境并运行
source .venv/bin/activate

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

# 转换为列表格式
if [[ -n "$COMPETITORS" ]]; then
    COMPETITORS="[${COMPETITORS//,/,\"}]"
    COMPETITORS="${COMPETITORS/,/,\"}"
else
    COMPETITORS="[]"
fi

echo "开始竞品分析..."
echo "竞品: $COMPETITORS"
echo "行业: $INDUSTRY"

python -c "
import sys
sys.path.insert(0, 'src')
from research_crew.main import run_competitive_analysis

competitors = []
if '$COMPETITORS' != '[]':
    competitors = [c.strip() for c in '$COMPETITORS'.strip('[]').replace('\"', '').split(',')]

run_competitive_analysis(competitors, '$INDUSTRY')
"