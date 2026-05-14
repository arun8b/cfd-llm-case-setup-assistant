from __future__ import annotations

from app.core.assistant import build_answer


def ask(question: str) -> str:
    response = build_answer(question)
    return response.answer
