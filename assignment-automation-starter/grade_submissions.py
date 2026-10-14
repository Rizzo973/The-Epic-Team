"""Example starter: extract text submissions and compare code to a JSON key.

Student code is treated as text and is never executed.
"""

import argparse
import csv
import json
from pathlib import Path


def normalize(code):
    # Preserve indentation; ignore outer blank lines and trailing spaces.
    lines = code.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(line.rstrip() for line in lines)


def parse_submission(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    student_ids = [line.split(":", 1)[1].strip()
                   for line in lines if line.startswith("STUDENT_ID:")]
    if len(student_ids) != 1 or not student_ids[0] or student_ids[0] == "REPLACE_WITH_YOUR_ID":
        raise ValueError("Provide exactly one completed STUDENT_ID line.")

    answers = {}
    index = 0
    while index < len(lines):
        if not lines[index].startswith("QUESTION:"):
            index += 1
            continue
        question_id = lines[index].split(":", 1)[1].strip()
        if not question_id or question_id in answers:
            raise ValueError("Empty or duplicate question ID.")
        index += 1
        block = []
        while index < len(lines) and not lines[index].startswith("QUESTION:"):
            block.append(lines[index])
            index += 1
        markers = ["CODE:", "END_CODE", "EXPLANATION:", "END_EXPLANATION"]
        if any(block.count(marker) != 1 for marker in markers):
            raise ValueError(f"{question_id}: missing or duplicate answer marker.")
        start, end, explanation_start, explanation_end = [block.index(m) for m in markers]
        if not start < end < explanation_start < explanation_end:
            raise ValueError(f"{question_id}: answer markers are out of order.")
        answers[question_id] = {
            "code": "\n".join(block[start + 1:end]),
            "explanation": "\n".join(block[explanation_start + 1:explanation_end]),
        }
    if not answers:
        raise ValueError("No QUESTION blocks found.")
    return student_ids[0], answers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submissions", default="submissions", help="Folder of .txt submissions")
    parser.add_argument("--key", default="solution_key.json")
    parser.add_argument("--output", default="results/grades.csv")
    args = parser.parse_args()

    key = json.loads(Path(args.key).read_text(encoding="utf-8-sig"))["questions"]
    paths = sorted(Path(args.submissions).glob("*.txt"))
    if not paths:
        parser.error("No .txt submissions found. Check --submissions.")
    rows = []
    errors = 0
    for path in paths:
        try:
            student_id, answers = parse_submission(path)
            unknown = set(answers) - set(key)
            if unknown:
                raise ValueError(f"Unknown question IDs: {', '.join(sorted(unknown))}")
        except (ValueError, OSError) as error:
            errors += 1
            rows.append({"submission_file": path.name, "status": "parse_error", "note": str(error)})
            continue
        for question_id, solution in key.items():
            answer = answers.get(question_id, {"code": "", "explanation": ""})
            code = answer["code"]
            if not code.strip() or "PLACEHOLDER" in code:
                status = "missing"
            elif normalize(code) == normalize(solution["expected_code"]):
                status = "matches_key"
            else:
                status = "review_needed"
            rows.append({
                "submission_file": path.name, "student_id": student_id,
                "question_id": question_id, "code": code,
                "explanation": answer["explanation"], "status": status,
                "points_earned": solution["points"] if status == "matches_key" else 0,
                "points_possible": solution["points"],
                "note": "Provisional text comparison; instructor review required.",
            })

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["submission_file", "student_id", "question_id", "code", "explanation",
              "status", "points_earned", "points_possible", "note"]
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {output}. Files with parse errors: {errors}.")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
