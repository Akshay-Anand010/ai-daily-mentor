import feedparser

SOURCES = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "DeepLearning.AI": "https://www.deeplearning.ai/the-batch/feed/",
}
def collect_articles() -> list[dict]:
    items, seen = [], set()
    for source, url in SOURCES.items():
        try:
            for entry in feedparser.parse(url).entries[:8]:
                link = entry.get("link", "")
                if link and link not in seen:
                    seen.add(link); items.append({"source": source, "title": entry.get("title", ""), "url": link, "summary": entry.get("summary", "")[:500]})
        except Exception:
            continue
    return items
