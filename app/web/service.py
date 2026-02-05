from __future__ import annotations

from typing import Optional

from app.agent.manus import Manus
from app.flow.base import FlowType
from app.flow.flow_factory import FlowFactory


def normalize_prompt(prompt: str) -> str:
    return prompt.strip()


async def run_direct(prompt: str) -> str:
    agent = Manus()
    return await agent.run(prompt)


async def run_planning(prompt: str) -> str:
    flow = FlowFactory.create_flow(
        flow_type=FlowType.PLANNING,
        agents={"manus": Manus()},
    )
    return await flow.execute(prompt)


async def run_task(prompt: str, mode: str) -> tuple[str, str]:
    if mode == "planning":
        return "规划执行（PlanningFlow）", await run_planning(prompt)
    return "直接执行（Manus）", await run_direct(prompt)
