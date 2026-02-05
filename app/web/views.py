from __future__ import annotations

from html import escape


def page_template(body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang=\"zh\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>OpenManus GUI</title>
  <style>
    body {{ font-family: system-ui, -apple-system, sans-serif; margin: 2rem; }}
    .container {{ max-width: 900px; margin: 0 auto; }}
    textarea {{ width: 100%; min-height: 160px; }}
    select, button {{ padding: 0.5rem; font-size: 1rem; }}
    pre {{ background: #f6f8fa; padding: 1rem; white-space: pre-wrap; }}
    .meta {{ color: #666; font-size: 0.9rem; }}
  </style>
</head>
<body>
  <div class=\"container\">
    {body}
  </div>
</body>
</html>"""


def index_page() -> str:
    body = """
<h1>OpenManus GUI</h1>
<p class=\"meta\">输入你的任务，选择执行模式后提交。</p>
<form method=\"post\" action=\"/run\">
  <label for=\"prompt\">任务描述</label><br />
  <textarea id=\"prompt\" name=\"prompt\" placeholder=\"例如：帮我整理一份调研摘要...\"></textarea><br /><br />
  <label for=\"mode\">执行模式</label><br />
  <select id=\"mode\" name=\"mode\">
    <option value=\"direct\">直接执行（Manus）</option>
    <option value=\"planning\">规划执行（PlanningFlow）</option>
  </select>
  <br /><br />
  <button type=\"submit\">开始执行</button>
</form>
"""
    return page_template(body)


def result_page(mode_label: str, prompt: str, result: str) -> str:
    body = f"""
<h1>OpenManus GUI</h1>
<p class=\"meta\">执行模式：{escape(mode_label)}</p>
<h2>输入</h2>
<pre>{escape(prompt)}</pre>
<h2>输出</h2>
<pre>{escape(result)}</pre>
<p><a href=\"/\">返回继续</a></p>
"""
    return page_template(body)
