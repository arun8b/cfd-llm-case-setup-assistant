# CFD-LLM Case Setup Assistant

A domain-specific LLM/RAG assistant for **CFD case setup, solver selection, boundary-condition reasoning, mesh strategy, convergence troubleshooting and aerodynamic interpretation**.

This project is designed as a professional portfolio repository connecting:

- Aerospace CFD knowledge
- OpenFOAM/SU2-style case setup reasoning
- Python engineering automation
- Retrieval-Augmented Generation, RAG
- LLM evaluation and prompt engineering
- Technical answer quality control

The aim is not to build a generic chatbot. The aim is to demonstrate how domain-specific aerospace simulation knowledge can be structured into a retrieval and evaluation pipeline that supports practical CFD decision-making.

---

## Project Objective

The assistant answers engineering questions such as:

- Which boundary conditions should I use for an external airfoil CFD case?
- How do I choose between `simpleFoam`, `pimpleFoam` and SU2 RANS workflows?
- Why are my residuals decreasing but lift and drag are not converged?
- How should I plan a mesh sensitivity study?
- Why is y+ important for airfoil drag prediction?
- What does pressure recovery mean in an intake/diffuser CFD study?
- How should I document CFD verification and validation evidence?

The system uses a small local knowledge base and a retrieval step before producing an answer. It also includes an evaluation rubric so answers can be scored for technical quality.

---

## Why This Project Matters

CFD and simulation workflows require judgement. A useful engineering assistant must avoid shallow answers and must be able to reason about:

- solver suitability
- boundary-condition consistency
- mesh quality
- turbulence modelling
- convergence criteria
- coefficient extraction
- verification and validation
- uncertainty and limitations

This project demonstrates the ability to combine aerospace engineering expertise with LLM application development.

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
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## Quick Start

### 1. Create a Python environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Run the CLI assistant

```bash
python scripts/run_cli.py
```

Example question:

```text
For a 2D external airfoil RANS case, what boundary conditions and convergence checks should I use?
```

---

## Current Implementation

This repository includes a lightweight retrieval system based on keyword scoring. It is intentionally dependency-light so the project can run immediately.

The scaffold can later be upgraded to:

- vector embeddings
- FAISS or Chroma
- OpenAI, Anthropic, local Llama or Mistral models
- Streamlit user interface
- OpenFOAM/SU2 documentation ingestion
- automatic CFD log diagnosis
- fine-tuning dataset export

---

## Knowledge Base

The knowledge base is stored in:

```text
app/data/cfd_knowledge_base.jsonl
```

Each line contains a structured CFD knowledge item:

```json
{
  "id": "bc_external_airfoil_001",
  "topic": "boundary conditions",
  "question": "What boundary conditions are used for an external airfoil CFD case?",
  "answer": "For an external airfoil case, use a velocity inlet or freestream farfield, pressure outlet or farfield outlet, no-slip wall on the airfoil, and symmetry/empty boundaries for a 2D case...",
  "tags": ["airfoil", "boundary conditions", "openfoam", "rans"]
}
```

---

## Evaluation

The project includes an evaluation framework in:

```text
app/evaluation/
```

The assistant can be scored on:

- technical correctness
- CFD reasoning depth
- solver and boundary-condition awareness
- recognition of uncertainty
- clarity and actionability
- avoidance of hallucinated claims

---

## Example Output

Question:

```text
Why can residuals converge while lift and drag are still changing?
```

Expected answer quality:

```text
Residual convergence only shows that equation imbalances are reducing. It does not guarantee that integrated aerodynamic quantities have stabilised. In airfoil CFD, CL and CD can continue to drift because the wake, pressure distribution, separation region or near-wall solution is still evolving. A credible convergence check should monitor both residuals and force coefficients, and the final report should show that CL/CD have reached a stable plateau.
```

---

## Portfolio Value

This project demonstrates:

- CFD workflow knowledge
- OpenFOAM/SU2 reasoning
- aerospace simulation judgement
- Python software structure
- RAG-style assistant design
- LLM evaluation thinking
- engineering AI communication

---

## Recruiter-Facing Summary

Built a domain-specific CFD LLM assistant for simulation case setup, solver selection, boundary-condition reasoning and convergence troubleshooting. The project combines aerospace CFD expertise, Python retrieval pipelines, structured knowledge-base design and LLM answer-evaluation methods.

---

## Author

**Arun Mony Damodaran**  
Aerospace Engineer | CFD | Flight Testing | High-Speed Aerodynamics | Simulation | Engineering AI
