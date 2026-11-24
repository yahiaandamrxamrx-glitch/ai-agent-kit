from fastapi import FastAPI
from pydantic import BaseModel
from agent_core import AutonomousAgent, web_scraper_tool

app = FastAPI(title="AI Agent Kit API")
agent = AutonomousAgent(name="APIAgent", role="Web & App Backend")
agent.register_tool("scrape", web_scraper_tool)

class TaskRequest(BaseModel):
    task: str
    url: str

@app.post("/run-agent")
async def run_agent(req: TaskRequest):
    return await agent.execute_task(req.task, {"url": req.url})
  
