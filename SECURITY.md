# AI Security & Governance

Security is the primary barrier to enterprise AI adoption. This section covers mitigation strategies for common risks.

## 1. Prompt Injection
- **Problem**: Users manipulating prompts to bypass safety filters.
- **Mitigation**: 
  - Use system prompts to strictly define boundaries.
  - Implement a secondary LLM "checker" to validate user inputs before they reach the primary model.

## 2. PII / Sensitive Data Leakage
- **Problem**: Accidental transmission of PII (Names, SSNs, Keys) to 3rd party LLM providers.
- **Mitigation**: 
  - Use local regex-based masking (e.g., Presidio).
  - Proxy all requests through a secure internal gateway.

## 3. Jailbreaking (System Prompt Leaks)
- **Mitigation**: 
  - Never include sensitive secrets directly in system prompts.
  - Monitor for "ignore previous instructions" patterns.

## 4. Hallucination Management
- **Mitigation**: 
  - Grounding via RAG (Retrieval Augmented Generation).
  - Citation requirement: Force the model to provide source links for every claim.
