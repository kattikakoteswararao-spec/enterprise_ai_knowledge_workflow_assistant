from fastapi import FastAPI
from pydantic import BaseModel, Field


from app.knowledge_base import answer_question
from app.summarization import summarize_document
from app.classification import classify_document
from app.extraction import extract_information
from app. comparison import compare_documents



# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------


app = FastAPI(
    title="Enterprise AI Knowledge & Workflow Assistant",
    description="Week 6 Python and AI Final Capstone",
    version="1.0.0",
)




# --------------------------------------------------
# Request Models
# --------------------------------------------------


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question about company policies",
    )




class SummarizeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000,
        description="Document text to summarize",
    )




class ClassifyRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000,
        description="Document text to classify",
    )




class ExtractRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000,
        description="Document text to extract information from",
    )


class CompareRequest(BaseModel):
    documents: list[dict] = Field(
        ...,
        min_length=2,
        max_length=10,
        description="At least two documents to compare",
    )



# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Knowledge Assistant is running",
        "version": "1.0.0",
    }




# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }




# --------------------------------------------------
# Document Question and Answer Endpoint
# --------------------------------------------------


@app.post("/ask")
def ask(request: QuestionRequest):
    """
    Answer a question using the company policy document.
    """
    return answer_question(request.question)




# --------------------------------------------------
# Document Summarization Endpoint
# --------------------------------------------------


@app.post("/summarize")
def summarize(request: SummarizeRequest):
    """
    Generate a simple extractive summary of supplied text.
    """
    return summarize_document(request.text)


# Document Classification Endpoint


@app.post("/classify")
def classify(request: ClassifyRequest):
    """Classify a document into a business category."""
    return classify_document(request.text)


# Document Information Extraction Endpoint


@app.post("/extract")
def extract(request: ExtractRequest):
    """Extract structured information from a document."""
    return extract_information(request.text)


# Document Comparison Endpoint

@app.post("/compare")
def compare(request: CompareRequest):
    """Compare multiple documents and return a similarity score."""
    return compare_documents(request.documents)