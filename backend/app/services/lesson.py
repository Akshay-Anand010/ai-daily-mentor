import json
from datetime import date
from openai import OpenAI
from app.core.config import settings

CURRICULUM = ["LLMs", "Transformers", "Attention", "Embeddings", "Vector Databases", "RAG", "Prompt Engineering", "MCP", "Agents", "Memory", "LangGraph", "AI System Design", "Evaluation", "Fine-tuning", "Production AI"]

def demo_lesson(topic: str) -> str:
    return f'''# {topic}: building useful AI systems
## Daily objective
Explain {topic} clearly, then identify one engineering trade-off before production use.
## Executive summary
{topic} becomes valuable when it is connected to a measurable user outcome, reliable data, and an evaluation loop. This lesson moves from the mental model to an implementation plan.
## Why it matters
Teams often optimize demos rather than outcomes. The durable advantage is an observable, safe system that can be improved with real feedback.
## Beginner explanation
Think of {topic} as a focused tool: give it a clear job, useful context, and a way to check its work.
## Engineering explanation
Separate ingestion, retrieval or inference, orchestration, and evaluation. Version prompts and datasets, record latency and cost, and design a graceful fallback.
## Real-world example
A support assistant retrieves approved policy passages, cites them, and routes uncertain answers to an agent.
## Python example
```python
def answer(query, retrieve, model):
    context = retrieve(query, limit=4)
    return model.generate(query=query, context=context)
```
## Java example
```java
String answer(String query) {{ return model.generate(query, retriever.find(query)); }}
```
## Architecture diagram
`User → API → Retrieval → Model → Evaluation/Logs → User`
## Interview questions
1. How would you evaluate correctness? 2. Where can data leakage occur? 3. What is the fallback?
## Quiz
What should be versioned alongside a prompt? **Answer:** its model, context data, and evaluation set.
## Key takeaways
- Start with a measurable job.
- Observe quality, cost, latency, and safety.
- Build a fallback before scaling.
## References
- Official vendor documentation and your evaluated internal sources.
'''

def generate_lesson(topic: str, articles: list[dict]) -> tuple[str, str]:
    if not settings.openai_api_key:
        return f"Daily Mentor: {topic}", demo_lesson(topic)
    prompt = f"Create one coherent 15-minute Markdown lesson on {topic}. Include objective, executive summary, major news, why it matters, beginner and engineering explanations, real examples, Java and Python code, ASCII architecture diagram, interview questions, quiz, takeaways, references. Synthesize these sources: {json.dumps(articles[:10])}"
    response = OpenAI(api_key=settings.openai_api_key).responses.create(model=settings.openai_model, input=prompt)
    return f"Daily Mentor: {topic}", response.output_text
