def summarize_document(text: str) -> dict:
    """Create a simple extractive summary of a document."""


    if not text or not text.strip():
        return {
            "summary": "",
            "message": "Please provide document text."
        }


    # Split the document into sentences.
    sentences = [
        sentence.strip()
        for sentence in text.replace("\n", " ").split(".")
        if sentence.strip()
    ]


    # Select the first three sentences.
    summary_sentences = sentences[:3]


    summary = ". ".join(summary_sentences)


    if summary:
        summary += "."


    return {
        "summary": summary,
        "original_sentence_count": len(sentences),
        "summary_sentence_count": len(summary_sentences),
        "method": "extractive"
    }