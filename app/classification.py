"""Simple rule-based document classification."""


from typing import Any




def classify_document(text: str) -> dict[str, Any]:
    """Classify a document using simple keyword rules."""


    if not text or not text.strip():
        return {
            "category": "unknown",
            "confidence": 0.0,
            "reason": "Document text is empty.",
        }


    content = text.lower()


    categories = {
        "HR Policy": [
            "employee", "leave", "manager", "work from home",
            "recruitment", "salary", "maternity",
        ],
        "Security Policy": [
            "password", "confidential", "security",
            "authentication", "access control",
        ],
        "Finance": [
            "invoice", "payment", "budget", "expense", "tax",
        ],
        "Technical Document": [
            "python", "api", "database", "software", "server",
        ],
    }


    scores = {
        category: sum(
            1 for keyword in keywords if keyword in content
        )
        for category, keywords in categories.items()
    }


    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]


    if best_score == 0:
        return {
            "category": "Other",
            "confidence": 0.0,
            "reason": "No matching classification keywords found.",
            "scores": scores,
        }


    total_matches = sum(scores.values())
    confidence = round(best_score / total_matches, 2)


    return {
        "category": best_category,
        "confidence": confidence,
        "reason": (
            f"Matched {best_score} keyword(s) for "
            f"{best_category}."
        ),
        "scores": scores,
    }