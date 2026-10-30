def compare_documents(documents: list[dict]) -> dict:
    """
    Compare multiple documents.


    Each document must contain a name and text.


    Example:
    [
        {"name": "policy1.txt", "text": "Employees receive 20 days leave."},
        {"name": "policy2.txt", "text": "Employees receive 25 days leave."}
    ]
    """


    if not documents or len(documents) < 2:
        return {
            "error": "At least two documents are required."
        }


    results = []


    for document in documents:
        name = document.get("name", "Unnamed document")
        text = document.get("text", "")


        if not isinstance(text, str) or not text.strip():
            return {
                "error": f"Document '{name}' has empty or invalid text."
            }


        results.append({
            "name": name,
            "character_count": len(text),
            "word_count": len(text.split()),
            "text": text.strip()
        })


    return {
        "document_count": len(results),
        "documents": results,
        "comparison": [
            {
                "document_1": results[i]["name"],
                "document_2": results[j]["name"],
                "same_text": (
                    results[i]["text"].casefold()
                    == results[j]["text"].casefold()
                ),
                "word_count_difference": abs(
                    results[i]["word_count"]
                    - results[j]["word_count"]
                )
            }
            for i in range(len(results))
            for j in range(i + 1, len(results))
        ]
    }