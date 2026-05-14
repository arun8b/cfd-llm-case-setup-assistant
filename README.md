# CFD-LLM Case Setup Assistant

A domain-specific **LLM/RAG assistant** for CFD case setup, solver selection, boundary-condition reasoning, mesh strategy, convergence troubleshooting and aerodynamic interpretation.

This project combines **aerospace CFD knowledge** with **LLM application development**, showing how structured engineering knowledge can be used to support simulation decision-making.

---

## Project Objective

The objective of this project is to build a lightweight engineering AI assistant that helps users reason through CFD setup and troubleshooting questions.

Example questions the assistant is designed to answer include:

- What boundary conditions should I use for an external airfoil CFD case?
- How do I choose between steady and transient CFD solvers?
- Why are residuals decreasing but lift and drag are still changing?
- How should I structure a mesh sensitivity study?
- Why does y+ matter for airfoil drag prediction?
- What should be documented in a CFD verification report?
- What does pressure recovery mean in an intake or diffuser CFD study?

The goal is not to replace a CFD engineer. The goal is to demonstrate how aerospace simulation expertise can be organised into a retrieval-based assistant with technical safeguards and evaluation criteria.

---

## Why This Project Matters

CFD workflows require judgement. A useful assistant must understand that a simulation is not credible just because a solver has run.

This project is designed to show awareness of:

- Solver suitability
- Boundary-condition consistency
- Mesh quality
- Near-wall modelling
- Turbulence model selection
- Residual and force convergence
- Mesh sensitivity
- Verification and validation
- Engineering interpretation
- Limitations and uncertainty

It demonstrates a bridge between **CFD engineering**, **scientific Python**, **retrieval-augmented generation**, **LLM evaluation** and **domain-specific AI tooling**.

---

## Core Capabilities

The current version includes:

- A curated CFD knowledge base in JSONL format
- Lightweight retrieval system using keyword and tag scoring
- CLI-based assistant interface
- Structured response generation
- CFD safety and caution rules
- Evaluation benchmark questions
- Answer-quality rubric
- Documentation for methodology, limitations and future development

---

## Repository Structure

```text
cfd-llm-case-setup-assistant/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── assistant.py
│   │   ├── retrieval.py
│   │   ├── rules.py
│   │   └── schemas.py
│   ├── data/
│   │   ├── cfd_knowledge_base.jsonl
│   │   └── example_questions.json
│   ├── prompts/
│   │   └── system_prompt.md
│   └── evaluation/
│       ├── benchmark_questions.jsonl
│       └── rubric.md
├── scripts/
│   ├── run_cli.py
│   └── evaluate_answers.py
├── docs/
│   ├── methodology.md
│   ├── model_card.md
│   └── safety_and_limitations.md
├── examples/
│   └── sample_session.md
├── tests/
│   └── test_retrieval.py
├── requirements.txt
├── project_summary.json
├── LICENSE
└── README.md
