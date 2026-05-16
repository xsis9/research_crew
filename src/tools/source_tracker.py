from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from datetime import datetime


class SourceTrackerInput(BaseModel):
    """Input schema for SourceTracker."""
    action: str = Field(..., description="操作类型: register/query/list")
    url: str = Field(None, description="来源URL (register时必填)")
    title: str = Field(None, description="来源标题 (register时必填)")
    content: str = Field(None, description="要溯源的内容片段 (query时使用)")
    source_id: str = Field(None, description="来源ID (query/list时使用)")


class SourceTracker(BaseTool):
    """来源追踪工具 - 用于记录和查询分析结论的来源信息"""
    name: str = "source_tracker"
    description: str = (
        "来源追踪工具，用于记录分析结论的信息源并提供溯源查询。"
        "支持三种操作: register(注册来源)、query(查询来源)、list(列出所有来源)"
    )
    args_schema: Type[BaseModel] = SourceTrackerInput

    def __init__(self):
        super().__init__()
        self._sources = {}  # source_id -> Source info
        self._content_to_sources = {}  # content hash -> source_ids

    def _run(self, action: str, url: str = None, title: str = None,
             content: str = None, source_id: str = None) -> str:
        """执行来源追踪操作"""

        if action == "register":
            if not url or not title:
                return "Error: url and title are required for register action"

            # 生成 source_id
            source_id = f"src_{len(self._sources) + 1:03d}"
            timestamp = datetime.now().isoformat()

            source_info = {
                "source_id": source_id,
                "url": url,
                "title": title,
                "collected_at": timestamp
            }

            self._sources[source_id] = source_info

            # 建立内容到来源的映射（用于后续溯源）
            if content:
                content_hash = str(hash(content))
                if content_hash not in self._content_to_sources:
                    self._content_to_sources[content_hash] = []
                self._content_to_sources[content_hash].append(source_id)

            return f"Source registered: {source_id} - {title}"

        elif action == "query":
            if content:
                content_hash = str(hash(content))
                source_ids = self._content_to_sources.get(content_hash, [])
                if source_ids:
                    result = [f"{sid}: {self._sources.get(sid, {}).get('title', 'Unknown')}"
                             for sid in source_ids]
                    return f"Sources for content: {', '.join(result)}"
                return "No sources found for this content"

            if source_id:
                source = self._sources.get(source_id)
                if source:
                    return f"{source_id}: {source['title']} ({source['url']})"
                return f"Source {source_id} not found"

            return "Error: content or source_id required for query"

        elif action == "list":
            if not self._sources:
                return "No sources registered yet"

            result = ["Registered Sources:"]
            for sid, info in self._sources.items():
                result.append(f"  {sid}: {info['title']} ({info['url']})")
            return "\n".join(result)

        return f"Unknown action: {action}"

    def get_sources(self) -> dict:
        """获取所有来源信息（供外部使用）"""
        return self._sources.copy()