#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from app.core.assistant import build_answer


BENCHMARK_PATH = Path("app/evaluation/benchmark_questions.jsonl")


def simple_keyword_score(answer: str, expected_points: list[str]) -> float:
    answer_lower = answer.lower()
    hits = 0
    for point in expected_points:
        if any(token in answer_lower for token in point.lower().split()):
            hits += 1
    return hits / max(len(expected_points), 1)


def main() -> None:
    rows = []
    with BENCHMARK_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            response = build_answer(item["question"])
            score = simple_keyword_score(response.answer, item["expected_points"])
            rows.append((item["id"], score, response.confidence))

    print("CFD assistant benchmark")
    print("-----------------------")
    for qid, score, confidence in rows:
        print(f"{qid}: score={score:.2f}, confidence={confidence}")


if __name__ == "__main__":
    main()
