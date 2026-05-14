#!/usr/bin/env python3
from __future__ import annotations

from rich.console import Console
from rich.panel import Panel

from app.core.assistant import build_answer

console = Console()


def main() -> None:
    console.print(Panel.fit("CFD-LLM Case Setup Assistant", subtitle="type 'exit' to quit"))

    while True:
        question = console.input("\n[bold cyan]CFD question>[/bold cyan] ").strip()
        if question.lower() in {"exit", "quit", "q"}:
            break
        if not question:
            continue

        response = build_answer(question)

        console.print("\n[bold]Answer[/bold]")
        console.print(response.answer)

        console.print("\n[bold]Retrieved context IDs[/bold]")
        console.print(", ".join(response.retrieved_context_ids) or "None")

        console.print(f"\n[bold]Confidence[/bold]: {response.confidence}")

        console.print("\n[bold]Suggested CFD checks[/bold]")
        for check in response.suggested_checks:
            console.print(f"- {check}")


if __name__ == "__main__":
    main()
