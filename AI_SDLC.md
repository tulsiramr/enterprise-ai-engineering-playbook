# AI Software Development Life Cycle (AI SDLC)

This guide outlines the process of integrating AI into the engineering workflow, from research to production monitoring.

## 1. Requirement & Feasibility
- Define the core problem: Is an LLM necessary, or is it a search problem?
- Success metrics: Accuracy, Latency, Cost per request.

## 2. Data Preparation
- Extraction from unstructured sources (PDFs, Docs).
- Chunking strategies: Fixed-size vs. Semantic chunking.
- Embedding selection: Trade-offs between OpenAI, Cohere, and Open Source (HuggingFace).

## 3. Architecture Design
- **RAG (Retrieval Augmented Generation)**: For grounding models in private data.
- **Agent Orchestration**: For multi-step complex tasks.
- **Guardrails**: Input validation and output sanitization.

## 4. Evaluation (LLM-as-a-Judge)
- Automated evaluation using Ragas or G-Eval.
- Human-in-the-loop (HITL) for edge cases.

## 5. Deployment & Monitoring
- Token usage tracking.
- Latency monitoring (TTFT - Time To First Token).
- Drift detection: Is the model's performance degrading over time?
