"""Extract structured information from business documents."""


import re
from typing import Any




def extract_information(text: str) -> dict[str, Any]:
    """Extract dates, email addresses, amounts, and action items."""


    if not text or not text.strip():
        return {
            "dates": [],
            "emails": [],
            "amounts": [],
            "action_items": [],
        }


    dates = re.findall(
        r"\b\d{4}-\d{2}-\d{2}\b",
        text,
    )


    emails = re.findall(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        text,
    )


    amounts = re.findall(
        r"(?:₹|Rs\.?|USD|\$)\s?\d+(?:,\d{3})*(?:\.\d{2})?",
        text,
        flags=re.IGNORECASE,
    )


    action_items = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text)
        if re.search(
            r"\b(must|should|required|submit|complete|approve)\b",
            sentence,
            flags=re.IGNORECASE,
        )
    ]


    return {
        "dates": dates,
        "emails": emails,
        "amounts": amounts,
        "action_items": action_items,
    }