# Shared helpers for AIF-C01 topic pages
import json
from pathlib import Path


def box(cls, title, html):
    return f'<div class="{cls}"><h3>{title}</h3>{html}</div>'


def meaning(p):
    return box("ok", "Information", f"<p>{p}</p>")


def exam(p):
    return box("exam", "How they ask this on AIF-C01", f"<p>{p}</p>")


def trap(p):
    return box("warn", "Common trap", f"<p>{p}</p>")


def h2(t):
    return f"<h2>{t}</h2>"


def p(t):
    return f"<p>{t}</p>"


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for r in rows:
        trs += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return f"<table><tr>{th}</tr>{trs}</table>"


def q_single(stem, choices, ai, explain):
    return {"type": "single", "stem": stem, "choices": choices, "answer": [ai], "explain": explain}


def q_multi(stem, choices, ans, explain):
    return {"type": "multi", "stem": stem, "choices": choices, "answer": ans, "explain": explain}


def q_order(stem, items, answer, explain):
    return {"type": "order", "stem": stem, "items": items, "answer": answer, "explain": explain}


def q_match(stem, left, right, answer, explain):
    return {
        "type": "match",
        "stem": stem,
        "left": left,
        "right": right,
        "answer": answer,
        "explain": explain,
    }


def topic(tid, domain, task, title, lead, body, quiz):
    out = []
    for i, q in enumerate(quiz, 1):
        item = dict(q)
        item["id"] = f"{tid}-q{i:02d}"
        item["domain"] = domain
        out.append(item)
    return {
        "id": tid,
        "domain": domain,
        "task": task,
        "title": title,
        "lead": lead,
        "body": body,
        "quiz": out,
    }


def emit(topics, dest):
    dest = Path(dest)
    js = "(function(){\nwindow.AIF = window.AIF || {};\nwindow.AIF.topics = "
    js += json.dumps(topics, ensure_ascii=False)
    js += ";\n})();\n"
    dest.write_text(js, encoding="utf-8")
    print(f"Wrote {len(topics)} topics -> {dest} ({dest.stat().st_size} bytes)")
