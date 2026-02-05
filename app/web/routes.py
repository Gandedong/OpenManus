from __future__ import annotations

from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from app.web.service import normalize_prompt, run_task
from app.web.views import index_page, page_template, result_page

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index() -> str:
    return index_page()


@router.post("/run", response_class=HTMLResponse)
async def run(prompt: str = Form(...), mode: str = Form("direct")) -> str:
    cleaned_prompt = normalize_prompt(prompt)
    if not cleaned_prompt:
        return page_template(
            "<p>请输入任务描述。</p><p><a href=\"/\">返回</a></p>"
        )

    mode_label, result = await run_task(cleaned_prompt, mode)
    return result_page(mode_label, cleaned_prompt, result or "(无输出)")
