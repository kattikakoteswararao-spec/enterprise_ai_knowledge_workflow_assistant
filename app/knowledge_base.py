from pathlib import Path


DOCUMENT_PATH = (
    Path(__file__).resolve().parent.parent
    / "documents"
    / "company_policy.txt"
)




def load_document() -> str:
    """Load the company policy document."""
    if not DOCUMENT_PATH.exists():
        raise FileNotFoundError(
            f"Company policy document not found: {DOCUMENT_PATH}"
        )


    return DOCUMENT_PATH.read_text(encoding="utf-8")




def answer_question(question: str) -> dict:
    """Return relevant policy information for a question."""
    if not question or not question.strip():
        return {
            "answer": "Please provide a valid question.",
            "supported": False,
        }


    text = load_document().lower()
    question_lower = question.lower()


    topics = {
    "annual leave": [
        "annual leave",
        "leave entitlement",
        "yearly leave",
        "vacation days",
        "vacation",
        "time-off allowance",
        "days off",
        "leave benefit",
        "leave days",
    ],
    "work from home": [
        "work from home",
        "work-from-home",
        "remote work",
        "working from home",
        "work at home",
        "home working",
        "home-based work",
        "wfh",
        "working remotely",
        "work remotely",
        "allow working remotely",
        "work remotely from home",
        "ask to work remotely",
        "company allow working remotely",
    ],
    "manager": [
        "approve leave",
        "approves leave",
        "leave approval",
        "leave requests",
        "time-off requests",
        "approval authority",
        "signs off on leave",
        "approval decisions",
        "who approves employee leave",
        "who approves leave",
        "who is responsible for approving leave",
        "who reviews leave applications",
        "who needs to approve a leave application",
        "who must authorize employee leave",
        "what happens when employees request leave",
    ],
    "password security": [
        "password",
        "passwords",
    ],
    "security incidents": [
        "security incident",
        "security incidents",
        "report an incident",
    ],
    "training": [
        "training",
        "security awareness",
    ],
}
    
    sections = text.split("\n\n")


    for topic, keywords in topics.items():
        if any(keyword in question_lower for keyword in keywords):
            for section in sections:
                section_lower = section.lower()


                # Match the question topic to the correct policy heading.
                if topic in section_lower:
                    return {
                        "answer": section.strip(),
                        "supported": True,
                        "source": "company_policy.txt",
                    }


    return {
        "answer": (
            "I could not find sufficient information in the "
            "available company policy document."
        ),
        "supported": False,
    }