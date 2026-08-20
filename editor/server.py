"""A minimal local code editor: browse the lesson .py files in python-basics/,
edit them in the browser, and run them with a button — output (including the
PASS/FAIL self-checks) streams back into an on-page console.

Everything happens on localhost against files already on disk. No sandboxing
beyond "only .py files inside the lessons folder" — this is a personal
learning tool, not something exposed to anyone but you.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

LESSONS_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = Path(__file__).resolve().parent / "static"

FILENAME_RE = re.compile(r"^[A-Za-z0-9_\-.]+\.py$")


def safe_lesson_path(filename: str) -> Path:
    if not FILENAME_RE.match(filename):
        raise HTTPException(400, "Invalid filename.")
    path = (LESSONS_DIR / filename).resolve()
    if path.parent != LESSONS_DIR or not path.exists():
        raise HTTPException(404, "Lesson file not found.")
    return path


app = FastAPI(title="Python Basics Editor")


@app.get("/api/files")
def list_files() -> list[str]:
    return sorted(p.name for p in LESSONS_DIR.glob("*.py"))


@app.get("/api/files/{filename}")
def read_file(filename: str) -> dict:
    path = safe_lesson_path(filename)
    return {"filename": filename, "content": path.read_text()}


class SaveBody(BaseModel):
    content: str


@app.post("/api/files/{filename}")
def save_file(filename: str, body: SaveBody) -> dict:
    path = safe_lesson_path(filename)
    path.write_text(body.content)
    return {"ok": True}


@app.post("/api/run/{filename}")
def run_file(filename: str) -> dict:
    path = safe_lesson_path(filename)
    try:
        result = subprocess.run(
            ["python3", path.name],
            cwd=str(LESSONS_DIR),
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = result.stdout + result.stderr
        return {"output": output, "returncode": result.returncode}
    except subprocess.TimeoutExpired:
        return {"output": "Timed out after 10 seconds (infinite loop?).", "returncode": -1}


app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="editor-frontend")
