import asyncio
from typing import Dict, Any, Callable

class AutonomousAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.tools: Dict[str, Callable] = {}

    def register_tool(self, tool_name: str, func: Callable):
        self.tools[tool_name] = func

    async def execute_task(self, task: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if task not in self.tools:
            return {"status": "error", "message": f"Tool '{task}' not found."}
        
        result = await self.tools[task](**payload)
        return {"agent": self.name, "status": "success", "data": result}

async def web_scraper_tool(url: str) -> str:
    await asyncio.sleep(0.5)
    return f"Extracted structured data from {url}"

if __name__ == "__main__":
    agent = AutonomousAgent(name="CoreBot", role="System Automation")
    agent.register_tool("scrape", web_scraper_tool)
    output = asyncio.run(agent.execute_task("scrape", {"url": "https://example.com"}))
    print(output)
      
