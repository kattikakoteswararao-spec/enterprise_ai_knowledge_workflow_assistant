import sys
from pathlib import Path
import json
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.knowledge_base import answer_question




EVALUATION_DATASET = [
    {
        "question": "How many annual leave days do employees receive?",
        "expected": "20 days",
    },
    {
        "question": "Who must approve leave requests?",
        "expected": "manager",
    },
    {
        "question": "Can employees request work from home?",
        "expected": "work from home",
    },
    {
        "question": "What is the annual leave policy?",
        "expected": "20 days",
    },
    {
        "question": "Can managers approve leave requests?",
        "expected": "manager",
    },
    {
        "question": "How many days of annual leave are provided?",
        "expected": "20 days",
    },
    {
        "question": "Who approves employee leave?",
        "expected": "manager",
    },
    {
        "question": "Is remote work allowed?",
        "expected": "work from home",
    },
    {
        "question": "Can staff work from home?",
        "expected": "work from home",
    },
    {
        "question": "What happens when employees request leave?",
        "expected": "manager",
    },
    {
        "question": "How much annual leave can an employee take?",
        "expected": "20 days",
    },
    {
        "question": "Who is responsible for approving leave?",
        "expected": "manager",
    },
    {
        "question": "Does the company allow working remotely?",
        "expected": "work from home",
    },
    {
        "question": "How many vacation days are available?",
        "expected": "20 days",
    },
    {
        "question": "Can an employee ask to work remotely?",
        "expected": "work from home",
    },
    {
        "question": "Who reviews leave applications?",
        "expected": "manager",
    },
    {
        "question": "What is the employee leave entitlement?",
        "expected": "20 days",
    },
    {
        "question": "Are work-from-home requests permitted?",
        "expected": "work from home",
    },
    {
        "question": "Who should approve an employee vacation?",
        "expected": "manager",
    },
    {
        "question": "What is the yearly leave allowance?",
        "expected": "20 days",
    },
    {
        "question": "Is home working permitted by the policy?",
        "expected": "work from home",
    },
    {
        "question": "Who approves time-off requests?",
        "expected": "manager",
    },
    {
        "question": "How many annual vacation days do staff get?",
        "expected": "20 days",
    },
    {
        "question": "Can staff submit work-from-home requests?",
        "expected": "work from home",
    },
    {
        "question": "Which person approves leave?",
        "expected": "manager",
    },
    {
        "question": "What annual leave benefit do employees receive?",
        "expected": "20 days",
    },
    {
        "question": "Does the company support remote working?",
        "expected": "work from home",
    },
    {
        "question": "Who authorizes annual leave?",
        "expected": "manager",
    },
    {
        "question": "How much paid annual leave is provided?",
        "expected": "20 days",
    },
    {
        "question": "Can employees request remote work arrangements?",
        "expected": "work from home",
    },
    {
        "question": "Who needs to approve a leave application?",
        "expected": "manager",
    },
    {
        "question": "What is the annual time-off allowance?",
        "expected": "20 days",
    },
    {
        "question": "Are employees allowed to work at home?",
        "expected": "work from home",
    },
    {
        "question": "Who makes leave approval decisions?",
        "expected": "manager",
    },
    {
        "question": "How many leave days does the policy provide?",
        "expected": "20 days",
    },
    {
        "question": "Is working from home an available option?",
        "expected": "work from home",
    },
    {
        "question": "Who is the leave approval authority?",
        "expected": "manager",
    },
    {
        "question": "How many days off are given annually?",
        "expected": "20 days",
    },
    {
        "question": "Can employees work remotely from home?",
        "expected": "work from home",
    },
    {
        "question": "Who must authorize employee leave?",
        "expected": "manager",
    },
    {
        "question": "What is the number of annual leave days?",
        "expected": "20 days",
    },
    {
        "question": "Does the policy mention work from home?",
        "expected": "work from home",
    },
    {
        "question": "Who handles leave approvals?",
        "expected": "manager",
    },
    {
        "question": "What is the yearly vacation entitlement?",
        "expected": "20 days",
    },
    {
        "question": "May employees ask to work from home?",
        "expected": "work from home",
    },
    {
        "question": "Who approves staff leave requests?",
        "expected": "manager",
    },
    {
        "question": "How many annual leave days are allowed?",
        "expected": "20 days",
    },
    {
        "question": "Can workers request home-based work?",
        "expected": "work from home",
    },
    {
        "question": "Who signs off on leave requests?",
        "expected": "manager",
    },
    {
        "question": "What is the company's annual leave allowance?",
        "expected": "20 days",
    },
]




def run_evaluation():
    results = []


    for item in EVALUATION_DATASET:
        start_time = time.perf_counter()


        try:
            raw_answer = answer_question(item["question"])


            if isinstance(raw_answer, dict):
                answer = str(raw_answer.get("answer", raw_answer))
            else:
                answer = str(raw_answer)
            error = None
        except Exception as exc:
            answer = ""
            error = str(exc)


        latency_ms = round(
            (time.perf_counter() - start_time) * 1000, 2
        )


        # Check whether the expected phrase appears in the answer.
        expected = item["expected"].casefold().strip()
        actual = answer.casefold().strip()
        
        passed = expected in actual


        results.append(
            {
                "question": item["question"],
                "expected": item["expected"],
                "answer": answer,
                "passed": passed,
                "latency_ms": latency_ms,
                "error": error,
            }
        )


    total = len(results)
    passed_count = sum(result["passed"] for result in results)
    failed_count = total - passed_count


    report = {
        "total_questions": total,
        "passed": passed_count,
        "failed": failed_count,
        "accuracy_percent": round(
            passed_count / total * 100, 2
        ) if total else 0,
        "average_latency_ms": round(
            sum(r["latency_ms"] for r in results) / total, 2
        ) if total else 0,
        "results": results,
    }


    report_path = (
        Path(__file__).resolve().parent / "evaluation_report.json"
    )


    report_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )


    print(f"Total questions: {total}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Accuracy: {report['accuracy_percent']}%")
    print(f"Average latency: {report['average_latency_ms']} ms")
    print(f"Report saved to: {report_path}")




if __name__ == "__main__":
    run_evaluation()