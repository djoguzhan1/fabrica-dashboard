# Screening / hidden requirements (T1 addon)

From job post extract:
- Questions applicant must answer in proposal
- "Start with …" instructions (e.g. RAG cause guess)
- Required word/phrase to include
- Link or file client wants in first message

Output JSON:
```json
{
  "must_answer_in_letter": ["..."],
  "hidden_keywords": [],
  "forbidden_in_letter": [],
  "client_test_instruction": ""
}
```

Writer must satisfy `must_answer_in_letter` by sentence 3 without breaking card rules (primary still leads card).
